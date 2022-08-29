import random
c=int(input('Enter your range : '))
list=[]
for i in range (c):
    number=random.randint(100,350)
    list.append(number)
print('your list =',list)