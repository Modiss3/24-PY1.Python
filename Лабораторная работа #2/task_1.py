money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
not_in_debt = True # Значение отсутствия долгов
month_counter = 0 #

while not_in_debt:
    spend += spend * increase * bool(month_counter) # Перевод счетчика месяцев в булево значение, т.к. в нулевой итерации (первом месяце) увеличения трат нет, а во вслех последующих есть
    month_counter += 1
    money_capital += salary - spend
    not_in_debt = (money_capital + salary) > spend # Проверка отсутствия долгов на следующий месяц




print("Количество месяцев, которое можно протянуть без долгов:", spend_increase)
