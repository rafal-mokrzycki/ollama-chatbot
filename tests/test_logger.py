import os
import shutil

import pytest

from utils.logger import CustomLogger


@pytest.fixture(scope="module")
def logger():
    """Fixture to create a CustomLogger instance for testing."""
    log_file_path = "logs/test_conversation.log"
    logger_instance = CustomLogger(log_file_path)

    # Ensure the logs directory exists for testing
    if not os.path.exists("logs"):
        os.makedirs("logs")

    yield logger_instance

    # Clean up after tests are done
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
    if os.path.exists("logs") and not os.listdir("logs"):
        os.rmdir("logs")  # Remove the logs directory if empty


def test_create_directory(logger):
    """Test that the 'logs' directory is created if it doesn't already exist."""
    # Remove the logs directory for testing purposes
    if os.path.exists("logs"):
        shutil.rmtree("logs")  # Use rmtree to ensure it's removed

    logger.create_directory()
    assert os.path.exists("logs")


def test_create_log_file(logger):
    """Test that a log file is created with a specified name."""
    logger.create_log_file()

    # Check if log file path is set correctly
    assert logger.log_file_path is not None, "Log file path should not be None"

    # Check if the log file was created
    assert os.path.isfile(
        logger.log_file_path
    ), f"Log file {logger.log_file_path} was not created."


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
