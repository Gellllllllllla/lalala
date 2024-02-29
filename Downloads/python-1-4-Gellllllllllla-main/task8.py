'''
Напишите программу, которая считывает 3 строки с именами одним вызовом функции 
input() и выводит их в обратном порядке.

Sample Input 1:
Вася
Петя
Толя

Sample Output 1:
Толя
Петя
Вася
'''
text = ''
for i in range(3):
    text += input() + ' '
x = text.split()
print("\n".join(x[::-1]))
