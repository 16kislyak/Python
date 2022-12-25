# 2. Напишите программу для проверки ложности утверждения
# (W ⋀ Z) ⋁ ¬Y ⋁ (¬X ≡ ¬W) для всех значений предикат.

# print("x y z w")
# for x in range(2):
#    for y in range(2):
#        for z in range(2):
#           for w in range(2):
#                if not ((w and z) or (not y) or ( not x == w)):
#                    print(x, y, z, w)

def inputNumbers(x):
    xyzw = ["X", "Y", "Z", "W"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyzw[i]}: "))
    return a

def checkPredicate(x):
    result = (x[3] and x[2]) or (not x[1]) or (x[1] == x[2])
    return result

statement = inputNumbers(4)
if checkPredicate(statement) == False:
    print("Утверждение ложно")
else:
    print("Утверждение истинно")
