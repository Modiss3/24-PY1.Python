# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, seconds_group, split_sign=','):
    first_group_set = set(first_group.split(split_sign)) #создаем список на основе строки участников и переводим в множество, т.к. метод intersection() принадлежит ему
    second_group_list = seconds_group.split(split_sign) #создаем список на основе строки участников
    common_participants_list = list(first_group_set.intersection(second_group_list)) #создаем список из повторных участников
    common_participants_list.sort() #сортируем список повторяющихся участников
    return common_participants_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, split_sign='|'))
