# def sum(numbers):
#     total = 0
#     for x in numbers:
#         total += x
#     return total
# print(sum((8, 2, 3, 0, 7)))




# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# def sum(num):
#     sum = a+b
#     print(sum)
# sum(sum)

def sum(list):
    i=0
    sum=0
    while i<len(list):
        sum=sum+list[i]
        i=i+1
    return sum
list=[8,2,3,0,7]
print(sum(list))

