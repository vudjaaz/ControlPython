from notebook import *
from note import Note

notebook = Notebook()
isContinue = True


def create_note():
    print("Note creating module activated...")
    note = Note(input("Note header: "), input("Note body: "), generate_id())
    notebook.add_note(note)
    print("Note created.")
    save_notebook()


def show_all():
    for x in notebook.list:
        print(x)


def edit_note():
    print("Note editor activated...")
    try:
        note_edit_id = int(input("Enter note id to be edited: "))
        notebook.show_note(note_edit_id)
        notebook.edit_note(note_edit_id)
        save_notebook()
    except ValueError:
        print("Oops!  That was no valid number.")


def delete_note():
    print("Note deleting mode activated...")
    try:
        note_delete_id = int(input("Enter note id to be deleted: "))
        notebook.remove_note(note_delete_id)
    except ValueError:
        print("Oops!  That was no valid number.")


def save_notebook():
    notebook.save_notebook()


def load_notebook():
    notebook.load_notebook()


while isContinue:
    print("""
    1 - create note
    2 - show all
    3 - edit note
    4 - delete note
    5 - load notes
    6 - exit program
    """)

    command = input("Your choice: ")

    match command:
        case "1":
            create_note()
        case "2":
            show_all()
        case "3":
            edit_note()
        case "4":
            delete_note()
        case "5":
            load_notebook()
        case "6":
            print("Good bye")
            isContinue = False
        case _:
            print("You entered wrong command!")