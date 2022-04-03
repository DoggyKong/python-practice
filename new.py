import csv
def Create():
    with open("file1.csv",'w',newline=' ') as f:
        cv = csv.writer(f,delimiter =',')
        cv.writerow(['Rollno','Name','Marks'])
        cv.writerow([1,'one',100])
        cv.writerow([2,'two',90])
        cv.writerow([3,'three',70])
def Append():
    with open("file1.csv",'a',newline=" ") as f:
        cv = csv.writer(f,delimiter =',')
        while True:
            rno=int(input("enter the rollno"))
            name=input("enter the name")
            marks=int(input("enter the mark"))
            cv.writerow([rno,name,marks])
            ch=input("do you want to continue Y/N")
            if ch in "nN":
                break
            
        
def Read():
    with open("file1.csv",'r') as f:
        cv=csv.reader(f,delimiter =',')
        #print(type(cv))
        for c in cv:
            print(c)
            #print(type(c))
            #for i in c:
                
Create()
Read()
#print("Appending into the file")
#Append()
#Read()
