# # def add_numbers(num1,num2):
# #     print(num1+num2)
# # add_numbers(34, 34)



# # def print_date(year, month, day):
# #     joined = str(year) + '/' + str(month) + '/' + str(day)
# #     print(joined)

# # print_date(1871, 3, 19)

# # def average(values):
# #     if len(values) == 0:
# #         return None
# #     return sum(values) / len(values)
# # a = average([1, 3, 4])
# # print('average of actual values:', a)

# # a=[1,2,3,4]
# # i=-1
# # c=[]
# # while i>=-len(a):
# #     c.append(a[i])
# #     i=i-1
# # print(c)
# # print([a[1],a[0],a[3],a[2]])

# # def my_function(fname):
# #   print(fname + " Refsnes")

# # my_function("Emil")
# # my_function("Tobias")
# # my_function("Linus")


# # def my_function(fname, lname):
# #   print(fname + " " + lname)

# # my_function("Emil", "Refsnes")

# # def my_function(*kids):
# #   print("The youngest child is " + kids[1])

# # my_function("Emil", "Tobias", "Linus")


# a=[1,2,3,4]

# print([a[1],a[0],a[3],a[2]])

# list=[[1,4,5],[1,3,4],[2,6]]
# a=[]
# for i in list:
#     for num in i:
#         a.append(num)
#         a.sort()
# print(a)

# a= [[1, 2, 3], [4, 5, 6]]
# print(a[0])
# print(a[1])
# b = a[0]
# print(b)
# print(a[0][2])
# a[0][1] = 7
# print(a)
# print(b)
# b[2] = 9
# print(a[0])
# print(b)

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# ls1 = [1,5,3,[1,6,4],[4,2]]
# ls2 = []
# i = 0
# while i < (len(ls1)):
#     if type(ls1[i]) ==list:
#         j = 0
#         while j < (len(ls1[i])):
#             ls2.append(ls1[i][j])
#             j+=1
#     else:
#         ls2.append(ls1[i])
#     i+=1
# ls2.sort(reverse=False)
# print(ls2)

# def my_function(kids):
#   print("The youngest child is " + kids)


# my_function("Emil")
# my_function("rohini") 
# my_function("laxmi")

# pass
# my_function("nishu")

# def myfunction():
#   pass

# def my_function(x):
#   print( 5 * x)

# my_function(3)
# my_function(5)
# my_function(9)


# def hr(name):
#     return name
# print(hr("rohini"))
# print(hr("nishu"))
# print(hr("manu"))
# print(hr("laxmi"))

# def num(digit):
#     return  4*digit
# print(num(3))
# print(num(5))
# print(num(6))

# def tri_recursion(k):

#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)

# x = lambda a : a + 10
# print(x(5)) 

# a=["12","21","32","44"]
# i=0
# b=[]
# sum=0
# while i<len(a):
#   sum=sum+int(a[i])
#   b.append(sum)
#   i=i+1
# print(sum)

# a=["12","23","34"] #o/p[3,5,7]
# i=0
# b=[]
# while i<len(a)+1:
#   j=0
#   sum=0
#   while j<len(a[i]):
#     sum=sum+int(a[i][j])
#     b.append(sum)
#     i=i+1
# print(sum)



# # a="rohini"
# a=(input("enter name.."))
# i=0
# while i<5:
#   print(a)
#   i+=1


# a=str(input("enter your name..."))
# i=0
# while i<len(a):
#   print(a)
#   i+=1









# a=str(input("enter your name...n/"))
# i=0
# while i<5:
#   print(a)
#   i+=1


# a=str(input("enter your name="))
# i=0
# while i<1:
#   print(a)
#   i+=1

# l = []
# for i in range(10):
#     l1 = []
#     odd = ' is odd number'
#     even = 'is even number'
#     n = int(input("enter the number___: "))
#     if n %2 ==0:
#         l1.append([n,even])
#     else:
#         l1.append([n,odd])
#     l.extend(l1)
# print(l)

# list=["12","23","34"]#o/p[3,5,7]
# i=0
# n=[]
# while i<len(list):
#     x=int(list[i])
#     a=x//10
#     b=x%10
#     i=i+1
#     sum=a+b
#     n.append(sum)
# print(n)

def check_numbers(num1,num2):
    for i in num1,num2:
        if num1%2==0:
            print("even num")
        elif num2%2==0:
            print("even num")
        else:
            print("not even num")
check_numbers(4, 5)