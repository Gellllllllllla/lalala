'''
Напишите программу, которая запрашивает у пользователя имя, а затем отображает специальное приветствие этому человеку, если его имя - Bond. Если имя, введенное пользователем это что-то другое, ваш код не должен выдавать никаких результатов.

Sample Input 1:
Bond

Sample Output 1:
Wellcome, mr. Bond!

Sample Input 2:
James

Sample Output 2:

'''
name = str(input())
print(name)
if name == "Bond":
    print("Wellcome, mr. Bond!")
else:
    print("")
    
