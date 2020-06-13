p = int(input("Enter the chosen prime number (p) :"))
g = int(input("Enter the chosen primitive element (g) :"))

print("")
print("The set ({},{}) is known both to ALice and Bob".format(p,g),end='\n\n')

a = int(input("Enter the number which alice selects(a) :"))

A = (g**a) % p

print("A = ",A,"is shared to Bob",end='\n\n')

k = int(input("Enter the ephemeral key chosen by Bob (k) :"))

c1 = (g**k) % p

m = int(input("Enter the message to send(m) :",))

c2 = (m*(A**k)) % p
print("")
print("the encrypted set ({},{}) is sent to Alice".format(c1,c2))

print("")

print("Decryption starts....",end='\n')

temp=p-a-1
answer = ((c1**temp)*c2) % p

print("The decrypted message is",answer)
