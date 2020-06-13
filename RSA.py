def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		gcd, x, y = egcd(b % a, a)
		return (gcd, y - (b//a) * x, x)

p = int(input("Enter prime number 1 :"))

q = int(input("Enter prime number 2 :"))

e = int(input("Enter Alice's number 'e' such that gcd(e,phi(N))=1   :"))

m = int(input("Enter the message number :"))
print("")
n=p*q
print("N is ",n)

phi =(p-1)*(q-1)

print("phi(N) is ",phi)

gcd, x, y = egcd(e, phi)

print("The equation is (",e,"*",x,") + (",n,"*",y,") = 1",end='\n\n')

decrypt = x
print("d = ",decrypt,end='\n\n')

print("Encrytion :")
enc = (m**e) % n
print(m,"^",e,"mod",n,"= ",enc,end='\n\n')

print("Decryption :")

if decrypt>0:
	dec = (enc**decrypt) % n
	print(enc,"^",decrypt,"mod",n,"= ",dec,end='\n\n')

elif decrypt<0:
	temp = (enc**(-decrypt)) % n
	gcd1,x1,y1 = egcd(temp,n)
	dec = x1
	print(enc,"^",decrypt,"mod",n,"= ",dec,end='\n\n')


if(m==dec):
    print("original and decrypted messages are same!")





