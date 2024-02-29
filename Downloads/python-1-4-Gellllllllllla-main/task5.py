'''
Напишите программу, которая считывает целое число n и вычисляет значение
выражения: n + nn + nnn

Sample Input 1:
5 + 55 + 555

Sample Output 1:
615

Sample Input 1:
10

10 + 1010 + 101010

Sample Output 1:
102030
'''

n = input()

print(int(n) + int(11 * n) + int(111 *n))
      
