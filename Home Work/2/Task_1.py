# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

def SumNumber(n):
    sum = 0
    while n != int(n):
        n *= 10
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

print('Введите число: ')
num = float(input())
print(f"Сумма цифр = {SumNumber(num)}")


print(sum(map(int, list(input("Введите дробное число: ").replace(".", "")))))