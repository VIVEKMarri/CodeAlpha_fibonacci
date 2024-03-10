#Code Alpha task-1 Fibonacci generator
num=int(input("Enter the no of sequence to be generated:"))
n1,n2=0,1
sum=0
if num<=0:
    print("Enter the valid number!!!")
for _ in range(num):
    print(sum)
    n1=n2
    n2=sum
    sum=n1+n2