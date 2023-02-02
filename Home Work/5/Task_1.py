# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв авб
# бав вба бав вба

# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1
# out
# The data is incorrect

text = input("Введите текст через пробел \n")
find_text = "абв"
new_list = [i for i in text.split() if find_text not in i] # split разбивает строку на части, используя специальный разделитель, и возвращает эти части в виде списка
print(" ".join(new_list))