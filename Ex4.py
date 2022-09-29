# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

from random import randint
from xml.dom.minidom import Element


n = int(input('Введите число N = '))
list = []
for i in range(2*n+1):
    list.append(randint(-n,n))
print(list)
elem1 = list[int(input('Введеите индекс первого элемента элемента = '))]
elem2 = list[int(input('Введеите индекс второго элемента элемента = '))]
multi = elem1*elem2
print(f"Произведение элеентов по заданным индексам = {multi}")
