import multiprocessing
import random
import threading
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from queue import Queue
from typing import List, Optional, Union

from llama_server_client import LlamaClient
from llama_server_client.schema import ChatCompletionRequest, Message, MessageRole, ChatCompletion, SessionStateRequest, \
    SessionState, ChatCompletionChunk


@dataclass
class ChatCompletionResult:
    session_uuid: uuid.UUID
    country: str
    prompt: List[str]
    answer: Optional[str] = None


output_queue = Queue()


def output_worker():
    while True:
        result = output_queue.get()

        # check if we should stop
        if result is not None and isinstance(result, str):
            if result == "STOP":
                break

        # print the result
        print(f"=== Session {result.session_uuid} is about {result.country} ===")
        for i in range(len(result.prompt)):
            print(f"** Question{i}: {result.prompt[i]}")
        if result.answer is not None:
            print(f"## Answer: {result.answer}")
        output_queue.task_done()


def get_chat_completion_result(country: str,
                               messages: List[Message],
                               response: Union[str, ChatCompletion, None],
                               session_uuid: uuid) -> ChatCompletionResult:
    questions = [message.content for message in messages]
    if response is None:
        return ChatCompletionResult(session_uuid, country, questions)
    if isinstance(response, str):
        return ChatCompletionResult(session_uuid, country, questions, response)
    else:
        answer = response.choices[0].message.content
        return ChatCompletionResult(session_uuid, country, questions, answer)


user_uuid = uuid.UUID("708bab67-64d2-4e7d-94b6-2b6e043d880c")

chat_prompt_message = Message(role=MessageRole.system,
                              content="A chat between a curious human and an artificial intelligence assistant. The "
                                      "assistant gives helpful, detailed, and polite answers to the human's questions.")

title_prompt_message = Message(
    role=MessageRole.system,
    content="You are a helpful assistant. You generate a descriptive, short and meaningful title for the "
            "given conversation.")

followup_messages = [
    Message(role=MessageRole.user, content='What was the name of the city.'),
    Message(role=MessageRole.user, content='What was the name of the country that I asked?'),
    Message(role=MessageRole.user, content=f'Tell me more about the capital of the country?'),
    Message(role=MessageRole.user, content=f'What is the population of the city in your answer?'),
    Message(role=MessageRole.user, content=f'What is the population of the country in the context?'),
    Message(role=MessageRole.user, content=f'What is the area of the country?')
]

countries = ["Germany", "Italy", "Spain", "Netherlands", "Switzerland", "Denmark", "Sweden", "Poland",
             "Czech Republic", "Greece", "Bulgaria", "Romania", "Ukraine", "United Kingdom"]

STOP = ["### Human:"]


# Define the task function
def send_conversation(client: LlamaClient, country: str):
    chat_messages = [chat_prompt_message,
                     Message(role=MessageRole.user, content=f'What is the capital of {country}?')
                     ]

    chat_completion_results = []

    chat_request = ChatCompletionRequest(
        model='gpt-3.5-turbo',
        messages=chat_messages,
        temperature=0.8,
        max_tokens=256,
        stop=STOP,
        user=user_uuid,
        stream=True
    )

    answer, session_uuid = collect_stream_response(client, chat_request)

    chat_completion_result = get_chat_completion_result(country, chat_messages, answer, session_uuid)
    chat_completion_results.append(chat_completion_result)

    output_queue.put(chat_completion_result)

    # send title generation request
    title_messages = [title_prompt_message,
                      Message(role=MessageRole.user,
                              content=f'Question: What is the capital of {country}? '
                                      f'Answer: {chat_completion_result.answer}')
                      ]

    title_request = ChatCompletionRequest(
        model='gpt-3.5-turbo',
        messages=title_messages,
        temperature=0.8,
        max_tokens=256,
        stop=STOP
    )

    title_response: ChatCompletion = client.send_chat_completion_request(title_request)
    title_completion_result = get_chat_completion_result(country, title_messages, title_response, session_uuid)
    chat_completion_results.append(title_completion_result)

    output_queue.put(title_completion_result)

    # send each followup messages for each session
    for message in followup_messages:
        chat_request = ChatCompletionRequest(
            model='gpt-3.5-turbo',
            messages=[message],
            temperature=0.8,
            max_tokens=256,
            stop=STOP,
            user=user_uuid,
            stream=True,
            key_values={"session": session_uuid}
        )
        answer, session_uuid = collect_stream_response(client, chat_request)
        chat_completion_result = get_chat_completion_result(country, [message], answer, session_uuid)
        chat_completion_results.append(chat_completion_result)
        output_queue.put(chat_completion_result)

    return chat_completion_results


def collect_stream_response(client, request):
    answer_text = ""
    session_uuid = None
    for part_response in client.send_chat_completion_request(request):
        response: ChatCompletionChunk = part_response
        if not session_uuid:
            session_uuid = response.key_values["session"]
        if not response.choices[0].finish_reason:
            answer = response.choices[0].delta.content
            answer_text += answer
    return answer_text, session_uuid


def main():
    # Start the output worker thread in background (daemon)
    threading.Thread(target=output_worker, daemon=True).start()

    # Create a ThreadPoolExecutor context
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        # Schedule the tasks for execution
        futures = []

        # send initial messages for each session
        for _ in range(4):
            client = LlamaClient('tcp://localhost:5555', timeout=360000)
            country_index = random.randint(0, len(countries) - 1)
            country = countries[country_index]

            future = executor.submit(send_conversation, client, country)
            futures.append(future)

        client = LlamaClient('tcp://localhost:5555', timeout=360000)
        # Iterate over the Future objects as they complete
        for future in futures:
            results = future.result()
            session_uuid = results[0].session_uuid
            country = results[0].country
            questions = [res.prompt[-1] for res in results]
            answers = [res.answer for res in results if res.answer is not None]
            print(f"=== Session {session_uuid} Country {country} results ===")
            print(f"** Questions: {len(questions)}")
            print(f"## Answers: {len(answers)}")

            session_request = SessionStateRequest(
                session=session_uuid,
                user=user_uuid)
            try:
                response: SessionState = client.send_session_state_request(session_request)
                print(response.to_json_str())
                assert response is not None
                assert isinstance(response, SessionState)
            except TimeoutError as e:
                print(str(e))

    # Stop the output worker thread
    output_queue.put("STOP")


if __name__ == "__main__":
    main()
