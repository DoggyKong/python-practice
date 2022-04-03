

def multiple(n):
    return n*1,n*2,n*3
        

a=int(input('Enter a value : '))
c=multiple(a)
t=list(c)
t.append(6)
tup=tuple(t)

print(tup,sep='; ')
print(type(tup))
