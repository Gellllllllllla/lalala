'''
Напишите программу, которая принимает на вход 3 длины сторон треугольника
и вычисляет площадь треугольника по формуле Герона.
'''
from math import sqrt
s = list(map(int, input().split()))
p = sum(s) / 2

print(sqrt(p * (p - s[0]) * (p - s[1]) * (p - s[2])))
