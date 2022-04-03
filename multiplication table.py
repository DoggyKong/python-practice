#Program to find the multiplication table

def table(n):
    for i in range(1,11):
        print(n,' x ',i,' = {:10.2f}'.format(n*i))

r=1        
while r>0:
    g=int(input('Enter 1 for continuation \nEnter 2 to stop : '))
    if g==1:
        p=float(input('Enter the no. for which the multiplication table will be shown : '))
        v=table(p)
    elif g==2:
        print('****It is stopped as you command*****')
        break
    else:
        print('****Entered option not found**** ')
          
