# -*- coding: utf-8 -*-

# =============================================================================
# Docstring
# =============================================================================

"""
Tests for SingletonMeta Module
==============================

This test suite verifies the behavior of the `SingletonMeta` metaclass, which
implements the Singleton design pattern. It ensures that only one instance of
a class is created, regardless of how many times it is instantiated.

Tested Features:
----------------
- Ensures a single instance of a class using `SingletonMeta`.
- Validates that multiple instantiations return the same object.
- Confirms thread-safety for Singleton creation.
- Verifies instance reset behavior for testing purposes.

Dependencies:
-------------
- `pytest` for writing and executing tests.
- `threading` for testing thread-safe Singleton behavior.

"""

# =============================================================================
# Imports
# =============================================================================

import threading

import pytest

from rite.data.singleton import SingletonMeta

# =============================================================================
# Test Classes
# =============================================================================


class SingletonTestClass(metaclass=SingletonMeta):
    """
    A test class to verify the Singleton behavior of `SingletonMeta`.
    """

    def __init__(self, value: str) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"<{self.__class__.__module__}.{self.__class__.__name__} object at {hex(id(self))}>"

    @classmethod
    def reset_instance(cls):
        """
        Reset the Singleton instance for testing purposes.
        """
        if cls in SingletonMeta._instances:
            del SingletonMeta._instances[cls]


# =============================================================================
# Test Cases
# =============================================================================


def test_singleton_instance():
    """
    Test that `SingletonMeta` ensures only one instance is created.
    """
    instance1 = SingletonTestClass("value1")
    instance2 = SingletonTestClass("value2")

    assert (
        instance1 is instance2
    ), "SingletonMeta should ensure a single instance."
    assert (
        instance1.value == "value2"
    ), "The value should reflect the latest initialization."


def test_singleton_thread_safety():
    """
    Test the thread-safety of `SingletonMeta`.

    Ensures that even when multiple threads attempt to create an instance, only
    one instance is created.
    """
    instances = []

    def create_instance():
        instance = SingletonTestClass("thread-safe")
        instances.append(instance)

    threads = [threading.Thread(target=create_instance) for _ in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    assert all(
        instance is instances[0] for instance in instances
    ), "All instances should be the same due to SingletonMeta."


def test_singleton_reset():
    """
    Test resetting the Singleton instance for testing purposes.
    """
    instance1 = SingletonTestClass("value1")
    SingletonTestClass.reset_instance()  # Reset the Singleton instance
    instance2 = SingletonTestClass("value2")

    assert (
        instance1 is not instance2
    ), "Resetting should allow the creation of a new instance."
    assert (
        instance2.value == "value2"
    ), "The new instance should have the updated value."


def test_singleton_repr():
    """
    Test the `repr` output for Singleton instances.

    Ensures that the `repr` method provides the expected output for debugging
    and introspection.
    """
    instance = SingletonTestClass("repr-test")
    expected_repr = f"<{SingletonTestClass.__module__}.{SingletonTestClass.__name__} object at {hex(id(instance))}>"
    assert (
        repr(instance) == expected_repr
    ), "The `repr` method should match the expected format."


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main()
