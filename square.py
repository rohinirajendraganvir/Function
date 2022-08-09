def sq(num):
    words = list(str(num))
    for word in words: 
        print(int(word)**2, end="") 

num = 9119
sq(num)
print()