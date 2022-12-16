#a = int(input("Enter the a= "))
#if a % 3 == 0:
#   print("Yes")
#else:
#    print("No")

# Написать программу,который на вход принимает 2 числа и проверяет,
# являеться ли одно число квадратом другого.

#a = int(input('Enter the first number: a= '))
#b = int(input('Enter the second number: b= '))
#
#if a/b == b or b/a == a:
#    print('Yes')
#else:
#    print('No')

#Написать программу,который на вход принимает 5 чисель и находит из них max.

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет
'''
a = float(input('Enter the first number: a= '))
b = float(input("Enter the second number: b= "))

if a/b==b:
    print('Yes,a is the cvadrat of b ')
elif b/a==a:
    print('Yes, b is the cvadrat of a ')
else:
    print("No, a and b are not the cvadrats of each others")
'''

# write a program,that showes is the entering number 'cratno' 3?
'''
a = int(input('Enter the number a= '))

if a % 3 ==0:
    print('Yes the number a "Cratno" 3!')
else:
    c = a % 3
    print(f"No,the number a is not 'Cratno' 3! and ostatok ot deleni = {c}")
'''
# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
#Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет

a = int(input('Enter the first number a= '))
b = int(input("Enter the second number b= "))
'''
def Cvadrat(m, n):
    if a == b**2 or b == a**2:
        return print('Yes')
    else:
        return print('No')
Cvadrat(a, b)
'''
'''
def Cvadrat(m, n):
    if m == n*n or n == m*m:
        print("Yes")
    else:
        print("No")
Cvadrat(a,b)
'''
if a == b**2:
    print("Yes, a is Cvadrat b")
elif b == a**2:
    print("Yes, b is Cvadrat a")
else:
    print("No, no a nor b are not Cvadrat each others")


