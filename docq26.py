def fizz_buzz(num):
    if num%3==0 and num%5==0:
        print("fizzbuzz")
    elif num%5==0:
        print("buzz")
    elif num%3==0:
        print("fizz")
fizz_buzz(25)
