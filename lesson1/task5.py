"""
5. Пользователь вводит две буквы.
Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""

print('START')
a = input('Введите первую буку: ')
letter1 = int(ord(a.lower())) - 96
b = input('Введите вторую буку: ')
letter2 = int(ord(b.lower())) - 96
c = letter2 - letter1 - 1

print(f'Порядковый номер буквы {a} - {letter1}, порядковый номер буквы {b} - {letter2}, между ними {c} букв(ы).')
print('DONE')
