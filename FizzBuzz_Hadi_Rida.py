def fizz_buzz(n) :
    i=1
    while i <=n:
        if (i%3==0) and (i%5==0):
            print("FizzBuzz")  
        elif (i%3==0):
            print("Fizz")
        elif (i%5==0):
            print("Buzz")
        else:
            print(i) 
        i+=1  
number=int(input("WELCOME TO FIZZBUZZ PLEASE ENTER A NUMBER (integer) \n\t number :  ") ) 
fizz_buzz(number)
