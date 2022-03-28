# Представьте, что у нас есть список целых чисел неограниченной вложенности. То есть наш список может состоять из
# списков, внутри которых также могут быть списки. Ваша задача превратить все это в линейный список при помощи
# функции flatten

def flatten(s):
    if not s:
        return []

    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    return s[:1] + flatten(s[1:])


print(flatten([1, [2, 3, [4]], 5]))  # вернет [1,2,3,4,5]
print(flatten([1, [2, 3], [[2], 5], 6]))  # вернет [1,2,3,2,5,6]
print(flatten([[[[9]]], [1, 2], [[8]]]))  # вернет [9,1,2,8]
