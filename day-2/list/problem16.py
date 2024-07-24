my_list=[22,26,27,29]
print("enter choice")
choice=int(input())
if(choice==1):
    my_list.append(21)
elif(choice==2):
    my_list.sort()
elif(choice==3):
    my_list.pop()
elif(choice==4):
    print("good morning")
else:
    my_list.length()
print(*my_list)    
