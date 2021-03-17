user_numbers = input('Введите числа через пробел: ').split()

numbers = []
for number in user_numbers:
    try:
        number = int(number)
        numbers.append(number)
    except ValueError:
        print("ОШИБКА! Похоже Вы ввели не число!!!")
        quit()


check_number = input('Введите проверочное число: ')

try:
    check_number = int(check_number)
except ValueError:
    print("ОШИБКА! Проверочное число неверное!!!")
    quit()


# Insertion Sort Algorithm
def numbers_sort(data):
    for i in range(1, len(data)):
        n = data[i]
        idn = i

        while idn > 0 and n < data[idn - 1]:
            data[idn] = data[idn - 1]
            idn -= 1
        data[idn] = n

    return data


print(f'Список, введенный пользователем: {numbers}.')


numbers = numbers_sort(numbers)
print(f'Список, отсортированный в Python: {numbers}.')


ind = list(filter(lambda x: numbers[x] < check_number, range(len(numbers))))
if check_number < numbers[0]:
    print('Проверочное число меньше наименьшего числа в отсортированном списке.')
elif check_number > numbers[-1]:
    print('Проверочное число больше наибольшего числа в отсортированном списке.')
elif check_number in numbers:
    print(f'Проверочное число {check_number} является элементом списка.')
else:
    print(f'Проверочное число {check_number} находится между числом {numbers[len(ind) - 1]} с индексом {len(ind) - 1} '
          f'и числом {numbers[len(ind)]} с индексом {len(ind)}.')
