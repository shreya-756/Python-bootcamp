print("enter the a value")
a=int(input())
if(a>0 and a%2==0):
   print("positive and even")
elif(a<0 and a%2==0):
    print("negative and even")
elif(a>0 and a%2!=0):
 print("positive and odd")
else:
  print("negative and odd")