import requests
from src.web_app import is_token_right
# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8080

def menu(choice, token):
    if choice == 2 or choice == 3 or choice == 4 or choice == 5:
        id_note = int(input("Введите идентификатор заметки: "))

    if choice == 1:
        response = requests.post(f"http://{HOST}:{PORT}/create_note", params={"token": token})
    elif choice == 2:
        response = requests.get(f"http://{HOST}:{PORT}/text_note", params={"token": token, "id_note": id_note})
    elif choice == 3:
        response = requests.get(f"http://{HOST}:{PORT}/info_note", params={"token": token, "id_note": id_note})
    elif choice == 4:
        text = input("Введите текст: ")
        response = requests.patch(f"http://{HOST}:{PORT}/update_note", params={"token": token, "id_note": id_note, "text": text})
    elif choice == 5:
        response = requests.delete(f"http://{HOST}:{PORT}/delete_note", params={"token": token, "id_note": id_note})
    elif choice == 6:
        response = requests.get(f"http://{HOST}:{PORT}/list_note", params={"token": token})
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
        return 0
    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")

token = input("Введите токен: ")
if is_token_right(token):
    print("Меню:")
    print("1. Создать заметку")
    print("2. Прочитать заметку по id")
    print("3. Получить информацию о времени создания и последнего изменения заметки")
    print("4. Обновить текст заметки")
    print("5. Удалить заметку")
    print("6. Вывести список id заметок\n")

    while (True):
        choice = int(input("Введите номер действия: "))
        if (choice < 1 or choice > 6):
            print("Завершение программы")
            break
        menu(choice, token)
else:
    print("Пользователь не авторизован. Неправильный токен")



