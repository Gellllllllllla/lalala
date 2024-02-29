'''
Напишите программу:

Тимофей обычно спит ночью X часов и устраивает себе днем тихий час на Y минут. 
Определите, сколько всего минут Тимофей спит в сутки.

Внимание, программа принимает значения X и Y из стандартного потока ввода 
(функция input), результат надо выводить в стандартный поток вывода (функция 
print). Обратите внимание на то, что приглашение, переданное в качестве 
аргумента в функцию input, считается выводом вашей программы. 
Используйте эту функцию без аргументов:

values = input()  # без строки приглашения!

Sample Input 1:
7
30

Sample Output 1:
450

'''
x = int(input())
y = int(input())

print(x * 60 + y)

