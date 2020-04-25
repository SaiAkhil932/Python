shopping = []
print("Please enter the items one by one and type DONE if you finished your list")
while(True):
    shop = input("Enter please :")
    if(shop == 'DONE'):
        break
    else:
        shopping.append(shop)
        continue
print("here's your list :-")
for i in range(len(shopping)):
    print(shopping[i])

