import random
import string

def generate_password(length=8) -> str:
    """Функция генерации пароля при добавлении нового пользователя через админ-панель.
    Базовая длина пароля - 8"""
    characters = string.ascii_letters.lower() + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
