#Program to find max nad min in a list

def min_max(lis):
    l=len(lis)
    max=lis[0]
    min=lis[0]
    for i in range(0,l):
        if max<lis[i]:
            max=lis[i]
        elif min>lis[i]:
            min=lis[i]
    return min,max


a,b=min_max([12,23,34,15,26,78,89,90,99,11])
print('Minimum = ',a,'\nMaximum = ',b)
