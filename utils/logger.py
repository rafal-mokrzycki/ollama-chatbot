import datetime
import os


class CustomLogger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def create_directory(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")

    def create_log_file(self):
        if self.log_file_path is None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            self.log_file_path = os.path.join("logs", f"conversation_{timestamp}.log")

    def write_logs(self, question, answer):
        with open(self.log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"User: {question}\n")
            log_file.write(f"AI: {answer}\n")
