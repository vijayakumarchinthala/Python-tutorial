# FUnctions
def l_s(ar,item):
    i=0
    while i < len(ar) and ar[i]!=item :
        i+=1
    if i< len(ar):
        return i
    else:
        return False
def b_s(ar,item):
    beg=0
    last=len(ar)-1
    while(beg<=last):
        mid= (beg+last)//2
        if (item == ar[mid]):
            return mid
        elif (item >ar[mid]):
            beg=mid+1
        else:
            last= mid-1
    else:
        return False          #when item not found
def Findpos(ar,item):
    size=len(ar)
    if item<ar[0]:
        return 0
    else:
        pos=-1
        for i in range (size-1):
            if (ar[i]<=item and item < ar[i+1]):
                pos=i+1
                break
            if (pos==-1 and i<=size-1):
                pos = size
        return pos
def shift(ar,pos):
    ar.append(None) # add an empty element at an end
    size = len(ar)
    i=size-1
    while i>=pos:
        ar[i]=ar[i-1]
        i=i-1
def s_sort(liste):
    for curpos in range(len(liste)):
        minpos=curpos  #starting with current position
        for scanpos in range(curpos+1,len(liste)):
            if liste[scanpos]<liste[minpos]:
                minpos=scanpos
        #Swap the two values
        temp=liste[minpos]
        liste[minpos]=liste[curpos]
        liste[curpos]=temp
def swapelements(list):
    i=0
    while (i<len(list)-1):
        if (list[i]>list[i+1]):
            temp=list[i]
            list[i]=list[i+1]
            list[i+1]=temp
        i=i+1
        #print " List after pass",(i), ":",list
def b_sort(list):
    for num in range(len(list)-1):
        pass
    swapelements(list)
def i_sort(ar):
    for i in range(1,len(ar)):
        v=ar[i]
        j=i
        while ar[j-1]> v and j>=1:
            ar[j]=ar[j-1]
            j-=1
        #Insert the value at its correct postion
        ar[j]=v
def traverse(ar):
    size =len(ar)
    for i in range(size):
        print (ar[i],)
def isempty(stk):
    if stk==[]:
        return True
    else:
        return False
def push(stk,item):
    stk.append(item)
    top=len(stk)-1
def pop(stk):
    if isempty(stk):
        return "under flow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item
def peek(stk):
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
    return stk[top]
def display (stk):
    if isempty(stk):
        print("stack empty")
    else:
        top=len(stk)-1
        print(stk[top])
        for i in range(top-1,-1,-1):
            print(stk[i])
def cls():
    print("\n"*100)
def isempty(qu):
    if qu==[]:
        return True
    else:
        return False
def enqueue(qu,item):
    qu.append(item)
    if len(qu)==1:
        front=rear=0
    else:
        rear =len(qu)-1
def dequeue(qu):
    if isempty(qu):
        return "Underflow"
    else:
        item=qu.pop(0)
        if len(qu)>0:
            front=rear=0
            return qu[front]
def peek(qu):
    if isempty(qu):
        return "Underflow"
    else:
        front=0
    return qu[front]
def display(qu):
    if isempty(qu):
        print("Queue Empty!")
    elif len(qu) ==1:
        print(qu[0],"<== front,rear")
    else:
        front=0
        rear=len(qu)-1
        print(qu[front],"<-front")
        for a in range(1,rear):
            print(qu[a])
            print(qu[rear],"<-rear")
def s():
    print ("-------------------------------------------------------------------------------")
def quiz():
    print("Welcome to python quiz!!!!!!!!")
    count=0
    count1=0
    a=input("1.Strings are immutable in Python, which means a string cannot be modified.\n a)True \n b)False\n Your answer:")
    if a=="a":
        count+=1
    else:
        count1+=1
    b=input("2.Which keyword is used for function?\n a)Fun\n b)Define\n c)Def\n d)Function\n Your answer:")
    if b=="c":
        count+=1
    else:
        count1+=1
    c=input("3.What will be the output of the following Python code?\ni = 2\nwhile True:\n    if i%3 == 0:\n        break\n    print(i)\n    i += 2\n a)2 4 6 8 10 …\n b)2 4\n c)2 3\n d)error\n Your answer:")
    if c=="b":
        count+=1
    else:
        count1+=1
    d=input("4.What is the output of the following print() function\n print(sep='--', 'Ben', 25, 'California')\n a)Syntax Error\n b)Ben–25–California\n c)Ben 25 California\n d)None of these\n Your answer:")
    if d=="a":
        count+=1
    else:
        count1+=1
    e=input("5.The term Push and Pop is related to...?\n a)Queue\n b)Stack\n c)Both\n d)None\n Your answer:")
    if e=="b":
        count+=1
    else:
        count1+=1
    f=input("6.Linear search(recursive) algorithm used  _____________\n a)When the size of the dataset is low\n b)When the size of the dataset is large\n c)When the dataset is unordered\n d)Never used\n Your answer:")
    if f=="a":
        count+=1
    else:
        count1+=1
    g=input("7. A data structure in which elements can be inserted or deleted at/from both ends but not in the middle is?\n a)Queue\n b)Circular queue\n c)Dequeue\n d)Priority queue\n Your answer:")
    if g=="c":
        count+=1
    else:
        count1+=1
    h=input("8.What is the default value for a function that does not return any value explicity?\n (a)None\n (b)int\n (c)double\n (d)null\n Your answer:")
    if h=="a":
        count+=1
    else:
        count1+=1
    i=input("9.Information stored on a storage device with a specific name is called a _______?\n (a)array\n (b)dictionary\n (c)file\n (d)tuple\n Your answer:")
    if i=="c":
        count+=1
    else:
        count1+=1
    j=input("10. Which block lets you test a block of code for errors?\n a)try \n b)except \n c)finally \n d)None of the above\n Your answer:")
    if j=="a":
        count+=1
    else:
        count1+=1
    print("Your number of correct  and incorrect answers are:Correct(",count,"),incorrect(",count1,")")

import pickle
import sys
dict1={}
def display():
    file=open("student.dat","rb")
    try:
        while True:
            student=pickle.load(file)
            print(student)
    except EOFError:
        pass
    file.close()

def write_in_file():
    print("1 Login ")
    print("2.sign up ")
    x=int(input("enter your choice(1-2):"))
    if x==1:
        name=input("Enter the user name:")
        password=input("Enter the user password:")
        file=open("student.dat","rb")
        for line in file:
            found=0
            data=pickle.load(file)
            print(data)
            if name ==data["name"] and password ==data["password"]:
                print("Correct credentials!")
                print(" Welcome to python tutorial ",name,"!!!!!!!!")
                return True
            else:
                print("Incorrect credentials.")
                return False
        
        
            
                      
    else:
        file=open("student.dat","ab")
        dict1["name"]=input(" Enter the name :")
        dict1["password"]=input(" Enter the password:")
        dict1["class"]=int(input(" Enter the class you study:"))
        dict1["gender"]=input(" Enter the gender :")
        pickle.dump(dict,file)
        print(" Welcome to python tutorial ",dict1["name"],"!!!!!!!!")
        file.close()
        
    
