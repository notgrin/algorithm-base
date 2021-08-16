"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
 Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

print('START')
a = int(input('Введите натуральное число: '))
a = str(a)
even = []
odd = []
for i in a:
    i = int(i)
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f'В числе {a} четных цифр: {len(even)} {even} и {len(odd)} нечетных {odd}')
print('DONE')
