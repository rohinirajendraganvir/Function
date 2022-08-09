

def list1():
    list1 = [2, -7, 5, -64, -14]
    pos = 0
    neg = 0
    i = 0 
    while i < len(list1):
        if list1[i] > 0 :
            pos+=1
        else:
            neg+=1
        i+=1
    print("pos=",pos)
    print('neg=',neg)
list1()