# BSD 3-Clause License
#
# Copyright (c) 2022-Present, nxtlo
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Basic implementation of a cheap container for dealing with byte buffers."""

from __future__ import annotations

__all__ = ("Bytes", "Rawish", "Buffer")

import array
import ctypes as _ctypes
import io as _io
import sys as _sys
import typing
from collections import abc as collections

from sain import convert
from sain import iter as _iter
from sain import option as _option
from sain import result as _result

from . import vec as _vec

if typing.TYPE_CHECKING:
    import inspect

    from sain import Option
    from sain import Result

Rawish: typing.TypeAlias = _io.StringIO | _io.BytesIO | _io.BufferedReader | memoryview
"""A type hint for some raw data type.

This can be any of:
* `io.StringIO`
* `io.BytesIO`
* `io.BufferedReader`
* `memoryview`
"""

Buffer: typing.TypeAlias = bytes | bytearray | collections.Iterable[int]
"""A type hint for some bytes data type.

This can be any of:
* `bytes`
* `Bytes`
* `bytearray`
* `Iterable[int]`
"""

ENCODING = "utf-8"


def unwrap_bytes(data: Rawish) -> bytes:
    if isinstance(data, _io.StringIO):
        buf = bytes(data.read(), encoding=ENCODING)
    elif isinstance(data, memoryview):
        buf = data.tobytes()
    else:
        # BufferedReader | BytesIO
        buf = data.read()
    return buf


@typing.final
class Bytes(convert.ToString):
    """Provides abstractions for working with UTF-8 compatible bytes.

    It is an efficient container for storing and operating with bytes.
    It behaves very much like `array.array[int]` as well has the same layout.

    A `Bytes` objects are usually used within networking applications, but can also be used
    elsewhere as well.

    ## Construction
    `Bytes` object accept multiple rawish data types, See `Rawish` for all supported types.

    * `Bytes()`: Initialize an empty `Bytes` object
    * `from_str`: Create `Bytes` from `str`
    * `from_bytes`: Create `Bytes` from a `Buffer` type
    * `from_raw`: Create `Bytes` from a `Rawish` type
    * `from_static`: Create `Bytes` that points to an `array.array[int]` without copying it
    * `Bytes.zeroed(count)`: Create `Bytes` filled with `zeroes * count`.

    Example
    -------
    ```py
    from sain import Bytes

    buf = Bytes()
    buffer.put_bytes(b"Hello")
    print(buffer) # [72, 101, 108, 108, 111]

    buf.put(32) # space
    assert buffer.to_bytes() == b"Hello "
    ```
    """

    __slots__ = ("_buf",)

    def __init__(self) -> None:
        """Creates a new empty `Bytes`.

        This won't allocate the array and the returned `Bytes` will be empty.
        """
        self._buf: array.array[int] | None = None

    # construction

    @classmethod
    def from_str(cls, s: str) -> Bytes:
        """Create a new `Bytes` from a utf-8 string.

        Example
        -------
        ```py
        buffer = Bytes.from_str("💀")
        assert buffer.as_ref() == (240, 159, 146, 128)
        ```
        """
        b = cls()
        b._buf = array.array("B", s.encode(ENCODING))
        return b

    @classmethod
    def from_static(cls, arr: array.array[int]) -> Bytes:
        """Create a new `Bytes` from an array.

        The returned `Bytes` will directly point to `arr` without copying.

        Example
        -------
        ```py
        arr = array.array("B")
        buffer = Bytes.from_static(arr)
        ```
        """
        b = cls()
        b._buf = arr
        return b

    @classmethod
    def from_bytes(cls, buf: Buffer) -> Bytes:
        """Create a new `Bytes` from an initial bytes.

        Example
        -------
        ```py
        buffer = Bytes.from_bytes(b"SIGNATURE")
        ```
        """
        b = cls()
        b._buf = array.array("B", buf)
        return b

    @classmethod
    def from_raw(cls, raw: Rawish) -> Bytes:
        """Initialize a new `Bytes` in-place from a valid raw data type.

        Example
        -------
        ```py
        with open('file.txt', 'rb') as file:
            buff = Bytes.from_raw(file)

        # in memory bytes io
        bytes_io = io.BytesIO(b"data")
        buffer1 = Bytes.from_raw(bytes_io)
        # in memory string io
        string_io = io.StringIO("data")
        buffer2 = Bytes.from_raw(string_io)
        ```
        """
        c = cls()
        c._buf = array.array("B", unwrap_bytes(raw))
        return c

    @classmethod
    def zeroed(cls, count: int) -> Bytes:
        """Initialize a new `Bytes` filled with zeros * `count`.

        Example
        -------
        ```py
        ALLOC_SIZE = 1024 * 2
        buffer = Bytes.zeros(ALLOC_SIZE)
        assert buffer.len() == ALLOC_SIZE
        ```
        """
        c = cls()
        c._buf = array.array("B", [0] * count)
        return c

    # buffer evolution

    def to_string(self) -> str:
        """Convert the bytes to a string.

        Same as `Bytes.to_str`
        """
        return self.to_str()

    def try_to_str(self) -> Result[str, bytes]:
        """A safe method to convert `self` into a string.

        This may fail if the `self` contains invalid bytes. strings
        needs to be valid utf-8.

        Example
        -------
        ```py
        buf = Bytes()
        sparkles_heart = [240, 159, 146, 150]
        buf.put_bytes(sparkles_heart)

        assert buf.try_to_str().unwrap() == "💖"
        ```

        Incorrect bytes
        ---------------
        ```py
        invalid_bytes = Bytes.from_bytes([0, 159, 146, 150])
        invalid_bytes.try_to_str().is_err()
        ```

        Returns
        -------
        `Result[str, bytes]`
            If successful, returns the decoded string, otherwise the original bytes that failed
            to get decoded.
        """
        try:
            return _result.Ok(self.to_bytes().decode(ENCODING))
        except UnicodeDecodeError as e:
            return _result.Err(e.object)

    def to_str(self) -> str:
        """Convert `self` to a utf-8 string.

        During the conversion process, any invalid bytes will get converted to
        [REPLACEMENT_CHARACTER](https://en.wikipedia.org/wiki/Specials_(Unicode_block))
        which looks like this `�`, so be carful on what you're trying to convert.

        Use `.try_to_str` try attempt the conversion incase of failure.

        Example
        -------
        ```py
        buf = Bytes()
        sparkles_heart = [240, 159, 146, 150]
        buf.put_bytes(sparkles_heart)

        assert buf.to_str() == "💖"
        ```

        Incorrect bytes
        ---------------
        ```py
        invalid_bytes = Bytes.from_bytes(b"Hello \xf0\x90\x80World")
        assert invalid_bytes.to_str() == "Hello �World"
        ```
        """
        if not self._buf:
            return ""

        return self._buf.tobytes().decode(ENCODING, errors="replace")

    def to_bytes(self) -> bytes:
        """Convert `self` into `bytes`, copying the underlying array into a new buffer.

        Example
        -------
        ```py
        buf = Bytes.from_str("Hello")
        assert buf.to_bytes() == b'Hello'
        ```
        """
        if not self._buf:
            return b""

        return self._buf.tobytes()

    def to_vec(self) -> _vec.Vec[int]:
        """Copies `self` into a new `Vec`.

        Example
        -------
        ```py
        buffer = Bytes.from_str([1, 2, 3, 4])
        x = buffer.to_vec()
        assert x == [1, 2, 3, 4]
        """
        return _vec.Vec(self)

    def leak(self) -> Option[array.array[int]]:
        """Consumes and leaks the `Bytes`, returning the contents as an `array[int]`
        or `None` if the buffer is not initialized.

        `self` will deallocate the underlying array, therefore it becomes unusable.

        Safety
        ------
        It is unsafe to access the leaked array from `self` after calling this function.

        Example
        -------
        ```py
        bytes = Bytes.from_str("chunks of data")
        consumed = bytes.leak().unwrap()
        # This is undefined behavior!!!
        bytes.put(0)
        # access the array directly instead.
        consumed.tobytes() == b"chunks of data"
        ```
        """
        if self._buf is None:
            return _option.NOTHING  # pyright: ignore

        arr = self._buf
        # We don't need to reference this anymore since the caller will own the array.
        del self._buf
        return _option.Some(arr)

    def as_ptr(self) -> memoryview[int]:
        """Returns a read-only pointer to the buffer data.

        Example
        -------
        ```py
        buffer = Bytes.from_bytes(b"data")
        ptr = buffer.as_ptr()
        ptr[0] = 1 # TypeError: cannot modify read-only memory
        ```
        """
        return self.__buffer__(0x100).toreadonly()

    def as_mut_ptr(self) -> memoryview[int]:
        """Returns a mutable pointer to the buffer data.

        Example
        -------
        ```py
        buffer = Bytes.from_str("ouv")
        ptr = buffer.as_mut_ptr()
        ptr[0] = ord(b'L')
        assert buffer.to_bytes() == b"Luv"
        ```
        """
        return self.__buffer__(0x100)

    def as_ref(self) -> collections.Sequence[int]:
        """Get an immutable reference to the underlying sequence, without copying.

        A `ReferenceError` is raised if the underlying sequence is not initialized.

        Example
        -------
        ```py
        async def send_multipart(buf: Sequence[int]) -> None:
            ...

        buffer = Bytes.from_bytes([0, 0, 0, 0])
        await send_multipart(buffer.as_ref()) # no copy.
        ```
        """
        if self._buf is not None:
            return self._buf.__buffer__(0x100).toreadonly()

        raise ReferenceError("`self` must be initialized first.") from None

    def as_mut(self) -> collections.MutableSequence[int]:
        """Get a mutable reference to the underlying sequence, without copying.

        A `ReferenceError` is raised if the underlying sequence is not initialized.

        Example
        -------
        ```py
        buff = Bytes.from_str("Hello")
        ref = buff.as_mut()
        ref.append(32)
        del ref
        assert buff.to_str() == "Hello "
        ```
        """
        if self._buf is not None:
            return self._buf

        raise ReferenceError("`self` must be initialized first.") from None

    def raw_parts(
        self,
    ) -> tuple[typing.Annotated[int, "address"], typing.Annotated[int, "len"]]:
        """Return `self` as tuple containing the memory address to the buffer and how many bytes it currently contains"""
        if not self._buf:
            return (0x0, 0)

        return self._buf.buffer_info()

    # default methods.

    def extend(self, src: Buffer) -> None:
        """Extend `self` from a buffer.

        Example
        -------
        ```py
        buf = Bytes()
        buf.extend([1, 2, 3])
        assert buf == [1, 2, 3]
        ```

        Parameters
        ----------
        src : `Buffer`
            Can be one of `Bytes`, `bytes`, `bytearray` or `Sequence[int]`

        Raises
        ------
        `OverflowError`
            If `src` not in range of `0..255`
        """
        if self._buf is None:
            # If it was `None`, we initialize it with a source instead of extending.
            self._buf = array.array("B", src)
        else:
            self._buf.extend(src)

    def put(self, src: int) -> None:
        """Append a byte at the end of the array.

        unlike `.put_bytes`, this method appends instead of extending the array
        which is faster if you're putting a single byte in a single call.

        if `self` hasn't been initialized, the array will allocate along with the byte.

        Example
        -------
        ```py
        buf = Bytes()
        buf.put(32) # append a space to the end of the buffer
        assert buf.to_bytes() == b' '
        ```

        Parameters
        ----------
        src : `int`
            An unsigned integer, also known as `u8` to put.

        Raises
        ------
        `OverflowError`
            If `src` not in range of `0..255`
        """
        if self._buf is None:
            # If it was `None`, we initialize it with a source instead of appending.
            self._buf = array.array("B", [src])
        else:
            self._buf.append(src)

    def put_char(self, char: str) -> None:
        """Append a single character to the buffer.

        This is the same as `self.put(ord(char))`.

        Example
        -------
        ```py
        buf = Bytes()
        buf.put_char('a')
        assert buf.to_str() == "a"
        ```

        Parameters
        ----------
        char : `str`
            The character to put.
        """
        assert (ln := len(char)) == 1, f"Expected a single character, got {ln}"
        self.put(ord(char))

    def put_raw(self, src: Rawish) -> None:
        """Extend `self` from a raw data type source.

        Example
        -------
        ```py
        buffer = Bytes()
        # A file descriptor's contents
        with open('file.txt', 'rb') as file:
            buffer.put_raw(file)

        # bytes io
        buffer.put(io.BytesIO(b"data"))
        # string io
        buffer.put(io.StringIO("data"))
        ```

        Parameters
        ----------
        src : `Rawish`
            A valid raw data type. See `Rawish` for more details.

        Raises
        ------
        `OverflowError`
            If `src` not in range of `0..255`
        """
        if self._buf is None:
            # If it was `None`, we initialize it with a source instead of extending.
            self._buf = array.array("B", unwrap_bytes(src))
        else:
            self._buf.extend(unwrap_bytes(src))

    def put_bytes(self, src: Buffer) -> None:
        """Put `bytes` into `self`.

        Example
        -------
        ```py
        buf = Bytes.from_bytes(b"hello")
        buf.put_bytes([32, 119, 111, 114, 108, 100])
        assert buf.to_str() == "hello world"
        ```

        Parameters
        ----------
        src : `Buffer`
            Can be one of `Bytes`, `bytes`, `bytearray` or `Sequence[int]`

        Raises
        ------
        `OverflowError`
            If `src` not in range of `0..255`
        """
        if self._buf is None:
            # If it was `None`, we initialize it with a source instead of extending.
            self._buf = array.array("B", src)
        else:
            self._buf.extend(src)

    def put_str(self, s: str) -> None:
        """Put a `utf-8` encoded bytes from a string.

        Example
        -------
        ```py
        buffer = Bytes()
        buffer.put_str("hello")

        assert buffer.to_str() == "hello"
        ```

        Parameters
        ----------
        src: `str`
            The string
        """
        self.put_bytes(s.encode(ENCODING))

    def fill(self, value: int) -> None:
        """Fill this `self` with the given byte.

        Nothing happens if the buffer is empty or unallocated.

        Example
        -------
        ```py
        a = Bytes.from_bytes([0, 1, 2, 3])
        a.fill(0)
        assert a == [0, 0, 0, 0]
        ```
        """
        if not self._buf:
            return

        self._buf.__buffer__(0x100)[:] = bytearray([value] * self.len())

    def swap(self, a: int, b: int):
        """Swap two bytes in the buffer.

        if `a` equals to `b` then it's guaranteed that elements won't change value.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([1, 2, 3, 4])
        buf.swap(0, 3)
        assert buf == [4, 2, 3, 1]
        ```

        Raises
        ------
        IndexError
            If the positions of `a` or `b` are out of index.
        """
        if self[a] == self[b]:
            return

        self[a], self[b] = self[b], self[a]

    def swap_unchecked(self, a: int, b: int):
        """Swap two bytes in the buffer. without checking if `a` == `b`.

        If you care about `a` and `b` equality, see `Bytes.swap`.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([1, 2, 3, 1])
        buf.swap_unchecked(0, 3)
        assert buf == [1, 2, 3, 1]
        ```

        Raises
        ------
        IndexError
            If the positions of `a` or `b` are out of index.
        """
        self[a], self[b] = self[b], self[a]

    def len(self) -> int:
        """Return the number of bytes in this buffer.

        Example
        -------
        ```py
        buf = Bytes()
        buf.put((1, 2, 3))
        assert buf.len() == 3
        ```
        """
        return self.__len__()

    def size(self) -> int:
        """The length in bytes of one array item in the internal representation.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([240, 159, 146, 150])
        assert buf.size() == 1
        ```
        """
        if not self._buf:
            return 0
        return self._buf.itemsize

    def iter(self) -> _iter.Iterator[int]:
        """Returns an iterator over the bytes of `self`.

        This iterator yields all `int`s from start to end.

        Example
        -------
        ```py
        buf = Bytes.from_bytes((1, 2, 3))
        iterator = buf.iter()

        # map each byte to a character
        for element in iterator.map(chr):
            print(element)
        # ☺
        # ☻
        # ♥
        ```
        """
        return _iter.Iter(self)

    def chars(self) -> _iter.Iterator[_ctypes.c_char]:
        """Returns an iterator over the characters of `Bytes`.

        This iterator yields all `int`s from start to end as a `ctypes.c_char`.

        Example
        -------
        ```py
        b = Bytes.from_str("Hello")
        for char in b.chars():
            print(char)

        # c_char(b'H')
        # c_char(b'e')
        # c_char(b'l')
        # c_char(b'l')
        # c_char(b'o')
        ```
        """
        # The built-in map is actually faster than our own pure python adapter impl.
        return _iter.Iter(map(_ctypes.c_char, self))

    def is_empty(self) -> bool:
        """Check whether `self` contains any bytes or not.

        Example
        -------
        ```py
        buffer = Bytes()
        assert buffer.is_empty()
        ```
        """
        return not self._buf

    def truncate(self, size: int) -> None:
        """Shortens the bytes, keeping the first `size` elements and dropping the rest.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([0, 0, 0, 0])
        buf.truncate(1)
        assert buf.len() == 1
        ```
        """
        if not self._buf:
            return

        del self._buf[size:]

    def split_off(self, at: int) -> Bytes:
        """Split the bytes off at the specified position, returning a new
        `Bytes` at the range of `[at : len]`, leaving `self` at `[at : bytes_len]`.

        if this bytes is empty, `self` is returned unchanged.

        Example
        -------
        ```py
        origin = Bytes.from_bytes((1, 2, 3, 4))
        split = origin.split_off(2)

        print(origin, split)  # [1, 2], [3, 4]
        ```

        Raises
        ------
        `RuntimeError`
            This method will raise if `at` > `len(self)`
        """
        len_ = self.len()
        if at > len_:
            raise RuntimeError(
                f"Index `at` ({at}) should be <= than len of `self` ({len_}) "
            ) from None

        # Either the list is empty or uninit.
        if not self._buf:
            return self

        split = self[at:len_]  # split the items into a new buffer.
        del self._buf[at:len_]  # remove the items from the original list.
        return split

    def split_first(self) -> _option.Option[tuple[int, collections.Sequence[int]]]:
        """Split the first and rest elements of the bytes, If empty, `None` is returned.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([1, 2, 3])
        split = buf.split_first()
        assert split == Some((1, [2, 3]))

        buf: Bytes = Bytes()
        split = buf.split_first()
        assert split.is_none()
        ```
        """
        if not self._buf:
            return _option.NOTHING  # pyright: ignore

        # optimized to only one element in the buffer.
        if self.len() == 1:
            return _option.Some((self[0], ()))

        first, *rest = self._buf
        return _option.Some((first, rest))

    def split_last(self) -> _option.Option[tuple[int, collections.Sequence[int]]]:
        """Split the last and rest elements of the bytes, If empty, `None` is returned.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([1, 2, 3])
        last, rest = buf.split_last().unwrap()
        assert (last, rest) == [3, [1, 2]]
        ```
        """
        if not self._buf:
            return _option.NOTHING  # pyright: ignore

        len_ = self.len()
        # optimized to only one element in the buffer.
        if len_ == 1:
            return _option.Some((self[0], ()))

        last = self[-1]
        return _option.Some((last, [*self[:-1]]))

    def split_at(self, mid: int) -> tuple[Bytes, Bytes]:
        """Divide `self` into two at an index.

        The first will contain all bytes from `[0:mid]` excluding `mid` it self.
        and the second will contain the remaining bytes.

        if `mid` > `self.len()`, Then all bytes will be moved to the left,
        returning an empty bytes in right.

        Example
        -------
        ```py
        buffer = Bytes.from_bytes((1, 2, 3, 4))
        left, right = buffer.split_at(0)
        assert left == [] and right == [1, 2, 3, 4]

        left, right = buffer.split_at(2)
        assert left == [1, 2] and right == [2, 3]
        ```

        The is roughly the implementation
        ```py
        self[0:mid], self[mid:]
        ```
        """
        return self[0:mid], self[mid:]

    # layout methods.

    def copy(self) -> Bytes:
        """Create a copy of the bytes.

        Example
        -------
        ```py
        original = Bytes.from_bytes([255, 255, 255, 0])
        copy = original.copy()
        ```
        """
        if not self._buf:
            return Bytes()

        return self.from_static(self._buf[:])

    def clear(self) -> None:
        """Clear the buffer.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([255])
        buf.clear()

        assert buf.is_empty()
        ```
        """
        if not self._buf:
            return

        self._buf.clear()

    def index(self, v: int, start: int = 0, stop: int = _sys.maxsize) -> int:
        """Return the smallest `i` such that `i` is the index of the
        first occurrence of `v` in the buffer.

        The optional arguments start and stop can be specified to search for x within a
        subsection of the array. Raise ValueError if x is not found
        """
        if not self._buf:
            raise ValueError from None

        return self._buf.index(v, start, stop)

    def count(self, x: int) -> int:
        """Return the number of occurrences of `x` in the buffer.

        Example
        --------
        ```py
        buf = Bytes([32, 32, 31])
        assert buf.count(32) == 2
        ```
        """
        if self._buf is None:
            return 0

        return self._buf.count(x)

    def insert(self, index: int, value: int) -> None:
        """Insert a new item with `value` in the buffer before position `index`.

        Negative values are treated as being relative to the end of the buffer.
        """
        if self._buf is None:
            return

        self._buf.insert(index, value)

    def pop(self, i: int = -1) -> Option[int]:
        """Removes the last element from the buffer and returns it, `Some(None)` if it is empty.

        Example
        -------
        ```py
        buf = Bytes((21, 32, 44))
        assert buf.pop() == Some(44)
        ```
        """
        if not self._buf:
            return _option.NOTHING  # pyright: ignore

        return _option.Some(self._buf.pop(i))

    def swap_remove(self, byte: int) -> int:
        """Remove the first appearance of `item` from this buffer and return it.

        Raises
        ------
        * `ValueError`: if `item` is not in this buffer.
        * `MemoryError`: if this buffer hasn't allocated, Aka nothing has been pushed to it.

        Example
        -------
        ```py
        buf = Bytes.from_bytes([1, 2, 3, 4])
        assert 1 == buf.swap_remove(1)
        assert buf == [2, 3, 4]
        ```
        """
        if self._buf is None:
            raise MemoryError("`self` is unallocated.") from None

        return self._buf.pop(self.index(byte))

    def remove(self, i: int) -> None:
        """Remove the first appearance of `i` from `self`.

        Example
        ```py
        buf = Bytes.from_bytes([1, 1, 2, 3, 4])
        buf.remove(1)
        print(buf) # [1, 2, 3, 4]
        ```
        """
        if not self._buf:
            return

        self._buf.remove(i)

    # special methods

    def __iter__(self) -> collections.Iterator[int]:
        if self._buf:
            return self._buf.__iter__()

        return ().__iter__()

    def __len__(self) -> int:
        return len(self._buf) if self._buf else 0

    def __repr__(self) -> str:
        return "[]" if not self._buf else "[" + ", ".join(map(str, self)) + "]"

    __str__ = __repr__

    def __bytes__(self) -> bytes:
        return self.to_bytes()

    def __buffer__(self, flag: int | inspect.BufferFlags) -> memoryview[int]:
        if not self._buf:
            raise BufferError("Cannot work with uninitialized bytes.")

        return self._buf.__buffer__(flag)

    def __contains__(self, byte: int) -> bool:
        return byte in self._buf if self._buf else False

    def __eq__(self, other: object, /) -> bool:
        if not self._buf:
            return False

        if isinstance(other, list):
            # this conversion may or may not cost,
            # users usually should not compare bytes this way anyway.
            return self._buf.tolist() == other

        return self._buf.__eq__(other)

    def __ne__(self, other: object, /) -> bool:
        return not self.__eq__(other)

    def __le__(self, other: object) -> bool:
        if not self._buf:
            return False

        if not isinstance(other, Bytes):
            return NotImplemented

        if not other._buf:
            return False

        return self._buf <= other._buf

    def __ge__(self, other: object) -> bool:
        if not self._buf:
            return False

        if not isinstance(other, Bytes):
            return NotImplemented

        if not other._buf:
            return False

        return self._buf >= other._buf

    def __lt__(self, other: object) -> bool:
        if not self._buf:
            return False

        if not isinstance(other, Bytes):
            return NotImplemented

        if not other._buf:
            return False

        return self._buf < other._buf

    def __gt__(self, other: object) -> bool:
        if not self._buf:
            return False

        if not isinstance(other, Bytes):
            return NotImplemented

        if not other._buf:
            return False

        return self._buf > other._buf

    def __setitem__(self, index: int, value: int):
        if not self._buf:
            raise IndexError from None

        self._buf[index] = value

    @typing.overload
    def __getitem__(self, index: slice) -> Bytes: ...

    @typing.overload
    def __getitem__(self, index: int) -> int: ...

    def __getitem__(self, index: int | slice) -> int | Bytes:
        if not self._buf:
            raise IndexError("Index out of range")

        if isinstance(index, slice):
            return self.from_static(self._buf[index])

        return self._buf[index]

    def __delitem__(self, key: typing.SupportsIndex | slice, /) -> None:
        if not self._buf:
            return

        del self._buf[key]
