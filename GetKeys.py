def get_key(dictionary, value):
    """Функция, которая используется для получения ключа по значению из словаря."""
    for key, val in dictionary.items():
        if val == value:
            return key
