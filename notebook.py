import json
from note import Note
from note import CustomEncoder
from pathlib import Path
from datetime import datetime
import os


def generate_id() -> int:
    id_db_path = Path("ids.json")
    db_path = Path("data.json")
    with open(db_path, "r+") as database:
        json_read = json.load(database)
        if len(json_read) > 0 and json_read != '0':
            identifiers_list = list()
            for i in range(len(json_read)):
                identifiers_list.append(json_read[i]["note_id"])
            available_id = int(max(identifiers_list) + 1)
            with open(id_db_path, "w") as id_db:
                json.dump(available_id, id_db)
            return int(available_id)

        else:
            with open(id_db_path, "r+") as file:
                id_db = json.load(file)
                if id_db == "0":
                    file.seek(0)
                    json.dump("1", file)
                    return 1
                else:
                    available_id = int(id_db) + 1
                    file.seek(0)
                    json.dump(str(available_id), file)
                    return available_id


class Notebook:

    def __init__(self):
        self.list = list()
        self.is_first_start()

    def add_note(self, note):
        self.list.append(note)

    def remove_note(self, note_id):
        for note in self.list:
            if note.__getattribute__("note_id") == note_id:
                if len(self.list) == 1:
                    self.init_database()
                self.list.remove(note)
        self.save_notebook()

    def edit_note(self, note_id):
        for note in self.list:
            if note.__getattribute__("note_id") == note_id:
                command = input("""
                1 - edit header
                2 - edit body 
                """)
                if command != "1" and command != "2":
                    print("Entered wrong command.")
                match command:
                    case "1":
                        new_header = input("Enter the new header: ")
                        note.__setattr__("header", new_header)
                        note.__setattr__("datetime", str(datetime.now()))
                    case "2":
                        new_body = input("Enter the new body: ")
                        note.__setattr__("body", new_body)
                        note.__setattr__("datetime", str(datetime.now()))

    def show_note(self, note_id):
        for note in self.list:
            if note.__getattribute__("note_id") == note_id:
                print(note)

    def save_notebook(self):
        with open("data.json", "w") as file:
            json.dump(self.list, file, cls=CustomEncoder)

    def load_notebook(self):
        db_path = Path("data.json")
        is_blank = db_path.stat().st_size == 0
        if is_blank:
            print("Data base is empty. Nothing to load.")
        else:
            with open(db_path, "r") as file:
                json_input = json.load(file)
                if json_input == '0' or len(json_input) == 0:
                    print("Data base is empty. Nothing to load.")
                else:
                    dict_keys = json_input[0].keys()
                    temp_list = list()
                    for x in range(len(json_input)):
                        temp_note = Note(None, None, 0)
                        for y in dict_keys:
                            temp_note.__setattr__(y, json_input[x][y])
                        # self.add_note(temp_note)
                        temp_list.append(temp_note)
                        self.list = temp_list
                    print("Notes loaded.")

    def init_database(self):
        default_db_value = "0"
        with open("data.json", "w") as database:
            database.seek(0)
            json.dump(default_db_value, database)
        with open("ids.json", "w") as id_database:
            id_database.seek(0)
            json.dump(default_db_value, id_database)

    def is_first_start(self):
        is_data_base_exists = os.path.exists("data.json")
        is_id_data_base_exists = os.path.exists("ids.json")
        if not is_id_data_base_exists and not is_data_base_exists:
            self.init_database()