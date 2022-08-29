number = int(input('please Enter integer number: '))
factorial = number
for i in range(1,number-1):
     factorial = factorial / i 
     
if factorial==1:
        c=True
      

else:
        c=False
if c==True:
    print('Yes, the given number is the factorial of another number')
else:
    print('no the given number is not a factorial of another number')