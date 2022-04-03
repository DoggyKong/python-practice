#program for conditional operator demonstration

##a=int(input('No. : '))
##b=int(input('No. : '))
##c=a if a>b else b
##print(c)

x=lambda a,b: a*b
print(x(2,3))

y=lambda :print('this is an example of lambda function')
y()
