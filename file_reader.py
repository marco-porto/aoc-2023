import logging

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        try:
            self.file = open(self.filename, "r")
            return self.file
        except Exception as e:
            logging.info(f"FILE READER - Unexpected error trying to open {self.filename}: {e}")
            return None

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            logging.info(f"FILE READER - An error occurred: {exc_type}, {exc_value}")
        try:
            self.file.close()
        except Exception as e:
            logging.info(f"FILE READER - Error closing {self.filename}: {e}")