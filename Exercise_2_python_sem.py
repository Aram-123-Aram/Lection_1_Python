 # Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них. 
 # Примеры:
 # 1, 4, 8, 7, 5 -> 8
 # 78, 55, 36, 90, 2 -> 90 

list = [78, 55, 36, 90, 2]
'''
max = list[0]
for i in list:
    if i>max:
        max = i
print(max)
'''
max = list[0]
i = 1
while i < len(list):
    if list[i]>max:
        max = list[i]
    i+=1
print(max)
    

