import math

n = int(input("Enter N :"))

i=1
while(True):
    sum = n + (i**2)
    if math.sqrt(sum)==int(math.sqrt(sum)):
        n1 = int(math.sqrt(sum))+i
        n2 = int(math.sqrt(sum))-i
        print("{} + {}^2  = {} that is {}^2".format(n,i,sum,int(math.sqrt(sum))),end='\n\n')
        print("The prime factors are {} and {}".format(n2,n1))
        break
    
    else:
        print("{} + {}^2  = {} that is not a perfect square".format(n,i,sum),end='\n\n')
        i+=1
