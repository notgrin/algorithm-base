# 3. По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

print('START')
x1 = float(input('Введите x коорбинаты точки A(x1, y1): '))
y1 = float(input(f'Введите y коорбинаты точки A(x1, y1): '))

x2 = float(input('Введите x коорбинаты точки A(x2, y2: '))
y2 = float(input(f'Введите y коорбинаты точки A(x2, y2): '))

print('Координаты точек:')
print(f'A({x1:.2f}, {y1:.2f})')
print(f'B({x2:.2f}, {y2:.2f})')

# print("Уравнение прямой вида y=kx+b, проходящей через эти точки:")
k = (y1 - y2) / (x1 - x2)
k = float(k)
b = y2 - k * x2
b = float(b)
print(f'y = {k:.2f} * x + {b:.2f}')
print('DONE')
