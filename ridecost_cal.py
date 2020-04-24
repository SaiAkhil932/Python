distance = float(input('Enter the distance travelled (in km):'))
cost = float(input('Enter the cost of diesel per litre :'))
fuelavg = float(input('Enter your vehicle fuel average (km/litre):'))

consumption = (distance/fuelavg)
costperday = (cost * consumption)

print('Your ride cost is : ',costperday, 'INR/day20')