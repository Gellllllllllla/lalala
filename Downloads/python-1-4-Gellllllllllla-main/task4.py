'''
Напишите программу, которая вычисляет площадь круга с заданным пользователем 
радиусом.

Sample Input 1:
1.1

Sample Output 1:
3.8013271108436504
'''
 #import math 

 # print(math.pi)

from math import pi

r = float(input())

print (pi * r ** 2)