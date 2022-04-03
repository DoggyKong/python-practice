#program to perform binary search

def binary_search(lis,start,stop,key):
    if stop>=start:
        mid=(start+stop)//2
        if lis[mid]==key:
            return mid
        elif lis[mid]>key:
            return binary_search(lis,start,mid-1,key)
        else:
            return binary_search(lis,mid+1,stop,key)
    else:
        return -1

def binary(lis,start,stop,key):
    while start<=stop:
        mid=(start+stop)//2
        if lis[mid]==key:
            return mid
        elif lis[mid]>key:
            stop=mid-1
        else:
            start=mid+1
    return -1

lis=[1,2,3,4,5,6,7,8,9,10,11,12]
while True:
    try:
        print('\nThe given list is\t',lis)
        key=int(input('\nEnter the item to be search : '))
        result=binary(lis,0,len(lis)-1,key)
        if result==-1:
            print('\nITEM NOT FOUND IN THE GIVEN LIST')
        else:
            print('\nITEM FOUND AT INDEX',result,'AND POSITION',result+1)
        ch=input('\nDo you want to try again(y/n)? ')
        if ch in 'yY':
            continue
        else:
            break
    except:
        print('\nINVALID CHOICE')
        exit()




                
        
