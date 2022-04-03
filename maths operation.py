#Program to do simple mathematical operations

print("***This is a simple calculator program***\n")
a=float(input('Enter a no. : '))
b=float(input('Enter another no. : '))
print("\n\n\tMENU")
print("\n\t1-For addition \n\t 2-For substraction \n \t 3-For multiplication \n \t 4-For division ")
c=int(input('\n\t Enter your choice :    '))

if c==1:
    print('The sum of ',a,' , ',b,' = ',a+b)
elif c==2:
    if a>b:
        print('The difference of ',a,' - ',b,' = ',a-b)
    else:
        print('The difference of ',a,' - ',b,' = ',b-a)
elif c==3:
    print('The product of ',a,' * ',b,' = ',a*b)
elif c==4:
    print('The result of ',a,' / ',b,' = ',a/b)
else:
    print("Invalid Choice!!!") 
