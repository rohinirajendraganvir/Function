def alphabets(string):
    i=0
    upper_case=0
    lower_case=0
    while i<len(string):
        if string[i].isupper():
            upper_case+=1
        elif string[i].islower():
            lower_case+=1
        i=i+1
    print("uppercase =",upper_case)
    print("lower case =",lower_case)
# string=input("enter string...")
alphabets("tokKOm")
