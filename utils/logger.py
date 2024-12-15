class CustomLogger:
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def write_logs(self, question, answer):
        with open(self.log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(f"User: {question}\n")
            log_file.write(f"AI: {answer}\n")
