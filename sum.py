

#     n=[]
#     while i<len(list1):
#         x=(list1[i])
#         a=x//10
#         b=x%10
#         c=a+b
#         n.append(c)
#         i+=1
#     print(n)
# function()
# n.append(sum)

def sum(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return sum
list=[8,2,3,0,7]
print(sum(list))
