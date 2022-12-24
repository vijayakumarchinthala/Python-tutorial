("""This  mini project is created to teach new begineers how to program and
learn about python program """)
try:
    from FUNCTIONS import *
except ImportError:
    print("Module Not imported")

# MAIN
con=True
while con:
    print("****************           HARI OM                          ******************")
    print("************************************************************************************")
    print( " ")
    print( "                            GVK CHINMAYA VIDYALAYA                                            ")
    print( "TEAM MEMBERS:                                                                   ")
    print("CH.SAI CHARITHA REDDY                                               ")
    print("V.REVATHI                                                           ")
    print(" ")
    print("************************************************************************************")
    print(" ")
    print("************************************************************************************")
    print( " ")
    print( "                                 PYTHON TUTORIAL                                ")
    print(" ")
    print("************************************************************************************")
    print(" ")
    print(" Welcome to python tutorial!!!!!!!!")
    write_in_file()
    print( " ")
    print("  1. GET STARTED with PYTHON")
    print("  2. ABOUT PYTHON AND PROJECT")
    print("  3. EXIT")
    try:
        i1=int(input("enter your choice(1-3):"))
    except IOError:
        print(" No Input!")
        print( " ")
        print("PROGRAM WILL RESTART")
    if i1==1:
        con2=True
        while con2:
            print(" Lets start with python")
            print("Choose anyone of the module to start")
            print(" 1. Working with Srings")
            print(" 2. Simple Input and Output Statements")
            print(" 3. Python Functions and Modules")
            print(" 4. Loops in Python")
            print(" 5. Data Types and Usage")
            print(" 6. Linear list Manipulation")
            print(" 7. Stacks and Queues")
            print(" 8. Data File Handiling")
            print(" 9. Exception handiling and Generators in python")
            print("10. Get back to main menu")
            print(" *********************************************************************** ")
            try:
                i2=int(input("Enter your choice(1-10): "))
            except IOError:
                print (" No input given")
            if i2==1: # String OPerations
                con3=True
                while con3:
                    print( "Strings :-A data type are any number of valid characters into a set of quotion marks.")
                    print("Operations that can be performed with string are::")
                    print("1.Traversing of string")
                    print("2.String opeartors  on string")
                    print("3.String Functions")
                    print("4.Slicing a string")
                    print("5.Get Back to previous menu")
                    print(" ***************************************************************** ")
                    try:
                        i3=int(input("Enter your choice(1-5):"))
                    except IOError:
                        print("No input given")
                    if i3==1:
                        print("Travesing refers to iterating through the elements of a string at a time")
                        print( "Traversing can be performed in a following way")
                        a=("Python")
                        print(">>>a='Python'")
                        print(">>>for i in a:")
                        print( "      print (i,'-')") 
                        print("_______________")
                        for i in a :
                            print (i,"-",)
                        print()
                        print(" *********************************************************************** ")
                    elif i3==2:
                        print( "String operators are")
                        print("1.String Concatenation operator (+):")
                        print("  eg.")
                        print("     'ram' + 'shayam'")
                        print( "  will result into")
                        print("     'ramshayam' ")
                        print("2. String replication operator  (*):")
                        print("  eg.")
                        print( "     'DSS'*3")
                        print( "  will result into ")
                        print("     'DSSDSSDSS'")
                        print("3. Mermbership operator:")
                        print("in : Returns True if sub string  exist in given string, otherwise False")
                        print( "not in: Returns True if sub string   not exist in given string, oterwise False")
                        print(" eg.")
                        print( "   >>> 'a' in 'ram'")
                        print( "       True")
                        print("   >>> 'a' not in 'ram'")
                        print("4.Comparison operator(<,>,>=,<=,==,!=):")
                        print(" eg.")
                        print("   'a'=='a' will give True")
                        print("   'a'=='b' will give False")
                        print(" *********************************************************************** ")
                    elif i3==3:
                        q=open(r"S_FUN.txt","r")
                        w=q.read()
                        print( w)
                        del q,w
                        print(" *********************************************************************** ")
                    elif i3==4:
                        print("String slice refers to  part of a string  conting some contiguous characters.\nWhere strings are sliced using a range of indices.")
                        print("Slicing a string can be performed  as follow,")
                        print("")
                        print(">>a=ramayan")
                        a='ramayan'
                        print(">>>print a[0:3]")
                        print("  ",a[0:3])
                        print(" *********************************************************************** ")
                    elif i3==5:
                        con3=False
                    else:
                        print("INvalid input !!!!!!!!!!!")
            elif i2==2:   #Simple I/O Statement
                print("Simple input and output statement can be given by using")
                print("1. For input :")
                print("  1.input() and")
                print("  2.#raw_input()")
                print("  Following are sample programs to illustrate")
                print("    eg.")
                print("       >>> a=input('Enter your  number:' )")
                print("           Enter your number: 25")
                print("    eg.")
                print("       >>> b=#raw_input('Enter your  number:' )")
                print("           Enter your number: 25")
                print("2.For output Python use 'print' key word")
                print("")
                print(">>>For i in 'Python':")
                print("      print i    ")        # print is output keyword
                print("   Output will be as")
                print("   P \n   y\n   t\n   h\n   o\n   n\n")
                print(" *********************************************************************** ")
            elif i2==3: # FUNctions and modules
                 con4=True
                 while con4:
                     print("Python offers 3 type of Functions")
                     print("1.In-built functions")
                     print("2.Function defined in Modules")
                     print("3.User  defined functions")
                     print("4.Get back to previous menu")
                     print(" *********************************************************************** ")
                     try:
                         i4=int(input("Enter your choice(1-4):"))
                     except IOError:
                         print("No input provided")
                     if i4==1:
                        print("____________________ In-Bulit Functions___________________")
                        print("Python offers some predefined functions which are always availabel to use")
                        print( " eg. len(),type(),int()")
                        print(">>> a=Python")
                        print(">>>len(a)")
                        print("6")
                        print(" *********************************************************************** ")
                     elif i4==2:
                         q=open("M_FUN.txt")
                         w=q.read()
                         print (w)
                         q.close()
                         del q,w
                         print(" *********************************************************************** ")
                     elif i4==3:
                         print("____________________ User Defined Functions___________________")
                         print("These are the functions defined by programmer.And can be defined using 'def' keyword. ")
                         print("How to create a function is illustrated in following eample")
                         print("def sum(x,y):")
                         print("    r= x+y")
                         print("    return r")
                         print("a=input('Enter number1:')")
                         print("b=input('Enter number 2:)")
                         print("c=sum(a,b)")
                         print("print c")
                         print(" *********************************************************************** ")
                     elif i4==4:
                         con4=False       
                     else:
                         print( "Invalid input")
            elif i2==4:
                con5=True
                while con5:
                    print("Python offers  2  type of loop statement")
                    print("1. The for loop")
                    print("2. The while loop")
                    print("3. Get back to previous menu")
                    print(" *********************************************************************** ")
                    try:
                        i4=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print( "No input provided ")
                    if i4==1:
                        print("____________________ For Loop___________________")
                        print("A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).")
                        print("The general form of 'for loop' is as given below:")
                        print(" for <variable> in <sequence> :")
                        print("     statements_to_repeat")
                        print("eg.")
                        print("    for element in [10,15,20,25]:")
                        print("        print (element +2),")
                        print("Or for loop can be also used wiht range()function")
                        print("eg.")
                        print("   for val in range(3,10):")
                        print("      print val")
                        print(" *********************************************************************** ")

                    elif i4==2:
                        print("____________________ While Loop___________________")
                        print("With the while loop we can execute a set of statements as long as a condition is true.")
                        print("The general form of while loop is given below")
                        print(" while <logicalExpression>:")
                        print("    loop-body")
                        print(" *********************************************************************** ")

                    elif i4==3:
                        con5=False
                    else:
                        print("Invalid Input")
            elif i2==5:
                try:
                    e=open("D_T.txt")
                    w=e.read()
                    print (w)
                    print(" *********************************************************************** ")
                except EOFError:
                    print("Error in file opening")
                del e,w
            elif i2==6:
                con6=True
                while con6:
                    print(" Basic operations on Linear list")
                    print("1.Searching")
                    print("2.Insertion")
                    print("3.Deletion")
                    print("4.Traversal")
                    print("5.Sorting")
                    print("6.Return to previous menu")
                    print(" *********************************************************************** ")
                    try:
                        i6=int(input("Enter your choice(1-6):"))
                    except:
                        print(" InputError!!!!")
                    if i6==1:
                        con7=True
                        while True:
                            print("Python offers 2 type of common searching technique")
                            print("1.Linear search")
                            print("2.Binary search")
                            print("3.Return to previous menu")
                            print(" *********************************************************************** ")
                            try:
                                i7=int(input("Enter your choice(1-3):"))
                            except IOError:
                                print("Input error")
                            if i7==1:
                                print("__________________Linear search_______________")
                                print("In linear search each element of array?linear list is compared with the given Item to be searched for, one by one.")
                                print("This method, which traverses the array/linear list sequentially to locate the given ITEM,")
                                print("is called LINEAR SEARCH or SEQUENTIAL SEARCH ")
                                print("Following program is the example of linear search")
                                fh=open("l_search.txt")
                                print(fh.read())
                                print("Please run the following program of linear search")
                                n=int(input("Enter desired linearlist(max.50).."))
                                print("\nEnter elements for linear list\n")
                                ar=[0]*n  # initialise list of size n with zeros
                                for i in range(n):
                                    ar[i]=int(input("Element" +str(i+1) +":"))
                                item=int(input("\nENter element to be searched for..."))
                                index = l_s(ar,item)
                                if index :
                                    print("\nElement found at index:",index,",position:",(index+1))
                                else:
                                    print("\nSorry!! Givn element not found\n")
                                print(" *********************************************************************** ")
                            elif i7==2:
                                print("___________________Binary search_______________")
                                print("A binary search is an algorithm to find a particular element in the list.")
                                print(" Binary search can work for any sorted array while linear search can work for both sorted as well as unsorted array")
                                print("Following program is the example of Binary search")
                                fh=open("b_search.txt")
                                print(fh.read())
                                print("Please run the following program of binary search")
                                n=int(input("Enter desired linear-list size(max. 50).."))
                                ar=[0]*n
                                for i in range(n):
                                    ar[i]=int(input("Element"+str(i+1)+":"))
                                s_sort(ar)
                                print("\List after sorting",ar)
                                item=int(input("\nEnter Element to be searched for..."))
                                index=b_s(ar,item)
                                if index :
                                    print("\nElement found at index:",index,",position:",(index+1))
                                else:
                                    print("\nSorry!! Givn element not found\n")
                                print(" *********************************************************************** ")
                            elif i7==3:
                                break
                            else:
                                print(" Invalid input")
                    elif i6==2:
                        print("_________________Insertion in a list______________")
                        print("Insertion of new element in an array can be doone in two ways:")
                        print("(i)if the array is unordered,the new element is inserted at the end of the array.")
                        print("(ii)if the array is sorted,then new element is added at the appropriate position.")
                        print("Following program is the example of insertion in a list")
                        fh=open("insertion.txt")
                        print(fh.read())
                        print("Please run the following program of insertion of an element in linear list")
                        n=int(input("Enter desired linear-list size(max. 50).."))
                        ar=[0]*n
                        for i in range(n):
                            ar[i]=int(input("Element"+str(i+1)+":"))
                        s_sort(ar)
                        print("List in sorted order is",ar)
                        item=int(input("Enetr new element to be inserted:"))
                        position=Findpos(ar,item)
                        shift(ar,position)
                        ar[position]=item
                        print("The list after insertng",item,"is")
                        print(ar)
                        print(" *********************************************************************** ")
                    elif i6==3:
                        print("______________Deletion in a list____________________")
                        print("The element to be deleted is first searched for in the array using searching techniques.")
                        print("If the search is successful,then the element is removed.")
                        print("Following program is the example of deletion in a list")
                        fh=open("deletion.txt")
                        print(fh.read())
                        print("Please run the following program of deletion of an element in linear list")
                        n=int(input("Enter desired linear-list size(max. 50).."))
                        ar=[0]*n
                        for i in range(n):
                            ar[i]=int(input("Element"+str(i+1)+":"))
                        s_sort(ar)
                        print( "List in sorted order is",ar)
                        item=int(input("Enter new element to be deleted:"))
                        position=(b_s(ar,item))
                        if position:
                            del ar[position]
                            print("The list after deletion",item,"is")
                            print(ar)
                        else:
                            print ("SORRY! No such element in the list")
                        print(" *********************************************************************** ")
                    elif i6==4:
                        print("____________ Traversal of list_____________________")
                        print("Traversal in one dimensional arrays involves processing of all elements by","one by one",".")
                        print("Following program is the example of deletion in a list")
                        fh=open("traversal.txt")
                        print(fh.read())
                        print("Please run the following program of traversal in linear list")
                        print(" *********************************************************************** ")
                    elif i6==5:
                        while True:
                            print("Python offers 3 type of common sorting technique")
                            print("1.Selection sort")
                            print("2.Bubble sort")
                            print("3.Insertion sort")
                            print("4.Return to previous menu")
                            print(" *********************************************************************** ")
                            try:
                                i7=int(input("Enter your choice(1-4):"))
                            except IOError:
                                print ("Input error")
                            if i7==1:
                                print( "_______________________Selection sort____________________________")
                                print()
                                print(" The basic idea of selection sort is to repeadily select the smallest key in remaining us sorted array")
                                print(" The following program is the example of selection sort")
                                fh=open("s_s.txt")
                                print(fh.read())
                                print("Please run the following program of the sorting by Selection sort")
                                n=int(input("Enter desired linear-list size(max. 50).."))
                                ar=[0]*n
                                print ("Enter element for the  linear list")
                                for i in range(n):
                                    ar[i]=int(input("Element"+str(i+1)+":"))
                                print("Original list is:",ar)
                                s_sort(ar)
                                print("List after sorting:",ar)
                                print(" *********************************************************************** ")
                            elif i7==2:
                                print("______________________Bubble sort__________________________________")
                                print()
                                print("The basic idea of bubble sort is  to compare two adjoining values and exchange them if they are not in proper order.")
                                print(" The following program is the example of Bubble sort")
                                fh=open("b_s.txt")
                                print(fh.read())
                                print("Please run the following program of the sorting by Bubble sort")
                                n=int(input("Enter desired linear-list size(max. 50).."))
                                ar=[0]*n
                                print("Enter element for the  linear list")
                                for i in range(n):
                                    ar[i]=int(input("Element"+str(i+1)+":"))
                                print("Original list is:",ar)
                                b_sort(ar)
                                print("List after sorting:",ar)
                                print(" *********************************************************************** ")
                            elif i7==3:
                                print("______________________Insertion sort__________________________________")
                                print()
                                print("Suppose an array A wuth n elements a[1],A[2],...,A[N} is in memory.The insertion sort algorithm scans A from A[1]to A[N],insertion each element A[K]into is proper position in the previousy sorted sub array A[1],A[2]...,A[K-1].")
                                print(" The following program is the example of Insertion sort")
                                fh=open("i_s.txt")
                                print(fh.read())
                                print("Please run the following program of the sorting by Insertion sort")
                                n=int(input("Enter desired linear-list size(max. 50).."))
                                ar=[0]*n
                                print("Enter element for the  linear list")
                                for i in range(n):
                                    ar[i]=int(input("Element"+str(i+1)+":"))
                                print("Original list is:",ar)
                                i_sort(ar)
                                print("List after sorting:",ar)
                                print(" *********************************************************************** ")
                            elif i7==4:
                                break
                        else :
                            print("Invalid input!!!!")
                            
                            
                        
                    elif i6==6:
                        con6=False
                    else:
                        print("Invalid Input")
                        
            elif i2==7:
                con8=True
                while True:
                    print("1.Stacks")
                    print("2.Queues")
                    print("3.Return to previous menu")
                    print(" *********************************************************************** ")
                    try:
                        i7=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print("Input error")
                    if i7==1:
                        print("Stack is a linear data structure which follows a particular order in which the operations are performed.")
                        print("The order may be LIFO(Last In First Out) or FILO(First In Last Out).")
                        print("The following functions are stack operations")
                        print("stack operations")
                        print("1.push:Adds the value at end of the list.")
                        print("2.pop:Removes the value which is at end of the list.")
                        print("3.peek:It is referred as inspection.")

                        ###############STACK IMPLEMENTAION ###################
                        """
                           Stack:implemented as a list
                           top:Integer having topmost elemenet in a stack
                        """
                        print(" The following program is the example of how stack operations are implemented.")
                        fh=open("stack.txt")
                        print(fh.read())
                        print("Please run the following program of the stack operations.")
                        stack=[]
                        top=None
                        while True:
                            print("stack operations")
                            print("1.push")
                            print("2.pop")
                            print("3.peek")
                            print("4.display stack")
                            print("5.exit")
                            ch=int(input("enter your choice:"))
                            if ch==1:
                                n=int(input("enter the no. of items that you wanted to write:"))
                                for i in range(n):
                                    item=int(input("enter the item"+str(i+1)+":"))
                                    push(stack,item)
                            elif ch==2:
                                item=pop(stack)
                                if item=="under flow":
                                    print("underflow!stack is empty!")
                                else:
                                    print("poped item is:",item)
                            elif ch==3:
                                item=peek(stack)
                                if item=="underflow":
                                    print("underflow!stack is empty!")
                                else:
                                    print("top most item is:",item)
                            elif ch==4:
                                display(stack)
                            elif ch==5:
                                break
                            else:
                                print("invalid choice!")   
                        else:
                            print("Invalid choice!")
                        print(" *********************************************************************** ")
                    elif i7==2:
                        print("A Queue is a linear structure which follows a particular order in which the operations are performed.")
                        print("The order is First In First Out (FIFO).")
                        print("The following functions are QUEUE operations")
                        print("QUEUE operations")
                        print("1.Enqueue:Adds the value at end of the list.")
                        print("2.Dequeue:Removes the value which is at end of the list.")
                        print("3.peek:It is referred as inspection.")
                        ############### queue IMPLEMENTAION ###################
                        """
                           queue:implemented as a list
                           front:Integer having position if first (front most) element in a queue
                           rear: integer having position of last element in queue
                        """                       
                        print(" The following program is the example of how queue operations are implemented.")
                        fh=open("queue.txt")
                        print(fh.read())
                        print("Please run the following program of the queue operations.")
                        queue=[]
                        front=None
                        b=True
                        while b:
                            print("QUEUE OPERATIONS")
                            print("1.Enqueue")
                            print("2.Dequeue")
                            print("3.Peek")
                            print("4.Display queue")
                            print("5.Exit")                           
                            ch=int(input("Enter your choice(1-5):"))
                            if ch==1:
                                n=int(input("enter the no. of items that you wanted to write:"))
                                for i in range(n):
                                    item=int(input("Enter item"+str(i+1)+":"))
                                    enqueue(queue,item)
                            elif ch==2:
                                item=dequeue(queue)
                                
                                if item=="Underflow":
                                    print("Underflow! Queue is empty!")
                                else:
                                    print("Deueue-ed item is",item)
                            elif ch==3:
                                item=peek(queue)
                                if item=="Underflow":
                                    print ("Underflow! Queue is empty!")
                                else:
                                    print("Frontmost item is",item)
                            elif ch==4:
                                display(queue)
                            elif ch==5:
                                 b=False
                            else:
                                print("Invalid choice!")
                            print(" *********************************************************************** ")
                    elif i7==3:
                        break
                    else:
                        print("Invalid Input")
                        del i7,con8
                    
            elif i2==8:
                con9=True
                while True:
                    print("___________________ DATA FILE HANDLING__________________")
                    print("1. Opening and closing a file")
                    print("2. Reading and Writting onto files")
                    print("3. Return to previous menu")
                    print(" *********************************************************************** ")
                    try:
                        i7=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print ("Input error")
                    if i7==1:
                        a=open("R_W.txt")
                        b=a.read(837)
                        print (b)
                        a.close()
                        del a,b
                        print(" *********************************************************************** ")
                    elif i7==2:
                        a=open("R_W.txt")
                        b=a.read(837)
                        c=a.read(1900)
                        print (c)
                        a.close()
                        del a,b,c
                        print(" *********************************************************************** ")
                    elif i7==3:
                        break
                    else:
                        print ("Invalid input")
                        del i7,con9
            elif i2==9:
                con10=True
                while con10:
                    print("1.Exception Handiling")
                    print("2.Generators")
                    print("3.Return to previous menu")
                    print(" *********************************************************************** ")
                    try:
                        i7=int(input("Enter your choice(1-3):"))
                    except IOError:
                        print ("Input error")
                    if i7==1:
                        a=open("ERROR.TXT")
                        b=a.read(2235)
                        print (b)
                        a.close()
                        del a,b
                        print(" *********************************************************************** ")
                    elif i7==2:
                        a=open("ERROR.TXT")
                        b=a.read(2235)
                        c=a.read(9999)
                        print (c)
                        a.close()
                        del a,b,c
                        print(" *********************************************************************** ")
                    elif i7==3:
                        con10=False
                    else:
                        print("Invalid Input")
            elif i2==10:
                print(" *********************************************************************** ")
                print("Before exiting please try the quiz")
                print(" *********************************************************************** ")
                print("________________QUIZ__________________")
                quiz()
                con2=False
            else:
                print("Invalid input!")
    elif i1==2:
        a=open("ABOUT.txt")
        b=a.read()
        a.close()
        print (b)
        print("*****************************************************************")
    elif i1==3:
        con=False
        print ("Thank u for using program")
        print("HARI OM")
    
    else:
        print(" ")
        print(" INVALID INPUT !!!!")
        print(" ")
        print("PROGRAM WILL RESTART")
        for i in range (4):
            a=i
        del a
        
