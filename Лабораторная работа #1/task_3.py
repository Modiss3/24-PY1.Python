list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players_amount = len(list_players)
middle_index = players_amount // 2

team_A = list_players[:middle_index]
team_B = list_players[middle_index:]

print( "Первая команда:", team_A, "\n" + "Вторая команда:", team_B)