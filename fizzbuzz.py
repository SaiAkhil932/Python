for i in range(1,51):
    if(int(i/3)==i/3 and int(i/5)!=i/5):
        print("Fizz")
    elif(int(i/5)==i/5 and int(i/3)!=i/3):
        print("Buzz")
    elif(int(i/3)==i/3 and int(i/5)==i/5):
        print("FizzBuzz")
    else:
        print(i)