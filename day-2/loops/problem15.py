#avg of i even elements
my_list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(my_list) 
for i in range(len(my_list)):
      sum+=my_list[i]
      count+=1
print(sum/count)      