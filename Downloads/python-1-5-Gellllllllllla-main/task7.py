'''
Напишите программу, которая принимает число от пользователя и определяет, число положительное, отрицательное или ноль.

Sample Input 1:
0

Sample Output 1:
ноль

Sample Input 2:
-5

Sample Output 2:
отрицательное

Sample Input 3:
5

Sample Output 3:
положительное
'''
a = int(input())
print(a)

if a > 0:
    print("положительное")
elif a < 0:
    print("отрицательное")
elif a == 0:
    print("ноль")
    