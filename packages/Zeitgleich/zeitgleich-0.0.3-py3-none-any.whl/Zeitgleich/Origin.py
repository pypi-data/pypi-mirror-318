# Origin.py

import re

class Origin(str):
    def get_device(self, regex: str = r"([^/]+)") -> str:
        match = re.match(regex, self)
        if match:
            return match.group(1)
        else:
            raise ValueError(f"Could not extract device from origin '{self}' using pattern '{regex}'.")

    def get_topic(self, regex: str = r"^[^/]+/(.+)$") -> str:
        match = re.match(regex, self)
        if match:
            return match.group(1)
        else:
            raise ValueError(f"Could not extract topic from origin '{self}' using pattern '{regex}'.")
