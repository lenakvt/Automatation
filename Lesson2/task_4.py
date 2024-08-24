def Fizz_Buzz(n):
    if (n%3==0) and (n%5==0):
        print ("FizzBazz")
    elif (n%3==0):
        print ("Fizz")
    elif (n%5==0):
        print ("Bazz")
    else:
        print(n)
number = input("Введите число: ")
number= int(number)

Fizz_Buzz(number)