#Program to find the number of odd and even num

def even_odd_num(n):
    cte=0
    cto=0
    while n>0:
        r=n%10
        if r%2==0:   
            cte+=1
        else:
            cto+=1
        n=n//10
    print("The no. of even = ",cte,"\n The no. of odd = ",cto)


a=int(input("Enter a no. : "))
even_odd_num(a)
