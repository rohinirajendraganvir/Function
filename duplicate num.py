def function(list1):
    i=0
    b=[]
    while i<len(list1):
        if list1[i] not in b:
          b.append(list1[i])
        i=i+1
    print(b)

function([1,2,3,3,4,4,5,7,6])

