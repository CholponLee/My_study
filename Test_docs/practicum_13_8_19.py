# Получаем данные от пользователя по количеству билетов и проверяем, что введено число
users = input('Сколько билетов для посещения конференции Вы хотите приобрести? ')
try:
    users = int(users)
except ValueError:
    print('ОШИБКА!!! Введите число!')
    quit()


# Получаем данные от пользователя по возрасту посетителей и проверяем, что введено число,
# а также, что введено корректное число
age = []
for user in range(1, users + 1):
    try:
        a = int(input(f'Укажите возраcт посетителя для билета {user}: '))
        age.append(a)
    except ValueError:
        print("ОШИБКА! Введите число!")
        quit()
    else:
        if a > 100 or a <= 0:
            print('Указано неверное значение возраста!')
            quit()


# Стоимость билетов для разных возрастных групп
price1 = 0
price2 = 990
price3 = 1390


# Определяем общую стоимость билетов
# А также проверяем корректность введенного значения для возраста
price = []
for a in age:
    if 0 < a < 18:
        price.append(price1)
    elif 18 <= a < 25:
        price.append(price2)
    else:
        price.append(price3)

total_price = float(sum(price))


# Определяем, возможно ли применить скидку 10%. Если да, то вычисляем стоимость билето со скидкой
# А также проверяем, что введенное количество билетов не ноль и не отрицательное число
if users > 3:
    total_price_off = total_price * 0.9
    print(f'Сумма за {users} билет(-а,-ов) составила {total_price} рубля(-ей).\nВам предоставлена скидка 10%.'
          f'\nСумма к оплате - {total_price_off} рубля(-ей).')
elif 0 < users <= 3:
    print(f'Сумма к оплате за {users} билет(-а,-ов) составила {total_price} рубля(-ей).')
else:
    print('Укажите корректное количество билетов!')
    quit()