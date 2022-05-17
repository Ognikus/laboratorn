import json

def get_username():
    """Получение имени пользователя"""
    filename = 'text.json'
    try:
        with open(filename, encoding="utf8") as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user

def greed_user():
    """Приветсвие пользователя"""
    user_name = get_username()
    if user_name:
        print(f"Добро пожаловать {user_name}!")
    else:
        user_name = input("Введите ваше ФИО: ")
        filename = 'text.json'
        with open(filename, 'w', encoding="utf8") as f:
            json.dump(user_name, f, ensure_ascii=False)
            print(f"Мы запомнили тебя как {user_name}!")


greed_user()
