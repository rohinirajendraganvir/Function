n=int(input("enter the num"))
i=0
sum=0
while i<=n:
        if i%2==0:
            sum=sum+i
            print(i,"even")
        else:
            sum=sum+i
            print(i,"odd")
        i=i+1