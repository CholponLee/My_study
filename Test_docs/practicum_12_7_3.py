# Вводится сумма, которую человек планирует положить под проценты
money = float(input('Введите сумму вклада (рублей): '))

# Даны процентные ставки в банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Извлечение процентных ставок из словаря в список
banks = list(per_cent.keys())

# Извлечение процентных ставок из словаря в список
percents = list(per_cent.values())

# Создание списка сумм, которые можно заработать на вкладе в разных банках
deposit = list()
deposit.append(int(money / 100 * float(percents[0])))
deposit.append(int(money / 100 * float(percents[1])))
deposit.append(int(money / 100 * float(percents[2])))
deposit.append(int(money / 100 * float(percents[3])))
print(f'\nДоход по депозиту составит:\n{banks[0]} банк - {deposit[0]} рублей\n{banks[1]} банк - {deposit[1]} '
      f'рублей\n{banks[2]} банк - {deposit[2]} рублей\n{banks[3]} банк - {deposit[3]} рублей\n')

# Максимальная сумма, которую можно заработать
max_deposit = max(deposit)
print('Максимальная сумма, которую Вы можете заработать: {} рублей.'.format(max_deposit))
