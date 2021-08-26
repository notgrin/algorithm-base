import collections

"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
 (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
  (за год для всех предприятий) и вывести наименования предприятий,
   чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""
print('Задание 1')
organisations = collections.defaultdict()
n = int(input('Введите кол-во предприятий: '))
quarter = 4
common_profit = 0
for i in range(n):
    name = input(str(i+1) + ". предприятние: ")
    profit = 0
    q = 1
    while q <= quarter:
        profit += float(input(f"Прибыль за {q} квартал: "))
        q += 1
    organisations[name] = profit
    common_profit += profit

avrg_profit = common_profit / n

print(f'Средняя прибыль за год у предприятий: {avrg_profit:.2f} у.е.')
print('Прибыль выше среднего у предприятий: ')
for k, v in organisations.items():
    if v > avrg_profit:
        print(k)

print('------------------------------')

"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
 При этом каждое число представляется как массив, элементы которого это цифры числа.
  Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
   Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
print('Задание 2')


def my_dex(string):
    dex = 0
    num = collections.deque(string)
    # print(num)
    num.reverse()
    for i in range(len(num)):
        dex += table[num[i]] * 16 ** i
    return dex


def my_hex(numb):
    num = collections.deque()
    while numb > 0:
        d = numb % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


signs = '0123456789ABCDEF'
table = collections.defaultdict(int)
counter = 0
for key in signs:
    table[key] += counter
    counter += 1

num_1 = my_dex(input('Введите первое число в шестнадцатиричном формате: ').upper())
num_2 = my_dex(input('Введите второе число в шестнадцатиричном формате: ').upper())

print(f'Сумма чисел: {my_hex(num_1 + num_2)}')
print(f'Произведение чисел: {my_hex(num_1 * num_2)}')
