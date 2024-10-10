# map(int,input().split()) - метод split разбивает строку по пробелу,
# а map применяет указанную функцию к каждому элементу последовательности.
# [int(i) for i in input().split()] - второй способ создания списка
# *a - раскрывание итерируемого объекта

# list(map(int,input().split())) - список чисел
# list(range(1, 5)) - список из чисел от 1 до 4х
# list('BEEGEEK')=['B', 'E', 'E', 'G', 'E', 'E', 'K']
# del b[2] - удалить элемент списка по индексу 2
# type() - тип
# len() - в списке это количество элементов
# [1,2,3]*3=[1,2,3,1,2,3,1,2,3]
# [1,2,3]+[3]=[1,2,3,3]
# 2 in a - присутствует ли 2 в списке а (True, False)
# sum() - сумма всех элементов
# min,max - минимальное и максимальное значение в списке


# добавить элемент в список:
# a.append() - добавить один элемент в конец списка
# a +=[1,2,3]- добавить элементы в конец списка
# если добавить строку +="1,2,3" то добавится [1],[2],[3]
# a.insert(2,100) - вставить элемент 100 на 2 позицию, сдвигая другие позиции
# Если указан недопустимый индекс, то во время выполнения программы не происходит ошибки.
# Если задан индекс за пределами конца списка, то значение будет добавлено в конец списка.
# Если применен отрицательный индекс, который указывает на недопустимую позицию,
# то значение будет вставлено в начало списка.
# a.extend(b) - добавляет в конец списка a элементы списка b или можно добавить отдельный элемент
# words1.append('python') - получим ['iq option', 'stepik', 'beegeek', 'python']
# words2.extend('python') -  получим ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']

# удалить элемент в списке:
# a.remove() - удаляет элемент, первый попавшийся подходящий элемент a[0] - удаляет первый элемент под индексом 0
# del numbers[::2] - удалить все элементы на четных позициях (0, 2, 4, ...) исходного списка.

# Сортировка:
# sorted() - сортировка, изначальный список не меняется
# sorted(a,reverse=True) - сортировка по убыванию
# a.sort() - сортирует список по возрастанию, изменяя изначальный список
# a.sort(reverse=True) - сортирует список по убыванию
# a.reverse() -  в обратном порядке список  - так же это можно сделать a[::-1]
# sor применяется только в списках
# sorted() - можно применять к любым итерабельным последовательностям(всё что можно обойти в цикле for) но вернет все равно список

# a.clear( ) - очистить
# a.copy() - копия списка
# a.count() - сколько раз значение встречается в списке
# a.index(12) - поиск 12 по индексу слева направо
# a.index(12,3) - начиная с 3го
# a.index(12,3,5) - начиная с 3го и по 5й
# (-a[:: -1] - 1).index(12) - поиск индекса справа, тип например -1,-2,-3 и т.д
# len(a) - a[:: -1].index(12) - 1 - поиск индекса справа, тип например 8,9,10 и т.д

# a.pop() или a.pop(3)- удаляет элемент и выводит на экран, по умолчанию последний

#     строковые методы(работают только со списком строк)
# a.split() - разбивает строку (по пробелам) на элементы и преобразует в список
# a.split('.')  - разбивает строку на элементы по '.'
# a.split('\\') - что бы разделить по слэшам \ - нужно ставить двойной сллэш
# ' '.join(a) - собирает элементы списка в строку разделяя их ' '
# s.split() и s.split(' ') - не одно и то же, второй вариант не уберет все пробелы, если их несколько подряд.

# *a, b, c = [1, 2, 3, 4]   - * - присваивает несколько значений (список) одной переменной
# print(*mas) - * распаковка списка в отдельные элементы
# пример:
# mas=[1,2,3, "опа"]
# print(*mas) - распакуется как 1 2 3 опа , а не ['1','2','3','опа']


#             ГЕНЕРАТОРЫ СПИСКОВ - list comprehensions:

# #[выражение for val in коллекция]
# zeros = [0 for i in range(10)] - [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# squares = [i ** 2 for i in range(1,8)] - [1, 4, 9, 16, 25, 36, 49]
# cubes = [i ** 3 for i in range(10, 21)] - Создать список, заполненный кубами целых чисел от 10 до 20 можно так:
# chars = [c for c in 'abcdefg'] - Создать список, заполненный символами строки:
# print(chars)
# lines = [input() for _ in range(int(input()))] - если сначала вводится число n – количество строк, а затем строки,
# то создать список можно так
# numbers = [int(input()) for _ in range(int(input()))] - Если требуется считать список чисел,
# a=input().split() - получаем список из строк
# a=[int(i) for i in a] - каждый элемент этого списка преобразуется в целочисленное

# Пример:
# a = [('ivanov', 2002)('Petrov', 2004)('Sidorov', 1980)]
# b = [elem[1] for elem in a if elem[0].startswith('P')] - выведет первые элементы кортежей, если его нулевой элемент начинается с 'P' = [2004]
# b = [elem[0] for elem in a if elem[1]>2000] - выведет нулевые элементы кортежей первый элемент которых больше 2000 =['ivanov', 'Petrov']
# d = [elem[0] if elem[1] > 2000 else elem[1] for elem in a] - выведет нулевые элементы кортежа, если первый элемент > 2000 в противном случае выведет первый элемент

# Пример:
# a={'ivanov':{'age': 1995, 'hobby': 'soccer', 'car': 'BMW'}, 'Petrov':{'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},'Sidorov':{'age': 1991, 'hobby': 'chess', 'car': 'BMW'}}
# b=[(elem, a[elem]['car']) for elem in a if a[elem]['age']<2000] - выведет название машины (значения ключа "car") если ворзраст меньше 2000
# и фамилию владельца(т.е ключи подходящие по условию)=[('ivanov', 'BMW'), ('Sidorov', 'BMW')]

# Пример:
# s='dfgh4356341wertgher45yhrt56745yert'
# b=[int(i) for i in s if i.isdigit()] - создаст список из цифр из переменной s

# Пример:
# import random
# a=[random.randit(-10,10) for i in range(10)] - создает список с 10 рандомными числами
# b=[abs(elem) for elem in a] - убирает все минусы
# a=[elem+1 for elem in a] - увеличиваем каждый элемент списка на 1

# #[выражение for val in коллекция if условие]
# evens = [i for i in range(21) if i % 5 == 0 or i % 3 == 0 ] - если требуется создать список кратных 3 или 5 от 0 до 20

# Матрица(вложенный списки):
# n=5
# m=4
# a=[[0]*m for i in range(n)] - создает  матрицу с 5 строками и 4 столбцами [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
# a=[[0]*n for i in range(n)] - если n=5 [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# a = [i * j for i in range(1, 5) for j in range(2)] - [0, 1, 0, 2, 0, 3, 0, 4]
# a=[(i,j) for i in 'abc' for j in [1,2,3]] - [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3), ('c', 1), ('c', 2), ('c', 3)]
# a=[i*j for i in [2,3,4,5] for j in [1,2,3] if i*j>10] - [12, 15]

# Пример:
# import random
# n=4
# m=6
# a=[[random.randit(1,6) for j in range(m)] for i in range(n)]
# for i in a:
#     print(i)  - выведет n=4 строки по m=6 случайных чисел от 1 до 6
# [6, 4, 4, 4, 2, 4]
# [1, 6, 6, 3, 4, 2]
# [2, 4, 3, 2, 5, 6]
# [2, 3, 4, 3, 2, 6]
# b=[a[i][j] for i in range(n) for j in range(m) if i==j] - список из элементов главной диагонали матрицы
# с=[a[2][j] for j in range(m)]] - список из элементов второй строки
# d=[a[i][3] for i in range(n)]] - список из элементов третьего столбика

# Пример таблица умножения:
# n=9
# m=9
# a=[[i*j for j in range(1,m+1)] for i in range(1,n+1)]
# for i in a:
#     print(i)

# генератор массива:
# a=[[0 for j in range(m)] for i in range(n)]

# Такой код:
# s = 'Python'

# print(*s)
# print()
# print(*s, sep='\n')

# выведет:

# P y t h o n

# P
# y
# t
# h
# o
# n

#             ВЫРАЖЕНИЯ-ГЕНЕРАТОРЫ - list comprehensions:
# Генератор - итератор, элементы которого можно обойти только один раз
# Итератор - объект, который поддерживает функцию next(). И помнит о том, какой элемент будет использоваться следующим
# Итерируемый объект - объект который предоставляет возможность обойти поочередно свои элементы. Может быть преобразован к итератору.
# s=[1,2,3] - итерируемый объект
# d=iter(s) - итератор
# next(d)
# b=(i**2 for i in range(1,6)) - в круглых скобках вместо квадратных
# итерация - процесс перебора элементов коллекции внутри цикла или функции, которая делает перебор
# пример:
# c=list(range(100000000)) - выражения-генератора не хранит в памяти всю информацию
# c=list(c) - преобразовать генератор к списку
# К генераторам невозможно применить индекс, функцию len()

#                 ФУНКЦИЯ ГЕНЕРАТОР - list comprehensions:
# Пример1
# def genf():
#     for i in [42,64,55]:
#         yield i # функция yield возвращает значение и замораживает вашу функцию со всеми значениями на этом месте

# #1) s=genf():

# #2) for i in genf():
#      #print(i)


# Пример2
# def genf():
#     s=7
#     for i in [42,64,55]:
#         yield i # функция yield возвращает значение и замораживает вашу функцию со всеми значениями на этом месте
#         print(s)
#         s=s*10+7

# g=genf()
# print(next(g)) #выводит 42 - первое значение i
# print(next(g)) #выводит 7 - s=7
# print(next(g)) #выводит 64 - второе значение i
# print(next(g)) #выводит 77- s=7*10+7

# функция факториала:
# def fact(n):  # Обычная функция факториала
#     pr=1
#     a=[]
#     for i in range(1,n+1):
#         pr=pr*i
#         a.append(pr)
#     return a
# print(fact(10))


# def fact(n):  # функция генератор факториала
#     pr=1
#     for i in range(1,n+1):
#         pr=pr*i
#         yield pr
# #s=fact(10)
# #print(next(s))
# #print(next(s))
# #print(next(s))
# for i in fact(10):
#     print(i, end=' ')

#                     РАСКРЫТИЕ МНОГОМЕРНОГО СПИСКА В ОДНОМЕРНЫЙ С ПОМОЩЬЮ ГЕНЕРАТОРА СПИСКОВ - list comprehensions
# new_list  = [sub_list_3 for sub_list_1 in original_list for sub_list_2 in sub_list_1 for sub_list_3 in sub_list_2]
