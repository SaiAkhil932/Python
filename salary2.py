k = int(input("Enter the number of salaries you want to enter :"))
sallist=[]
salary= []
for i in range(k):
    sallist.append(input("Enter the salary :"))
    n = len(sallist[i])
    sal=sallist[i]
    salary1 = sal[2:n-1]
    salary2 = salary1.split(',')
    s=""
    s = s.join(salary2)
    salary.append(int(s))
print(salary)