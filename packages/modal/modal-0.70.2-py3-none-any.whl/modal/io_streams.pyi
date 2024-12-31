import collections.abc
import modal.client
import modal.stream_type
import typing
import typing_extensions

def _sandbox_logs_iterator(
    sandbox_id: str, file_descriptor: int, last_entry_id: str, client: modal.client._Client
) -> collections.abc.AsyncGenerator[tuple[typing.Optional[bytes], str], None]: ...
def _container_process_logs_iterator(
    process_id: str, file_descriptor: int, client: modal.client._Client
) -> collections.abc.AsyncGenerator[typing.Optional[bytes], None]: ...

T = typing.TypeVar("T")

class _StreamReader(typing.Generic[T]):
    _stream: typing.Optional[collections.abc.AsyncGenerator[typing.Optional[bytes], None]]

    def __init__(
        self,
        file_descriptor: int,
        object_id: str,
        object_type: typing.Literal["sandbox", "container_process"],
        client: modal.client._Client,
        stream_type: modal.stream_type.StreamType = modal.stream_type.StreamType.PIPE,
        text: bool = True,
        by_line: bool = False,
    ) -> None: ...
    @property
    def file_descriptor(self) -> int: ...
    async def read(self) -> T: ...
    async def _consume_container_process_stream(self): ...
    def _stream_container_process(self) -> collections.abc.AsyncGenerator[tuple[typing.Optional[bytes], str], None]: ...
    def _get_logs(
        self, skip_empty_messages: bool = True
    ) -> collections.abc.AsyncGenerator[typing.Optional[bytes], None]: ...
    def _get_logs_by_line(self) -> collections.abc.AsyncGenerator[typing.Optional[bytes], None]: ...
    def __aiter__(self) -> collections.abc.AsyncIterator[T]: ...
    async def __anext__(self) -> T: ...
    async def aclose(self): ...

class _StreamWriter:
    def __init__(
        self, object_id: str, object_type: typing.Literal["sandbox", "container_process"], client: modal.client._Client
    ) -> None: ...
    def _get_next_index(self) -> int: ...
    def write(self, data: typing.Union[bytes, bytearray, memoryview, str]) -> None: ...
    def write_eof(self) -> None: ...
    async def drain(self) -> None: ...

T_INNER = typing.TypeVar("T_INNER", covariant=True)

class StreamReader(typing.Generic[T]):
    _stream: typing.Optional[collections.abc.AsyncGenerator[typing.Optional[bytes], None]]

    def __init__(
        self,
        file_descriptor: int,
        object_id: str,
        object_type: typing.Literal["sandbox", "container_process"],
        client: modal.client.Client,
        stream_type: modal.stream_type.StreamType = modal.stream_type.StreamType.PIPE,
        text: bool = True,
        by_line: bool = False,
    ) -> None: ...
    @property
    def file_descriptor(self) -> int: ...

    class __read_spec(typing_extensions.Protocol[T_INNER]):
        def __call__(self) -> T_INNER: ...
        async def aio(self) -> T_INNER: ...

    read: __read_spec[T]

    class ___consume_container_process_stream_spec(typing_extensions.Protocol):
        def __call__(self): ...
        async def aio(self): ...

    _consume_container_process_stream: ___consume_container_process_stream_spec

    class ___stream_container_process_spec(typing_extensions.Protocol):
        def __call__(self) -> typing.Generator[tuple[typing.Optional[bytes], str], None, None]: ...
        def aio(self) -> collections.abc.AsyncGenerator[tuple[typing.Optional[bytes], str], None]: ...

    _stream_container_process: ___stream_container_process_spec

    class ___get_logs_spec(typing_extensions.Protocol):
        def __call__(
            self, skip_empty_messages: bool = True
        ) -> typing.Generator[typing.Optional[bytes], None, None]: ...
        def aio(
            self, skip_empty_messages: bool = True
        ) -> collections.abc.AsyncGenerator[typing.Optional[bytes], None]: ...

    _get_logs: ___get_logs_spec

    class ___get_logs_by_line_spec(typing_extensions.Protocol):
        def __call__(self) -> typing.Generator[typing.Optional[bytes], None, None]: ...
        def aio(self) -> collections.abc.AsyncGenerator[typing.Optional[bytes], None]: ...

    _get_logs_by_line: ___get_logs_by_line_spec

    def __iter__(self) -> typing.Iterator[T]: ...
    def __aiter__(self) -> collections.abc.AsyncIterator[T]: ...
    def __next__(self) -> T: ...
    async def __anext__(self) -> T: ...
    def close(self): ...
    async def aclose(self): ...

class StreamWriter:
    def __init__(
        self, object_id: str, object_type: typing.Literal["sandbox", "container_process"], client: modal.client.Client
    ) -> None: ...
    def _get_next_index(self) -> int: ...
    def write(self, data: typing.Union[bytes, bytearray, memoryview, str]) -> None: ...
    def write_eof(self) -> None: ...

    class __drain_spec(typing_extensions.Protocol):
        def __call__(self) -> None: ...
        async def aio(self) -> None: ...

    drain: __drain_spec
