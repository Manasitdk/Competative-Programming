n=int(input("Enter the no."))
c=1
while(n!=1):
    if(n%2==0):
        n=n/2
        c=c+1
    else:
        n=3*n+1
        c=c+1
print(n)
print("count",c)

