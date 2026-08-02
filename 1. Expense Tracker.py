import Functions

ask = list(map(int, input("Enter the amount for each category (Food, House bills, Kids expense, Others) separated by spaces: ").split()))
Budget=int(input("Enter total Monthly earning"))
Total=0
largest=0
count=0
Flag=False

for num in ask:
    Total=Total+num
    print("you total has incraesed to ",Total)
    if num>largest:
        largest=num

for nums in ask:
    count += 1
    if nums == largest:
        Flag = True
        break

if count==1:
    catogary="Food"
elif count==2:
    catogary="House Bills"
elif count==3:
    catogary="Kids expneses"
elif count==4:
    catogary="Others uses and accessosries"   

    
    


if Total>Budget:
    debt=Functions.Debt(Budget,Total)
    print("you debt is:",debt)
elif  Budget>Total:
    saving=Functions.Subtract(Budget,Total)
    print("you savings is:",saving)
else:
    print("you eqauled you expnses by you earnings")


print("Your Total expenses were:",Total)
print("Your Largest expenses was:",largest)
print("Largest expense category:",catogary)



    
    




