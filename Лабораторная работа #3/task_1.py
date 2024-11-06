# TODO Напишите функцию для поиска индекса товара
def find_index(source_list, searched_item):
    for item_index, item_name in enumerate(source_list): #перебираем список по парам из индексов и значений
        if searched_item == item_name:
            return item_index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
