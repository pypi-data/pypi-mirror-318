# -*- coding: utf-8 -*-

# =============================================================================
# Docstring
# =============================================================================

"""
Tests for CircularBuffer Module
===============================

This test suite verifies the functionality of the `CircularBuffer` class,
which implements a fixed-size ring buffer with overwriting behavior when full.

Tested Features:
----------------
- Append elements and verify correct order.
- Check the full and empty state of the buffer.
- Handle overwriting of oldest elements.
- Proper handling of edge cases like zero or negative size.
- Validate `__repr__` output.

Dependencies:
-------------
- `pytest` for writing and executing tests.
"""

# =============================================================================
# Imports
# =============================================================================

import pytest

from rite.data.buffer_circular import CircularBuffer

# =============================================================================
# Test Cases
# =============================================================================


def test_initialization():
    """
    Test initialization of the CircularBuffer.
    """
    buffer = CircularBuffer(size=3)
    assert buffer.is_empty(), "Buffer should be empty upon initialization."
    assert (
        not buffer.is_full()
    ), "Buffer should not be full upon initialization."
    assert buffer.get_all() == [], "Buffer contents should be empty."

    with pytest.raises(
        ValueError, match="Buffer size must be a positive integer."
    ):
        CircularBuffer(size=0)

    with pytest.raises(
        ValueError, match="Buffer size must be a positive integer."
    ):
        CircularBuffer(size=-1)


def test_append_and_get_all():
    """
    Test appending elements to the buffer and retrieving them.
    """
    buffer = CircularBuffer(size=3)
    buffer.append(1)
    buffer.append(2)

    assert buffer.get_all() == [
        1,
        2,
    ], "Buffer should return appended elements in correct order."
    assert (
        not buffer.is_full()
    ), "Buffer should not be full after partial appending."
    assert (
        not buffer.is_empty()
    ), "Buffer should not be empty after appending elements."

    buffer.append(3)
    assert buffer.is_full(), "Buffer should be full after reaching its size."
    assert buffer.get_all() == [
        1,
        2,
        3,
    ], "Buffer should contain all appended elements."


def test_overwrite_behavior():
    """
    Test overwriting behavior when the buffer is full.
    """
    buffer = CircularBuffer(size=3)
    buffer.append(1)
    buffer.append(2)
    buffer.append(3)
    buffer.append(4)  # Overwrites 1
    buffer.append(5)  # Overwrites 2

    assert buffer.is_full(), "Buffer should remain full after overwriting."
    assert buffer.get_all() == [
        3,
        4,
        5,
    ], "Buffer should overwrite the oldest elements correctly."


def test_edge_case_single_element_buffer():
    """
    Test behavior with a buffer size of 1.
    """
    buffer = CircularBuffer(size=1)
    buffer.append(1)
    assert buffer.get_all() == [
        1
    ], "Buffer should store a single element correctly."
    buffer.append(2)  # Overwrites 1
    assert buffer.get_all() == [
        2
    ], "Buffer should overwrite the single element correctly."


def test_is_empty():
    """
    Test the is_empty() method of the CircularBuffer.
    """
    buffer = CircularBuffer(size=3)
    assert buffer.is_empty(), "Buffer should be empty initially."

    buffer.append(1)
    assert (
        not buffer.is_empty()
    ), "Buffer should not be empty after appending an element."

    buffer.append(2)
    buffer.append(3)
    assert not buffer.is_empty(), "Buffer should not be empty when full."


def test_is_full():
    """
    Test the is_full() method of the CircularBuffer.
    """
    buffer = CircularBuffer(size=3)
    assert not buffer.is_full(), "Buffer should not be full initially."

    buffer.append(1)
    buffer.append(2)
    assert (
        not buffer.is_full()
    ), "Buffer should not be full after partial appending."

    buffer.append(3)
    assert (
        buffer.is_full()
    ), "Buffer should be full after appending maximum elements."


def test_repr():
    """
    Test the __repr__ method of the CircularBuffer.
    """
    buffer = CircularBuffer(size=3)
    buffer.append(1)
    buffer.append(2)
    repr_output = repr(buffer)

    expected_output = (
        "CircularBuffer(\n"
        "    size=3,\n"
        "    buffer=[1, 2],\n"
        "    full=False\n"
        ")"
    )
    assert (
        repr_output == expected_output
    ), "The __repr__ output should match the expected format."


def test_large_buffer():
    """
    Test the behavior of a large buffer.
    """
    buffer = CircularBuffer(size=1000)
    for i in range(1000):
        buffer.append(i)

    assert (
        len(buffer.get_all()) == 1000
    ), "Buffer should hold the maximum number of elements."
    buffer.append(1001)
    assert (
        buffer.get_all()[0] == 1
    ), "Buffer should overwrite the oldest element correctly."


def test_get_all_empty():
    """
    Test get_all() on an empty buffer.
    """
    buffer = CircularBuffer(size=3)
    assert (
        buffer.get_all() == []
    ), "Buffer should return an empty list when no elements are appended."


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main()
