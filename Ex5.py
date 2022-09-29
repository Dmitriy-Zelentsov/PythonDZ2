# Реализуйте алгоритм перемешивания списка.
import random
n = int(input('Введите число N = '))
list = []
for i in range(1, n+1):
    list.append(i)
print(list)
random.shuffle(list)
print(list)
