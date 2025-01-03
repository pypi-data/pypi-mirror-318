"""
# Generic io helpers

`anystore` is built on top of
[`fsspec`](https://filesystem-spec.readthedocs.io/en/latest/index.html) and
provides an easy wrapper for reading and writing content from and to arbitrary
locations using the `io` command:

Command-line usage:
    ```bash
    anystore io -i ./local/foo.txt -o s3://mybucket/other.txt

    echo "hello" | anystore io -o sftp://user:password@host:/tmp/world.txt

    anystore io -i https://investigativedata.io > index.html
    ```

Python usage:
    ```python
    from anystore import smart_read, smart_write

    data = smart_read("s3://mybucket/data.txt")
    smart_write(".local/data", data)
    ```
"""

import contextlib
import sys
from io import BytesIO, StringIO
from os import PathLike
from pathlib import Path
from typing import (
    IO,
    Any,
    AnyStr,
    BinaryIO,
    Generator,
    Iterable,
    TextIO,
    TypeAlias,
    TypeVar,
)

from fsspec import open
from fsspec.core import OpenFile

from anystore.exceptions import DoesNotExist
from anystore.logging import get_logger
from anystore.util import ensure_uri

log = get_logger(__name__)

DEFAULT_MODE = "rb"
DEFAULT_WRITE_MODE = "wb"

Uri: TypeAlias = PathLike | Path | BinaryIO | TextIO | str
GenericIO: TypeAlias = OpenFile | TextIO | BinaryIO
T = TypeVar("T")


def _get_sysio(mode: str | None = DEFAULT_MODE) -> TextIO | BinaryIO:
    if mode and "r" in mode:
        io = sys.stdin
    else:
        io = sys.stdout
    if mode and "b" in mode:
        return io.buffer
    return io


class SmartHandler:
    def __init__(
        self,
        uri: Uri,
        **kwargs: Any,
    ) -> None:
        self.uri = uri
        self.is_buffer = self.uri == "-"
        kwargs["mode"] = kwargs.get("mode", DEFAULT_MODE)
        self.sys_io = _get_sysio(kwargs["mode"])
        self.kwargs = kwargs
        self.handler: IO | None = None

    def open(self) -> IO[AnyStr]:
        try:
            if self.is_buffer:
                return self.sys_io
            elif isinstance(self.uri, (BytesIO, StringIO)):
                return self.uri
            else:
                self.uri = ensure_uri(self.uri)
                handler: OpenFile = open(self.uri, **self.kwargs)
                self.handler = handler.open()
                return self.handler
        except FileNotFoundError as e:
            raise DoesNotExist from e

    def close(self):
        if not self.is_buffer and self.handler is not None:
            self.handler.close()

    def __enter__(self):
        return self.open()

    def __exit__(self, *args, **kwargs) -> None:
        self.close()


@contextlib.contextmanager
def smart_open(
    uri: Uri,
    mode: str | None = DEFAULT_MODE,
    **kwargs: Any,
) -> Generator[IO, None, None]:
    """
    IO context similar to pythons built-in `open()`.

    Example:
        ```python
        from anystore import smart_open

        with smart_open("s3://mybucket/foo.csv") as fh:
            return fh.read()
        ```

    Args:
        uri: string or path-like key uri to open, e.g. `./local/data.txt` or `s3://mybucket/foo`
        mode: open mode, default `rb` for byte reading.
        **kwargs: pass through storage-specific options

    Yields:
        A generic file-handler like context object
    """
    handler = SmartHandler(uri, mode=mode, **kwargs)
    try:
        yield handler.open()
    except FileNotFoundError as e:
        raise DoesNotExist from e
    finally:
        handler.close()


def smart_stream(
    uri: Uri, mode: str | None = DEFAULT_MODE, **kwargs: Any
) -> Generator[AnyStr, None, None]:
    """
    Stream content line by line.

    Example:
        ```python
        import orjson
        from anystore import smart_stream

        while data := smart_stream("s3://mybucket/data.json"):
            yield orjson.loads(data)
        ```

    Args:
        uri: string or path-like key uri to open, e.g. `./local/data.txt` or `s3://mybucket/foo`
        mode: open mode, default `rb` for byte reading.
        **kwargs: pass through storage-specific options

    Yields:
        A generator of `str` or `byte` content, depending on `mode`
    """
    with smart_open(uri, mode, **kwargs) as fh:
        while line := fh.readline():
            yield line


def smart_read(uri: Uri, mode: str | None = DEFAULT_MODE, **kwargs: Any) -> AnyStr:
    """
    Return content for a given file-like key directly.

    Args:
        uri: string or path-like key uri to open, e.g. `./local/data.txt` or `s3://mybucket/foo`
        mode: open mode, default `rb` for byte reading.
        **kwargs: pass through storage-specific options

    Returns:
        `str` or `byte` content, depending on `mode`
    """
    with smart_open(uri, mode, **kwargs) as fh:
        return fh.read()


def smart_write(
    uri: Uri, content: bytes | str, mode: str | None = DEFAULT_WRITE_MODE, **kwargs: Any
) -> None:
    """
    Write content to a given file-like key directly.

    Args:
        uri: string or path-like key uri to open, e.g. `./local/data.txt` or `s3://mybucket/foo`
        content: `str` or `bytes` content to write.
        mode: open mode, default `wb` for byte writing.
        **kwargs: pass through storage-specific options
    """
    if uri == "-":
        if isinstance(content, str):
            content = content.encode()
    with smart_open(uri, mode, **kwargs) as fh:
        fh.write(content)


def logged_io_items(
    items: Iterable[T], uri: Uri, action: str, chunk_size: int | None = 10_000
) -> Generator[T, None, None]:
    """
    Log process of iterating items for io operations.

    Example:
        ```python
        from anystore.io import logged_io_items

        items = [...]
        for item in logged_io_items(items, "local", "Read"):
            yield item
        ```

    Args:
        items: Sequence of any items
        uri: string or path-like key uri to open, e.g. `./local/data.txt` or
            `s3://mybucket/foo` (for logging purpose)
        action: Action name to log
        chunk_size: Log on every chunk_size

    Yields:
        The input items
    """
    chunk_size = chunk_size or 10_000
    ix = 0
    model = "Item"
    for ix, item in enumerate(items, 1):
        if ix == 1:
            model = item.__class__.__name__.title()
        if ix % chunk_size == 0:
            model = item.__class__.__name__.title()
            log.info(f"{action} `{model}` {ix} ...", uri=ensure_uri(uri))
        yield item
    if ix:
        log.info(f"{action} {ix} `{model}s`: Done.", uri=ensure_uri(uri))
