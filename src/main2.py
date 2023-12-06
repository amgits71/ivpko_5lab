from model import GetTextNote, GetInfoNote, GetListNote, PostNote
from datetime import datetime

if __name__ == '__main__':
    text_response = GetTextNote(
        id = 123,
	    text = 'sdjhskdhsdjh'
    )
    print(text_response.json())

    info_response = GetInfoNote(
        created_at = datetime(2022, 11, 10, 12, 30, 10, 123),
        updated_at = datetime(2022, 11, 11, 12, 10, 10, 123)
    )
    print(info_response.json())

    list_response = GetListNote(
        notes={
            0: 769,
            1: 123,
            2: 456
        }
    )
    print(list_response.json())

    post_response = PostNote(
        id=123
    )
    print(post_response.json())

