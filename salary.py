salary= input("Enter the salary :")
n = len(salary)
salary1 = salary[2:n-1]
salary2 = salary1.split(',')
s=""
s = s.join(salary2)
print('Non-Messy Salary is :',int(s))