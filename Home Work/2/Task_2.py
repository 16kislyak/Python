# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

def multiplication(n):
    if n == 1:
        return 1
    else:
        return n * multiplication(n - 1)

print('Введите число: ')
num = int(input())
mult = []

for i in range(1, num + 1):
    mult.append(multiplication(i))

print(f"- {num} ->  {mult}")