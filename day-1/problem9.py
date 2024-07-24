x_height=int(input()) 
X_weight=int(input())
X_fat=int(input())
y_height=int(input())
y_weight=int(input())
y_fat=int(input())
X=0 
y=0
if x_height>=140 and X_weight%2==0 and X_fat<12:
     x=1 
if x_height>=140 and X_weight%2==0 and X_fat<12:
     y=1
if x==1 and y==1: 
    print("in same plane")
else: 
     print("not in same plane")