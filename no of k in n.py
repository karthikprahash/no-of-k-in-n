# no-of-k-in-n
N,k=map(int,input().split())
n=[int(i) for i in input().split()]
count=0
for i in n:
    if(k == i):
        count=count+1
        
print(count)
    
