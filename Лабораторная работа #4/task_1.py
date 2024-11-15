import json

INPUT_FILE = 'input.json'


def task() -> float:
    """Функция десериализирует json файл, содержащий список словарей, и возвращает сумму произведений
    значений с ключами 'weight' и 'score', округленную до 3 значений после запятой"""
    with open(INPUT_FILE) as f:  # открытие json файла для чтения
        json_data = json.load(f)  # десериализация списка словарей из json файла

    # возврат округленной суммы списка произведений, составленного с помощью list comprehension
    return round(sum([dict_item['score'] * dict_item['weight'] for dict_item in json_data]), 3)


print(task())
