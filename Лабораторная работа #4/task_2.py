# импорт модулей json и csv для удобной работы с форматами
import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    """Функция десериализирует csv файл и преобразует данные в json для дальнейшей записи в файл в виде списка словарей
    [{header_1: value, ..., header_n: value}, ...]"""
    with open(INPUT_FILENAME) as f:  # открытие csv файла для чтения
        file_lines = [line_ for line_ in csv.DictReader(f)]  # чтение из csv файла списка словарей
    with open(OUTPUT_FILENAME, 'w') as f:  # открытие json файла для записи
        json.dump(file_lines, f, indent=4)  # сериализация списка словарей file_lines и запись в файл json формата


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
