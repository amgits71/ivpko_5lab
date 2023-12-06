import fastapi
import os
from model import GetTextNote, GetInfoNote, GetListNote, PostNote

api_router = fastapi.APIRouter()

notesPath = 'C:/Users/MYaO/PycharmProjects/ivpko_lab5/notes'
tokenPath = 'C:/Users/MYaO/PycharmProjects/ivpko_lab5/token.txt'

def note_path(id):
    return notesPath + '/' + str(id) + '.txt'

def count_files_in_folder(notesPath):
    if os.path.exists(notesPath) and os.path.isdir(notesPath):
        file_count = len(os.listdir(notesPath))
        return file_count

def is_token_right(token):
    with open(tokenPath, 'r') as file:
        content = file.read()

    if token == content:
        return True
    else:
        print("Неверный токен")
        return False

@api_router.post("/create_note", response_model=PostNote)
def post_notes(token: str):
    try:
        if is_token_right(token):
            id_note = count_files_in_folder(notesPath)
            if not os.path.exists(note_path(id_note)):
                file = open(note_path(id_note), 'a')
                file.close()
            else:
                id_note += 1
                file = open(note_path(id_note), 'a')
                file.close()
            return PostNote(
                id = id_note
            )
    except Exception as e:
        print(e)

@api_router.get("/text_note", response_model=GetTextNote)
def text_notes(token: str, id_note: int):
    try:
        if is_token_right(token):
            with open(note_path(id_note), 'r') as file:
                content = file.read()
            return GetTextNote(
                id = id_note,
                text = content
            )
    except Exception as e:
        print(e)

@api_router.get("/info_note", response_model=GetInfoNote)
def text_notes(token: str, id_note: int):
    try:
        if is_token_right(token):
            modified_time = os.path.getmtime(note_path(id_note))
            creation_time = os.stat(note_path(id_note)).st_ctime
            return GetInfoNote(
                created_at = creation_time,
                updated_at = modified_time
            )
    except Exception as e:
        print(e)

@api_router.patch("/update_note", response_model=str)
def update_note(token: str, id_note: int, text: str):
    try:
        if is_token_right(token):
            with open(note_path(id_note), 'w') as file:
                file.write(text)
            return text
    except Exception as e:
        print(e)

@api_router.delete("/delete_note", response_model=str)
def delete_note(token: str, id_note: int):
    try:
        if is_token_right(token):
            os.remove(note_path(id_note))
            text = "Заметка успешно удалена"
            return text
    except Exception as e:
        print(e)

@api_router.get("/list_note", response_model=GetListNote)
def list_note(token: str):
    try:
        if is_token_right(token):
            notes_list = os.listdir(notesPath)
            dictionary_note = {}
            for i in range(len(notes_list)):
                dictionary_note[i] = int(notes_list[i].split('.')[0])
            return GetListNote(
                notes = dictionary_note
            )
    except Exception as e:
        print(e)
