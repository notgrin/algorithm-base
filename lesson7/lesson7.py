from random import randint

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
print('Задание 1')
b = 15
array = [0] * b
for i in range(b):
    array[i] = randint(-100, 100)
print(array)


def insertion_sort(array_to_sort):
    a = array_to_sort
    for item in range(len(a)):
        v = a[item]
        j = item
        while (a[j - 1] < v) and (j > 0):
            a[j] = a[j - 1]
            j = j - 1
            a[j] = v
    return a


print(insertion_sort(array))
print('---')

"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
"""
print('Задание 2')
b = 15
array = [0] * b
for i in range(b):
    array[i] = randint(0, 50)
print(array)


def merge_sort(a):
    if len(a) < 2:
        return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:len(a)])

    m = j = k = 0

    while m < len(left) and j < len(right):
        if left[m] < right[j]:
            a[k] = left[m]
            m += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while m < len(left):
        a[k] = left[m]
        m += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
    return a


print(merge_sort(array))
print('---')

"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. 
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, 
то используйте метод сортировки, который не рассматривался на уроках.
"""
print('Задание 3')


def median(arr):
    a = arr[0]

    less_med_elems = []
    greater_med_elems = []
    left_med_shoulder = 0
    right_med_shoulder = 0

    for i in arr:
        if i < a:
            left_med_shoulder += 1
        elif i > a:
            right_med_shoulder += 1

        if i in arr:
            if i < a:
                less_med_elems.append(i)
            elif i > a:
                greater_med_elems.append(i)

    if left_med_shoulder > right_med_shoulder:
        return median(less_med_elems)
    elif left_med_shoulder < right_med_shoulder:
        return median(greater_med_elems)

    return a


m = randint(0, 10)
n = 2 * m + 1
# print(f'эелементов в массиве - {n}')

max_val = pow(n, 2)
array = []
while len(array) < n:
    x = randint(0, max_val)
    if x not in array:
        array.append(x)

print(array)
print(f'Медиана = {median(array)}')
