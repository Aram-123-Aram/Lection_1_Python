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

a = float(input('Enter the first number: a= '))
b = float(input("Enter the second number: b= "))

if a/b==b:
    print('Yes,a is the cvadrat of b ')
elif b/a==a:
    print('Yes, b is the cvadrat of a ')
else:
    print("No, a and b are not the cvadrats of each others")


