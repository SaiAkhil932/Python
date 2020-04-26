orders = [ ["34587", "Learning Python", "Mark Lutz", 4, 40.95], 
      ["98762", "Programming Python", "Mark Lutz", 5, 56.80], 
      ["77226", "Head First Python", "Paul Barry", 3,32.95],
      ["88112", "Einführung in Python3", "Bernd Klein",  3, 24.99]
    ]

def func(x):
    if x[1]<100:
        return (x[0],x[1]+10)
    else:
        return (x[0],x[1])

list1 = list(map(lambda x:(x[0],round(x[3]*x[4],2)),orders))

list2 =list(map(func,list1))

print(list2)