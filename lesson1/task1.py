# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print('START')
num = int(input('Введите трехзначное положительное число: '))
a = num // 100
b = num % 100 // 10
c = num % 10
print(f'Сумма цифр числа {num} равняется: ', a + b + c)
print(f'Произведение цифр числа {num} равняется: ', a * b *c)
print('DONE')
