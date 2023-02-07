# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.

# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers!")
        return []
    list_nums = sample(range(1, count * 2), count)
    return list_nums


list = list_rand_nums(int(input('Введите число элементов: ')))
new_list = [i for num, i in enumerate(list) if list[num - 1] < list[num] and num !=0]
print(f'Исходный список {list}')
print(f'Новый список {new_list}')