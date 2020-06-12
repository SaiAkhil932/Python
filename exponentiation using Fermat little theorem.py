import math

def gcd(a, b): 
  
    if (a == 0): 
        return b 
    return gcd(b % a, a) 

def phi(n): 
  
    result = 1
    for i in range(2, n): 
        if (gcd(i, n) == 1): 
            result+=1
    return result 

print("Please enter in the  format a^b mod m")
a= int(input("Enter a :"))
b= int(input("Enter b :"))
m= int(input("Enter m :"))

amod = a % m
print("")
print(a," mod ",m," is = ",amod,"mod",m)
p = phi(m)
print("")
print("phi(",m,") = ",p)
temp = b / p
temp2=b//p
temp3 = temp - temp2
temp3 = temp3 * p
print("")
print(b," can be written as ",p,"*",temp2,"+",round(temp3))
print("")
print(amod,"^",p,"*",temp2," is equal to 1")
print("")
reduced = amod**round(temp3)
print(amod,"^",round(temp3)," is equal to ",reduced,"mod",m)
answer = reduced % m
print("")
print(reduced,"mod",m," = " ,answer)

