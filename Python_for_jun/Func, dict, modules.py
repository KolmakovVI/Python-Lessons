# def sum_of_elem(a, b):
#     c = a + b
#     return c
#
#
# def min2(a, b):
#     if a >= b:
#         return a
#     elif b > a:
#         return b
#
#
# def massage(massages):
#     if massages != 0:
#         print('You have a new massage!')
#
#
# def min_any(*inp_param):
#     m = inp_param[0]
#     for i in inp_param:
#         if m > i:
#             m = i
#     return m
#
#
# def const_foo(mes=0):
#     if mes != 0:
#         print('not a zero')
#     else:
#         print('it`s zero')
#
#
# def foo2():
#     c = a + 10
#     return c
#
#
# a = 100
# d = foo2()
# print(d)

# task 1 ==========================================================================================
# Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
# f(x)={ 1−(x+2)^2, при x≤−2
#      { −x/2, при −2<x≤2
#      { (x−2)^2 + 1, при 2<x
# Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

# my decision:

# def f(x):
#     if x <= -2:
#         ans = 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         ans = -(x / 2)
#     else:
#         ans = (x - 2) ** 2 + 1
#     return ans

# best decisions:

# 1:---------------
# a and b - возвращает a если bool(a)==false, иначе возвращает b
# a or b - возвращет a если bool(a)==true, иначе возвращает b
# если убрать приведение к float, то в точке -3 функция выдаст False, а не 0.0

# def f(x):
#     return float(x < -2 and 1 - (x + 2) ** 2 or 2 < x and (x - 2) ** 2 + 1 or -2 <= x <= 2 and -x / 2)

# 2:--------------- можно использовать return, после него уже ничего в функции не будет выполняться
# def f(x):
#     if x<=-2:
#         return -(x+1)*(x+3)
#     elif 2<x:
#         return (x-2)*(x-2)+1
#     return -x/2

# 3:--------------- использует словарь, у которого ключ - Bool. Выбирает из словаря то, что true
# def f(x):
#     return {
#         x <= -2:      1 - (x + 2) ** 2,
#         -2 < x <= 2:  -x / 2,
#         2 < x:        (x - 2) ** 2 + 1
#     }[True]


# task 2 ==========================================================================================
# Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

# my decision:

# def modify_list(mod_list):
#     i = 0
#     while i != len(mod_list):
#         if mod_list[i] % 2 == 0:
#             mod_list[i] = mod_list[i] // 2
#         else:
#             # mod_list[:] = mod_list[:k] + mod_list[k + 1:]
#             mod_list.remove(mod_list[i])
#             i -= 1
#         i += 1

# best decisions:

# 1:--------------- мы копируем c с помощью [:] входящий список от начала до конца, можете представить это как буд-то
# вы выделяете все елементы списка, а потом вместо этого выделения вставляете новые элемены в тот же самый список

# def modify_list(l):
#     l[:] = [i//2 for i in l if not i % 2]

# 2:---------------for x in l[:] - перебор элементов ведём по копии списка, полученной с помощью среза, т.к. исходный
# список мы меняем прямо во время прохода, а в этом случае простой поэлементный перебор "ломается"

# def modify_list(l):
#     for x in l[:]:
#         if x % 2 == 0:
#             l.append(x//2)
#         l.remove(x)

# task 3 ==========================================================================================

# Напишите функцию update_dictionary(d, key, value), которая принимает на вход словарь d и два числа: key и value
# Если ключ key есть в словаре d, то добавьте значение value в список, который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2∗key. Если и ключа 2∗key нет, то нужно
# добавить ключ 2∗key в словарь и сопоставить ему список из переданного элемента [value].

# my decision: --------------------

# def update_dictionary(d, key, value):
#     if key in d:
#         d[key].append(value)
#     elif 2*key in d:
#         d[2*key].append(value)
#     else:
#         d[2*key] = [value]

# best decisions:

# 1:-------------- Использовали логику Bool и метод словаря get
# def update_dictionary(d, key, value):
#     key += key * (key not in d) # Использовали логику Bool - либо добавляем значение ключа, либо нет
#     d[key] = d.get(key, []) + [value]

# 2:-------------- использовали метод setdefault
# def update_dictionary(d, k, v):
#     if k in d:
#         d[k].append(v)
#     else:
#         d.setdefault(k*2, []).append(v)

# task 4 ==========================================================================================
# Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и в каком количестве используется в этой книге.
# Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова, разделённые пробелом и вывести получившуюся статистику.
# Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой
# строке число его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода).
# Порядок вывода слов может быть произвольным, каждое уникальное слово﻿ должно выводиться только один раз.

# my decision:

# your_str = input().lower().split()
# str_set = set(your_str)
# for i in str_set:
#     count = your_str.count(i)
#     print(i, count)

# best decisions:

# 1:--------------- Использование форматирования строки и лист компрехеншион
# w = input().lower().split()
# print(*['%s %s' %(x, w.count(x)) for x in set(w)], sep='\n')

# task 5 ==========================================================================================
# Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
# Далее считывает n строк с числами xi, по одному числу в каждой строке. Итого будет n+1 строк.
# При считывании числа xi программа должна на отдельной строке вывести значение f(xi).
# Функция f(x) уже реализована и доступна для вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x. Для того, чтобы уложиться в
# ограничение по времени, нужно избежать повторного вычисления значений.

# my decision:

# n = int(input())
# lst = [int(input()) for i in range(n)]
# dct = dict()
# for i in lst:
# 	if i not in dct:
# 		dct[i] = f(i)
# print(*[dct[i] for i in lst], sep='\n')


# best decisions:
# 1:--------------- использовали словарь. С помощью сет() отсекли повторения для расчета значений в словарь
# n = int(input())
# my_lst = [int(input()) for i in range(n)]
# my_dct = {x: x*x for x in set(my_lst)}
# print(*(my_dct[x] for x in my_lst), sep='\n')

# 2:--------------- создали словарь и сразу выводим значение
# cache = {}
# for _ in range(int(input())):
#     x = int(input())
#     if x not in cache: # проверяем, что х нет в словаре
#         cache[x] = f(x)
#     print(cache[x])

# task 6 ==========================================================================================
# На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
# Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
# и производит обратную операцию, получая исходный текст.
# Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
# В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

# my decision:
# lines = ''  # пустая трока, чтобы добавить в нее новые строки в цикле
# alpha = ''
# digit = '0'
# my_lst = list()
# with open('C:\\Python_tasks\\dataset_3363_2.txt') as file:
#     for l in file:
#         lines += l.strip()  # добавляет каждый цикл новую строку к старой (будет одна большая)
# for simbol in lines:
#     if simbol.isalpha():
#         my_lst += [alpha for n in range(int(digit))]
#         # print(*(alpha for n in range(int(digit))), sep='', end='')
#         digit = ''
#         alpha = simbol
#     if simbol.isdigit():
#         digit += simbol
# # print(*(alpha for n in range(int(digit))), sep='', end='')
# my_lst += [alpha for n in range(int(digit))]
# my_str = ''.join(my_lst)
#
# with open('C:\\Python_tasks\\test.txt', 'w') as write:
#     write.write(my_str)

# best decisions:
# 1:---------------

# with open('dataset_3363_2.txt', 'r') as f:
#     s = f.readline().strip()
#
# for i in range(len(s)):
#     r = 1
#     number=''
#     if s[i].isalpha():
#         while s[i+r].isdigit():
#             number += str(s[i + r])
#             r+=1
#         for _ in range(int(number)):
#             print(s[i],end='')

# 2:---------------

# import re                         ﻿# подгрузил библиотеку с регулярными выражениями, рекомендую прочитать статью
#                                   ﻿# https://tproger.ru/translations/regular-expression-python/﻿
# vyvod=''  ﻿                        # объявил пустую строку в которую в конце буду все записывать
# with open("dataset_3363_2.txt") as file:   # открываю файл
#   line = file.readline().strip()           # читаю строку
# bukvi = re.findall(r'\D', line)            # re.findall находит все сочетания до цифры и помещает их в список  в виде ('a', 'A', 'c'...) ﻿﻿
#                                            # \﻿d - ﻿Любая цифра [0-9] (\D — все, кроме цифры)﻿﻿ ﻿
# cifri = re.findall(r'\d+', line)           # \d ﻿﻿находит все сочетания цифр, а остальные пропускает, но чтобы он не
#                                            # оставлял пробелы вместо пропущенных букв написано '\d+' - где +
# ﻿                                          ﻿ # обозначает 1 и ﻿более вхождений цифр (по умолчанию, как я понял 0 и
#                                            # более вхождений)﻿  
# ﻿for i in range(len(bukvi)):                # поскольку букв и сочетаний цифр одинаковое количество, то цикл
#                                            # ﻿имеет ﻿одинаковую длину (len(bukvi)) как для цифр, так и для букв   
#     vyvod+= str(bukvi[i])*int(cifri[i])    # каждую букву записываю в ﻿строку определенное количество раз
# with open("textfile_out.txt", "w") as outfile: outfile.write(vyvod) #записываю в файл


# task 7 ==========================================================================================
# Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так интересно
# смотреть, как, например, на наиболее часто используемые.
# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
# слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
# лексикографически первое (можно использовать оператор < для строк).

# my decision:
# line = list()
#
# with open('C:\\Python_tasks\\dataset_3363_3.txt', 'r') as file:
#     for i in file:
#         line += i.lower().split()
#
# counter = 0
# big = line[0]
#
# for i in set(line):
#     curr = line.count(i)
#     if curr > counter:
#         counter = curr
#         big = i
#     elif curr == counter and i < big:
#         big = i
#
# with open('C:\\Python_tasks\\test.txt', 'w') as file:
#     file.write(big + ' ' + str(counter))


# best decisions:

# 1:----------------------------------------------------------------------------------------
# Без словаря, сразу читаем файл и сортируем список слов, чтобы потом первое найденное было лексиграфически впереди.
# with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
#     maxc = 0
#     s = inf.read().lower().strip().split()
#     s.sort()
#     for word in s:
#         counter = s.count(word)
#         if counter > maxc:
#             maxc = counter
#             result_word = word
#     ouf.write(result_word +' ' + str(maxc))

# 2:----------------------------------------------------------------------------------------
# with open('words.txt') as f:
#     text = f.read().lower().split()
# popular_word = max(set(text), key=text.count)
# print(popular_word, text.count(popular_word))

# 2:----------------------------------------------------------------------------------------
# with open('1.txt') as string:
#     s1 = string.read().replace('\n', ' ').lower().split()
# a = max(s1, key=s1.count)
# print(a, s1.count(a))

# task 8 ==========================================================================================
# Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю
# оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
# Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам.
# В качестве ответа на задание прикрепите полученный файл со средними оценками.
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']

# my decision:
# можно через словарь, где каждая фамилия - ключ
# а можно сразу при чтении каждой строки находить сумму
# а можно через map(int, i) и list comprehension
# average = list()
# with open('C:\\Python_tasks\\dataset_3363_4.txt', 'r', encoding='utf-8') as infile, \
#         open('C:\\Python_tasks\\out.txt', 'w') as outfile:
#     for i in infile:
#         lst = [float(x) for x in i.split(';')[1:]]
#         average += [lst] # сделали список из списков для каждого ученика. [[std1...],[std2...],...]
#
#     for i in average: # записываем в файл средний балл каждого ученика
#         outfile.write(str(round(sum(i) / len(i), 9)) + '\n')  # round для того, чтобы было 9 знаком после запятой
#
#     summ = 0
#     for i in range(len(average[0])): #
#         for j in range(len(average)):
#             summ += average[j][i]
#         outfile.write(str(round(summ / len(average), 9)) + '\n')
#         summ = 0

# best decisions:

# 1:--------------------------------------------------------------------------
# with open('C:\\Python_tasks\\dataset_3363_4.txt', 'r') as txt_file:
#     s_in = txt_file.readlines()
# # Формируем матрицу оценок
# s = []
# for i in range(len(s_in)):
#     s.append(list(map(int, s_in[i].strip('\n').split(';')[1:])))
#
# with open('C:\\Python_tasks\\out.txt', 'w') as txt_file:
#     # Пишем среднюю оценку каждого абитуриента
#     for i in s:
#         txt_file.write(str(sum(i) / len(i)) + '\n')
#     # Пишем средние баллы по всем абитуриентам
#     for i in range(len(s[0])):
#         score = 0
#         for j in range(len(s)):
#             score += s[j][i]
#         txt_file.write(str(score / len(s)) + ' ')

# 2:--------------------------------------------------------------------------
# st = [x.split(';') for x in open('fl.txt').readlines()]
# print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
# print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])

# task 9 ==========================================================================================
# Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран
# (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.
# Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.
# Пример работы программы:
# > python3 my_solution.py arg1 arg2
# arg1 arg2

# my decision:


# best decisions:
# 1:---------------

# task 2 ==========================================================================================

# my decision:

# best decisions:
# 1:---------------
