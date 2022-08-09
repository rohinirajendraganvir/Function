def function(age):
    i=0
    while i<=age:
        if age<=18:
            print("not able to voting")
        else:
            print("able to voting")
            i=i+1
        break
function(19)