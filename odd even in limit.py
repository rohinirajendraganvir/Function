# def shownumbers(limit):

#         for i in range(limit+1):

#             if (i%2==0):

#                 print (i,"Even", end=" ")

#         else:

#                 print(i,"Odd", end=" ")

#                 print()

                
# shownumbers(3)


# def shownumbers(limit):
#     i=0
#     while i<=limit:
#         if i%2==0:
#             print(i,"even")
#         else:
#             print(i,"odd")
#         i=i+1
# shownumbers(25)



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
