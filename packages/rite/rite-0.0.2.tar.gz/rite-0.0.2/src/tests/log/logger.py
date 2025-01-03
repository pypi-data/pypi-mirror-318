# -*- coding: utf-8 -*-

# =============================================================================
# Docstring
# =============================================================================

"""
Tests for Logger Module
=======================

This test suite verifies the functionality of the `Logger` class, a configurable
logging utility for applications.

Tested Features:
----------------
- Log messages to console and file.
- Verify correct log levels for debug, info, warning, error, and critical.
- Clear the log file content.
- Handle invalid log levels.

Dependencies:
-------------
- `pytest` for writing and executing tests.
- `os` and `tempfile` for temporary file handling.

"""

# =============================================================================
# Imports
# =============================================================================

import os
import tempfile

import pytest

from rite.log import Logger

# =============================================================================
# Test Cases
# =============================================================================


def test_logger_initialization():
    """
    Test initialization of the Logger with console and file logging.
    """
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        logger = Logger(name="TestLogger", log_file=temp_log.name)
        assert logger.log_file == temp_log.name, "Log file path should match."

    os.remove(temp_log.name)


def test_logging_levels():
    """
    Test logging at various levels (debug, info, warning, error, critical).
    """
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        logger = Logger(name="TestLogger", log_file=temp_log.name)

        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")

        with open(temp_log.name, "r") as log_file:
            log_content = log_file.read()

        assert (
            "Debug message" in log_content
        ), "Debug message should be logged."
        assert "Info message" in log_content, "Info message should be logged."
        assert (
            "Warning message" in log_content
        ), "Warning message should be logged."
        assert (
            "Error message" in log_content
        ), "Error message should be logged."
        assert (
            "Critical message" in log_content
        ), "Critical message should be logged."

    os.remove(temp_log.name)


def test_invalid_log_level():
    """
    Test logging with an invalid log level.
    """
    logger = Logger(name="TestLogger")

    with pytest.raises(ValueError, match="Invalid log level: invalid"):
        logger.log("invalid", "This should raise an error")


def test_clear_log():
    """
    Test clearing the log file content.
    """
    with tempfile.NamedTemporaryFile(delete=False) as temp_log:
        logger = Logger(name="TestLogger", log_file=temp_log.name)

        logger.info("Test message")
        logger.clear_log()

        with open(temp_log.name, "r") as log_file:
            log_content = log_file.read()

        assert (
            log_content == ""
        ), "Log file should be cleared after calling clear_log."

    os.remove(temp_log.name)


def test_console_logging(capsys):
    """
    Test console logging output.
    """
    logger = Logger(name="TestLogger")

    logger.info("Console info message")
    captured = capsys.readouterr()

    assert (
        "Console info message" in captured.out
    ), "Console logging should capture messages."


# =============================================================================
# Run Tests
# =============================================================================

if __name__ == "__main__":
    pytest.main()
