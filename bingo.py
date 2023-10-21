import random
import numpy as np


def create_system_bingo():
    i=0
    bingo=[]
    all=[]
    internal_list=[]
    while(len(bingo)<5):
        x=random.randint(1,25)
        if(x not in all):
            all.append(x)
            internal_list.append(x)

        if(len(internal_list)==5):
            bingo.append(internal_list)
            internal_list=[]
    return bingo

def create_user_bingo():
    bingo=[[],[],[],[],[]]
    all=[]
    for i in(range(5)):
        for j in range((5)):
            print("Enter element at position ",i+1,j+1," : ",end="")
            user_input=0
            while(user_input<1 or user_input>25 or user_input in all):
                user_input=int(input())
                if(user_input<1 or user_input>25 or user_input in all):
                    print("wrong input\n plese enter another number between 1 and 25 : ")
            bingo[i].append(user_input)
            all.append(user_input)
    print("\nyour bingo is: ")
    show_bingo(bingo)
    return bingo

def show_bingo(bingo):
    i=0
    j=0
    while(i<5):
        while(j<5):
            if(bingo[i][j]<10):
                print(bingo[i][j],"  ",end="")
            else:
                print(bingo[i][j]," ",end="")
            j+=1
        i+=1
        j=0
        print()
        
def bingo_element_deletion(elt,bingo):
    for i in range(5):
        for j in range(5):
            if(elt==bingo[i][j]):
                bingo[i][j]=0
                break
    #print("updated bingo becomes: ")
    #show_bingo(bingo)
    return bingo

def bingo_counter(bingo):
    counter=0
    #row checker
    for i in range(5):
        rcounter=0
        for j in range(5):
            if(bingo[i][j]==0):
                rcounter+=1
        if(rcounter==5):
            counter+=1
            
    #column checker
    for i in range(5):
        ccounter=0
        for j in range(5):
            if(bingo[j][i]==0):
                ccounter+=1
        if(ccounter==5):
            counter+=1
    
    #diagonal checker
    dcounter=0
    for i in range(5):
        if(bingo[i][i]==0):
            dcounter+=1
    if(dcounter==5):
        counter+=1
    
    #reverse diagonal checker
    dcounter=0
    for i in range(5):
        for j in range(5):
            if(i+j==4 and bingo[i][j]==0):
                dcounter+=1
    if(dcounter==5):
        counter+=1
    
    return counter
            
def easy_level():
    #The easy level
    #creating user bingo
    user_bingo=create_user_bingo()

    #creating system bingo
    system_bingo=create_system_bingo()
    print("\n The system bingo is \n")
    show_bingo(system_bingo)

    #initializing important variables
    steps_counter=0
    covered_numbers=[]

    #giving choice to the user if they want to start
    start_choice=int(input("press 1 to start from the computer press 2 to start from user: "))
    if(start_choice==1):
        system_choice=random.randint(1,25)
        covered_numbers.append(system_choice)
        print("system choice is ",system_choice)
        system_bingo=bingo_element_deletion(system_choice,system_bingo)
        user_bingo=bingo_element_deletion(system_choice,user_bingo)
        steps_counter+=1

    count=0

    while(count<5):
        print("\n")

        #taking user input 
        user_choice=int(input("Enter the number to be marked: "))
        while(user_choice in covered_numbers):
            user_choice=int(input("That number is already covered please enter another number: "))
        covered_numbers.append(user_choice)

        #making changes in both the bingos according to the received input
        user_bingo=bingo_element_deletion(user_choice,user_bingo)
        system_bingo=bingo_element_deletion(user_choice,system_bingo)

        #checking bingos after 15 checks as it takes at least 17 choices to make 5 bingos
        if(steps_counter>=15):
            count=bingo_counter(user_bingo)
            if(count>=5):
                print("YOU WON")
                show_bingo(user_bingo)
                break

            count=bingo_counter(system_bingo)
            if(count>=5):
                print("system wins")
                show_bingo(system_bingo)
                break
            
        #*************************************************
        #taking random number
        system_choice=random.randint(1,25)
        while(system_choice in covered_numbers):
            system_choice=random.randint(1,25)
        covered_numbers.append(system_choice)
        print("system choice is ",system_choice)

        #making changes in both the bingos according to the random number 
        user_bingo=bingo_element_deletion(system_choice,user_bingo)
        system_bingo=bingo_element_deletion(system_choice,system_bingo)
        
        #checking both bingos after 15 checks as it takes at least 17 choices to make 5 bingos
        if(steps_counter>=15):
            count=bingo_counter(system_bingo)
            if(count>=5):
                print("system wins")
                show_bingo(system_bingo)
                break

            count=bingo_counter(user_bingo)
            if(count>=5):
                print("YOU WON")
                show_bingo(user_bingo)
                break

        #increasing the steps by 2 for user and system
        steps_counter+=2

        #showing the current progress of the user
        print("\n Your bingo now becomes\n")
        show_bingo(user_bingo)
        print("Currently you have made ",bingo_counter(user_bingo)," bingos")

        #giving option for the user to see system bingo
        cheating=int(input("Press 1 to see the system bingo: "))
        if(cheating==1):
            print("\nSystem bingo is now\n")
            show_bingo(system_bingo)
            print("Currently system have made ",bingo_counter(system_bingo)," bingos")

def max_counter(matrix):
    max_zeroes=0
    index=0
    maxlist=[]
    for i in range(5):
        if(matrix[i]!=5):
            if(max_zeroes<matrix[i]):
                max_zeroes=matrix[i]
                index=i
    maxlist.append(index)
    maxlist.append(max_zeroes)
    return maxlist

def max_all(row,column,diagonal,reverse_diagonal):
    if(row>=column):
        if(row>=diagonal):
            if(row>=reverse_diagonal):
                return '0'
            else:
                return '3'
        else:
            if(diagonal>=reverse_diagonal):
                return '2'
            else:
                return '3'

    else:
        if(column>=diagonal):
            if(column>reverse_diagonal):
                return '1'
            else:
                return '3'
        else:
            if(diagonal>=reverse_diagonal):
                return '2' 
            else:
                return '3'

def check_best_move(system_bingo):
    #counter=0
    #row checker
    #choice =0 for rows, 1 for columns, 2 for diagonal and 3 for reverse diagonal
    choice=0
    rcounter=[0,0,0,0,0]
    for i in range(5):
        for j in range(5):
            if(system_bingo[i][j]==0):
                rcounter[i]+=1
        if(rcounter[i]==5):
            rcounter[i]==-1
    row_list=max_counter(rcounter)
    row=row_list[1]
    row_index=row_list[0]
        
    #column checker
    ccounter=[0,0,0,0,0]
    for i in range(5):
        for j in range(5):
            if(system_bingo[j][i]==0):
                ccounter[i]+=1
        if(rcounter[i]==5):
            rcounter[i]==-1
    column_list=max_counter(ccounter)
    column=column_list[1]
    column_index=column_list[0]
    
    #diagonal checker
    dcounter=0
    for i in range(5):
        if(system_bingo[i][i]==0):
            dcounter+=1
    if(dcounter==5):
        dcounter=-1
    diagonal=dcounter
    
    #reverse diagonal checker
    rdcounter=0
    for i in range(5):
        for j in range(5):
            if(i+j==4 and system_bingo[i][j]==0):
                rdcounter+=1
    if(rdcounter==5):
        rdcounter=-1
    reverse_diagonal=rdcounter
    
    #checking which has the maximum number of zeroes
    choice=max_all(row,column,diagonal,reverse_diagonal)

    #making choice=row/column+its index
    if(choice=='0'):
        choice+=str(row_index)
    elif(choice=='1'):
        choice+=str(column_index)

    return choice

def medium_level():
    #The medium level
    #creating user bingo
    user_bingo=create_user_bingo()
    # user_bingo_list=[1,2,3,4,0,5,6,7,0,0,11,14,13,0,0,22,23,0,0,0,20,21,0,0,0]
    # user_bingo=np.array(user_bingo_list).reshape(5,5)
    #creating system bingo
    #system_bingo=create_system_bingo()
    system_bingo_list=[1,2,3,4,0,5,6,7,0,0,11,14,13,0,0,22,23,0,0,0,20,21,0,0,0]
    system_bingo=np.array(system_bingo_list).reshape(5,5)
    print("\n The system bingo is \n")
    show_bingo(system_bingo)

    #initializing important variables
    steps_counter=11
    covered_numbers=[]

    #giving choice to the user if they want to start
    start_choice=int(input("press 1 to start from the computer press 2 to start from user: "))
    if(start_choice==1):
        system_choice=random.randint(1,25)
        covered_numbers.append(system_choice)
        print("system choice is ",system_choice)
        system_bingo=bingo_element_deletion(system_choice,system_bingo)
        user_bingo=bingo_element_deletion(system_choice,user_bingo)
        steps_counter+=1

    count=0
    while(count<5):
        print("\n")
        
        #taking user input 
        user_choice=int(input("Enter the number to be marked: "))
        while(user_choice in covered_numbers):
            user_choice=int(input("That number is already covered please enter another number: "))
        covered_numbers.append(user_choice)

        #increasing the steps by 1 
        steps_counter+=1

        #making changes in both the bingos according to the received input
        user_bingo=bingo_element_deletion(user_choice,user_bingo)
        system_bingo=bingo_element_deletion(user_choice,system_bingo)

        #checking bingos after 15 checks as it takes at least 17 choices to make 5 bingos
        if(steps_counter>=15):
            count=bingo_counter(user_bingo)
            if(count>=5):
                print("YOU WON")
                show_bingo(user_bingo)
                break

            count=bingo_counter(system_bingo)
            if(count>=5):
                print("system wins")
                show_bingo(system_bingo)
                break

        #selection of the best choice by the system
        choice=check_best_move(system_bingo)

        #if diagonal has maximum zeroes
        if(choice=='2'):
            system_choice=diagonal_chooser(system_bingo)
            print("system choice is ",system_choice)

        #if reverse diagonal has maximum zeroes
        if(choice=='3'):
            system_choice=reverse_diagonal_chooser(system_bingo)
            print("system choice is ",system_choice)

        #if a row has maximum zeroes
        if(choice[0]=='0'):
            system_choice=row_chooser(system_bingo,int(choice[1]))
            print("system choice is ",system_choice)

        #if a column has maximum zeroes
        if(choice[0]=='1'):
            system_choice=column_chooser(system_bingo,int(choice[1]))
            print("system choice is ",system_choice)

        #making changes in user bingo according to the random number as system bingo has already been updated
        user_bingo=bingo_element_deletion(system_choice,user_bingo)

        #checking both bingos after 15 checks as it takes at least 17 choices to make 5 bingos
        if(steps_counter>=15):
            count=bingo_counter(system_bingo)
            if(count>=5):
                print("system wins")
                show_bingo(system_bingo)
                break

            count=bingo_counter(user_bingo)
            if(count>=5):
                print("YOU WON")
                show_bingo(user_bingo)
                break

        #increasing the steps by 1 
        steps_counter+=1

        #showing the current progress of the user
        print("\n Your bingo now becomes\n")
        show_bingo(user_bingo)
        print("Currently you have made ",bingo_counter(user_bingo)," bingos")

        

    return 0

def column_chooser(system_bingo,column_index):
    j=column_index
    for i in range(5):
        if(system_bingo[i][j]!=0):
            system_choice=system_bingo[i][j]
            system_bingo[i][j]=0
            return system_choice

def row_chooser(system_bingo,row_index):
    i=row_index
    for j in range(5):
        if(system_bingo[i][j]!=0):
            system_choice=system_bingo[i][j]
            system_bingo[i][j]=0
            return system_choice

def reverse_diagonal_chooser(system_bingo):
    for i in range(5):
        for j in range(5):
            if(i+j==4 and system_bingo[i][j]!=0):
                system_choice=system_bingo[i][j]
                system_bingo[i][j]==0
                return system_choice

def diagonal_chooser(system_bingo):
    for i in range(5):
        if(system_bingo[i][i]!=0):
            system_choice=system_bingo[i][i]
            system_bingo[i][i]=0
            return system_choice

def asian_hack(covered_numbers):
    if(len(covered_numbers)==17):
        all_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        for i in range(len(covered_numbers)):
            all_numbers.remove(covered_numbers[i])
        system_bingo=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        system_bingo[0][1]=all_numbers[0]
        system_bingo[0][3]=all_numbers[1]
        system_bingo[2][0]=all_numbers[2]
        system_bingo[2][1]=all_numbers[3]
        system_bingo[2][3]=all_numbers[4]
        system_bingo[2][4]=all_numbers[5]
        system_bingo[4][1]=all_numbers[6]
        system_bingo[4][3]=all_numbers[7]
        print("The system wins")
        show_bingo(system_bingo)
        print("\n\nEMOTIONAL DAMAGE!!!!!!!!\n\n")
        return True
    return False

def Asian_level():
    #creating user bingo
    user_bingo=create_user_bingo()

    #initializing important variables
    steps_counter=0
    covered_numbers=[]

    #giving choice to the user if they want to 
    start_choice=int(input("press 1 to start from the computer press 2 to start from user: "))
    if(start_choice==1):
        system_choice=random.randint(1,25)
        covered_numbers.append(system_choice)
        print("system choice is ",system_choice)
        steps_counter+=1

    #while(steps_counter<25):
    count=0

    #loop which runs until anyone makes 5 bingo
    while(count<5):
        print("\n")
        #taking user input 
        user_choice=int(input("Enter the number to be marked: "))
        while(user_choice in covered_numbers):
            user_choice=int(input("That number is already covered please enter another number: "))
        covered_numbers.append(user_choice)

        #incrementing number of steps done by 1
        steps_counter+=1

        #making changes in user bingo according to the received input
        user_bingo=bingo_element_deletion(user_choice,user_bingo)

        #checking bingos after 15 checks as it takes at least 17 choices to make 5 bingos
        if(steps_counter>=15):
            count=bingo_counter(user_bingo)
            if(count>=5):
                print("YOU WON")
                show_bingo(user_bingo)
                break
            #applying the hack
            if(asian_hack(covered_numbers)):
                break

        #taking random number
        system_choice=random.randint(1,25)
        while(system_choice in covered_numbers):
            system_choice=random.randint(1,25)
        covered_numbers.append(system_choice)
        print("system choice is ",system_choice)

        #incrementing number of steps done by 1
        steps_counter+=1

        #making changes in both the bingos according to the random number 
        user_bingo=bingo_element_deletion(system_choice,user_bingo)
        
        #checking user bingo after 15 checks as it takes at least 17 choices to make 5 bingos
        if(steps_counter>=15):
            count=bingo_counter(user_bingo)
            if(count>=5):
                print("YOU WON")
                show_bingo(user_bingo)
                break
            #applying the hack
            if(asian_hack(covered_numbers)):
                break
        
        #showing the current progress of the user
        print("\n Your bingo now becomes")
        show_bingo(user_bingo)
        print("Currently you have made ",bingo_counter(user_bingo)," bingos")



#BINGO CREATION
all_numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


#choosing the level of difficulty
level=1
levels=[1,2,3]
while(level in levels):
    level=int(input("Press 1 for easy level\nPress 2 for medium level\nPress 3 for Asian difficulty\nPress any other number to exit\n"))
    if(level==1):
        easy_level()
    elif(level==2):
        medium_level()
    elif(level==3):
        print("You choose to lose yourself")
        Asian_level()
    else:
        break


