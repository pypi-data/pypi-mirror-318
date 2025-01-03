import json
import os


class JsonLineHandler:
    def __init__(self, file_url):
        """
        Initialize the handler with the file URL.

        :param file_url: Path to the file.
        """
        self.file_url = file_url
        if os.path.exists(self.file_url):
            return # File already exists
        os.makedirs(os.path.dirname(self.file_url), exist_ok=True)
        # Ensure the file is empty before each test
        with open(self.file_url, "w"):
            pass

    def append(self, obj):
        """
        Append a JSON object as a new line in the file.

        :param obj: Python dictionary or JSON-serializable object.
        """
        with open(self.file_url, 'a') as file:
            file.write(json.dumps(obj) + '\n')

    def iterate(self, reverse=False):
        """
        Get an iterator that reads lines from the file and yields JSON objects.

        :param reverse: If True, iterate from the last line to the first line.
        :return: Iterator of JSON objects.
        """

        # As simple case, when need to iterate in forward order
        if not reverse:
            # Reading lines in forward order
            with open(self.file_url, 'r') as file:
                for line in file:
                    yield json.loads(line)
            return

        # Reading lines in reverse order using memory-efficient method
        with open(self.file_url, 'rb') as file:
            file.seek(0, 2)  # Move to end of file
            position = file.tell()
            buffer = bytearray()
            while position > 0:
                file.seek(position - 1)
                char = file.read(1)
                position -= 1
                if char == b'\n' and buffer:
                    yield json.loads(buffer[::-1].decode())
                    buffer.clear()
                buffer.extend(char)
            if buffer:
                yield json.loads(buffer[::-1].decode())
