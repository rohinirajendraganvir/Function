# def function(list1):
#     i=0
#     count=0
#     while i<len(list1):
#         if list1[i][0]==list1[i][-1]:
#             count=count+1
#             i=i+1
#     print(count)
        
# list1=["aba","abc","mom","pop"]
# function()

def sq(num):
    words = list(str(num))
    for word in words: 
        print(int(word)**2, end="") 

num = 9119
sq(num)
print()