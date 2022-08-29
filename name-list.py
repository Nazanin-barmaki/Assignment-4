names_lst = int(input("enter the number of names you want: "))
for i in range(names_lst):
    name_input = input("enter the name you want: ")
    names_lst.append(name_input)
    print(names_lst)
names_collc = []
for name in names_lst:
    if name in names_collc:
        continue
 
else:
    names_collc.append(name)
    
for name in names_collc:
    counter = 0
    for item in names_lst:
        if name == item:
            counter += 1
    print(f'{counter}\t{name}')

    



