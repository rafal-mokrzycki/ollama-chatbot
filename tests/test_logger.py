import os
import shutil

import pytest

from utils.logger import CustomLogger


@pytest.fixture(scope="module")
def logger():
    """Fixture to create a CustomLogger instance for testing."""
    log_file_path = "logs_for_tests/conversation_test.log"
    logger_instance = CustomLogger(log_file_path)

    yield logger_instance


def test_create_directory(logger):
    """
    Test that the 'logs_for_tests' directory
    is created if it doesn't already exist.
    """

    logger.create_directory("logs_for_tests")
    assert os.path.exists("logs_for_tests")
    shutil.rmtree("logs_for_tests", ignore_errors=True)


def test_create_log_file(logger):
    """Test that a log file is created with a specified name."""

    logger.create_log_file("logs_for_tests")
    assert logger.log_file_path == "logs_for_tests/conversation_test.log"


def test_write_logs(logger):
    """Test that logs are written correctly to the log file."""

    logger.create_log_file()  # Ensure the log file is created

    # Write a log entry
    logger.write_logs("What is your name?", "I am an AI chatbot.")

    # Read the log file content to verify it was written correctly
    with open(logger.log_file_path, "r", encoding="utf-8") as log_file:
        content = log_file.read()

    expected_content = "User: What is your name?\nAI: I am an AI chatbot.\n"

    assert (
        expected_content in content
    ), f"Expected content not found in log file. Content: {content}"


if __name__ == "__main__":
    pytest.main()
