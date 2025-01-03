from typing import Optional, Iterable, Union
import zmq

from llama_server_client.base_client import BaseLlamaClient
from llama_server_client.schema import HealthCheck
from llama_server_client.schema.base import T
from llama_server_client.schema.completion import ChatCompletionRequest, ChatCompletion, ChatCompletionChunk, \
    CompletionRequest
from llama_server_client.schema.zmq_message_header import (
    ZmqMessageType, create_message_header, ZmqMessageHeader, ZmqMessageStatus
)
from llama_server_client.schema.session_state import SessionStateRequest, SessionState
from llama_server_client.error import LlamaClientError
from llama_server_client.schema.zmq_response import ZmqResponse


class LlamaClient(BaseLlamaClient):
    """
    LlamaClient is a synchronous client class for communication with a server using ZeroMQ.
    It handles socket creation, sending requests, and receiving responses with an option for timeouts.
    """

    def _create_context(self) -> zmq.Context:
        """Create a new ZeroMQ context."""
        return zmq.Context()

    def _create_socket(self) -> zmq.Socket:
        """Create a new ZeroMQ DEALER socket."""
        return self.context.socket(zmq.DEALER)

    def _send_request(
        self,
        zmq_message_type: ZmqMessageType,
        request: Optional[T] = None,
        raw_response: bool = False
    ) -> Union[T, Iterable[T], ZmqResponse]:
        """
        Synchronously sends a request to the server, and waits for a response, handling timeouts.

        :param zmq_message_type: The type of the ZeroMQ message to be sent.
        :param request: The request object to be sent, if applicable.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: The unpacked response if successful, raw response if specified, or raises a timeout exception.
        """
        message_header: ZmqMessageHeader = create_message_header(zmq_message_type)
        message_parts = [message_header.msgpack_pack()]
        if request:
            message_parts.append(request.msgpack_pack())

        self.socket.send_multipart(message_parts)

        try:
            resp_messages = self.socket.recv_multipart()
            if len(resp_messages) > 2:
                raise ValueError("Invalid response length")

            response_header = ZmqMessageHeader.msgpack_unpack(resp_messages[0])
            if response_header.status == ZmqMessageStatus.ERROR:
                raise LlamaClientError(response_header)

            response_body_class = zmq_message_type.get_associated_class

            if isinstance(request, (ChatCompletionRequest, CompletionRequest)) and request.stream:
                return self._stream_responses(resp_messages, raw_response)
            else:
                if raw_response:
                    return ZmqResponse(
                        header=response_header,
                        body=response_body_class.msgpack_unpack(resp_messages[1])
                    )
                return response_body_class.msgpack_unpack(resp_messages[1])

        except zmq.Again:
            self._initialize_context_and_socket()
            raise TimeoutError(f"Request timed out after {self.timeout} milliseconds")

    def _stream_responses(
        self,
        initial_resp_messages,
        raw_response: bool
    ) -> Iterable[Union[T, ZmqResponse]]:
        """
        Handles streaming of responses.

        :param initial_resp_messages: The initial response messages received.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: An iterable yielding responses.
        """
        try:
            if raw_response:
                yield ZmqResponse(
                    header=ZmqMessageHeader.msgpack_unpack(initial_resp_messages[0]),
                    body=ChatCompletionChunk.msgpack_unpack(initial_resp_messages[1])
                )
            else:
                yield ChatCompletionChunk.msgpack_unpack(initial_resp_messages[1])

            while True:
                resp_messages = self.socket.recv_multipart()
                response_header = ZmqMessageHeader.msgpack_unpack(resp_messages[0])
                if response_header.status == ZmqMessageStatus.ERROR:
                    raise LlamaClientError(response_header)

                if raw_response:
                    yield ZmqResponse(
                        header=ZmqMessageHeader.msgpack_unpack(resp_messages[0]),
                        body=ChatCompletionChunk.msgpack_unpack(resp_messages[1])
                    )
                else:
                    yield ChatCompletionChunk.msgpack_unpack(resp_messages[1])

                if not response_header.has_more_message:
                    break

        except zmq.Again:
            self._initialize_context_and_socket()
            raise TimeoutError(f"Request timed out after {self.timeout} milliseconds")

    def _handle_chat_completion_response(
        self, request: ChatCompletionRequest, raw_response: bool = False
    ) -> Union[ChatCompletion, ZmqResponse]:
        """
        Handles ChatCompletion responses.

        :param request: The ChatCompletionRequest to send.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: A ChatCompletion response or raw response if specified.
        """
        return self._send_request(ZmqMessageType.CHAT_COMPLETION, request, raw_response)

    def _handle_chat_completion_chunk_response(
        self, request: ChatCompletionRequest, raw_response: bool = False
    ) -> T | Iterable[T] | ZmqResponse:
        """
        Handles ChatCompletionChunk responses.

        :param request: The ChatCompletionRequest to send.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: An Iterable yielding ChatCompletionChunk responses or raw response if specified.
        """
        return self._send_request(ZmqMessageType.CHAT_COMPLETION, request, raw_response)

    def send_chat_completion_request(
        self, request: ChatCompletionRequest, raw_response: bool = False
    ) -> Union[Iterable[ChatCompletionChunk], ChatCompletion, Iterable[ZmqResponse], ZmqResponse]:
        """
        Synchronously sends a ChatCompletionRequest to the server and waits for a ChatCompletion or
        ChatCompletionChunk response.

        :param request: The ChatCompletionRequest to send.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: An Iterable yielding ChatCompletionChunk responses if request.stream is True,
                 a single ChatCompletion response if request.stream is False,
                 or a raw response if specified.
        """
        if request.stream:
            return self._handle_chat_completion_chunk_response(request, raw_response)
        else:
            return self._handle_chat_completion_response(request, raw_response)

    def _handle_completion_response(
            self, request: CompletionRequest, raw_response: bool = False
    ) -> Union[ChatCompletion, ZmqResponse]:
        """
        Handles Completion responses.

        :param request: The CompletionRequest to send.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: A ChatCompletion response or raw response if specified.
        """
        return self._send_request(ZmqMessageType.COMPLETION, request, raw_response)

    def _handle_completion_chunk_response(
            self, request: CompletionRequest, raw_response: bool = False
    ) -> T | Iterable[T] | ZmqResponse:
        """
        Handles CompletionChunk responses.

        :param request: The CompletionRequest to send.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: An Iterable yielding ChatCompletionChunk responses or raw response if specified.
        """
        return self._send_request(ZmqMessageType.COMPLETION, request, raw_response)

    def send_completion_request(
            self, request: CompletionRequest, raw_response: bool = False
    ) -> Union[Iterable[ChatCompletionChunk], ChatCompletion, Iterable[ZmqResponse], ZmqResponse]:
        """
        Synchronously sends a CompletionRequest to the server and waits for a ChatCompletion or
        ChatCompletionChunk response. This legacy request is used for FIM

        :param request: The CompletionRequest to send.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: An Iterable yielding ChatCompletionChunk responses if request.stream is True,
                 a single ChatCompletion response if request.stream is False,
                 or a raw response if specified.
        """
        if request.stream:
            return self._handle_completion_chunk_response(request, raw_response)
        else:
            return self._handle_completion_response(request, raw_response)

    def send_session_state_request(
        self,
        request: SessionStateRequest,
        raw_response: bool = False
    ) -> Union[SessionState, ZmqResponse]:
        """
        Synchronously sends a SessionStateRequest to the server and waits for a SessionState response.

        :param request: The SessionStateRequest to send.
        :param raw_response: Flag to determine if raw response should be returned.
        :return: A SessionState response, raw response if specified, or None if timed out.
        """
        return self._send_request(ZmqMessageType.SESSION_STATE, request, raw_response)

    def send_health_check_request(
        self,
        raw_response: bool = False
    ) -> Union[HealthCheck, ZmqResponse]:
        """
        Synchronously sends a HealthCheck request to the server and waits for a HealthCheck response.

        :param raw_response: Flag to determine if raw response should be returned.
        :return: A HealthCheck response, raw response if specified, or None if timed out.
        """
        return self._send_request(ZmqMessageType.HEALTH_CHECK, raw_response=raw_response)
