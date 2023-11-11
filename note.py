import json
from datetime import datetime
from typing import Any


class Note:

    def __init__(self, header, body, note_id):
        self.header = header
        self.body = body
        self.datetime = str(datetime.now())
        self.note_id = int(note_id)

    def __str__(self):
        return (f"Header: {self.header}\n"
                f"Body: {self.body}\n"
                f"Create date: {self.datetime}\n"
                f"ID: {self.note_id}")

    def __setattr__(self, __name: str, __value: Any) -> None:
        super().__setattr__(__name, __value)


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__