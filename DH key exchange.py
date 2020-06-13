p = int(input("Enter the chosen prime number (p) :"))
c = int(input("Enter the chosen number (c) :"))

print("")
print("The set ({},{}) is known both to ALice and Bob".format(p,c),end='\n\n')
a = int(input("Enter the number which alice selects(a) :"))

b = int(input("Enter the number chosen by Bob (b) :"))



A = (c**a) % p

print("A = ",A,"is shared to Bob",end='\n\n')

B = (c**b) % p

print("B = ",B,"is shared to Alice",end='\n\n')


Da = (B**a) % p

print("Private key computed by Alice = ",Da,end='\n\n')

Db = (A**b) % p

print("Private key computed by Bob = ",Db,end='\n\n')

if(Da==Db):
    print("Both are same!!")
else:
    print("Oh  no!...They are not same")