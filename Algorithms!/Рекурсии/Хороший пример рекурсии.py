# Напишите функцию list_sum_recursive, которая принимает на вход список из целых чисел и возвращает сумму
# элементов переданного списка. Не забывайте, что реализовать это нужно при помощи рекурсии.

def list_sum_recursive(x):
    if isinstance(x, str):
        x = list(map(int, x.split()))

    if len(x) == 0:
        return 0
    if len(x) == 1:
        return x[0]  # внимательно для последней рекурсии

    return x[0] + list_sum_recursive(x[1:])  # с конца суммирует


print(list_sum_recursive('1 2 3 4'))
