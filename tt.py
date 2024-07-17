num1=int(input('enter a first number'))
num2=int(input('enter a second number'))
num3=int(input('enter a thrid number'))

if num1 > num2 and num1> num3:
    print(f'num1{num1}')
elif num2 >num3 and num2 >num1:
    print(f'num 2{num2}')
elif num3 >num2 and num3 >num1:
    print(f'num3{num3}')
else:
    print('there are two equal number')
    