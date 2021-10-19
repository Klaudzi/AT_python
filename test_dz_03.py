# 6. Удалить все элементы с заданным значением, если они имеются в списке.
import random

n = int(input("Введите количество элементов в списке: \n"))
A=[]
for i in range(n):
    a = random.randint(1,10)
    A.append(a)
print("Наш список состоит : ")
print(A)
z = int(input("Что удалим (указываем в диапазоне от 0 до 10!!): \n"))
B = []
if (z <= 0) or (z >= 10):
    print("Такого числа нет в списке!")
else:
    for i in range(n):
        if A[i] != z:
            B.append(A[i])
    print("Новый список : ")
    print(B)




