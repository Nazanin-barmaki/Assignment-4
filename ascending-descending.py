list = []
count = True
for i in range(10):

    print('\nEnter the number :\n')
    numbers = int(input())
    list.append(numbers)

for num in range(len(list) - 1): 

    if (list[num] < list[ num + 1]):
        count = True
        continue
    
    else:
        count = False
        break

if (count ==True):
    print('Yeah')
else:
    print('No')