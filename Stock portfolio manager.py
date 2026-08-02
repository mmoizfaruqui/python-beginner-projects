Largest=0
Portfolio=0
HighestCompany=""
print("1:Press 1 if you want to enter the information")

num=int(input("Enter 1 if you wan tto enter the information else it woill break and program will be fininshed"))
while num==1:
 Total=0
 x=int(input("Enter 1 again if you want to continue:"))
 if x==1:
  print("Enter the name of the comapny, then price per share then number of shares")
  ask = list( input("Enter info: ").split())
 # 1. Convert the second item (index 1) to an integer
  num1 = int(ask[1])
# 2. Convert the third item (index 2) to an integer
  num2 = int(ask[2]) 
#Calculate Total of one company
  Total=num1*num2
  print("The Total amount on ",ask[0] ,"is ",Total)

#Calculating total portfolio value by incrementing total everytime
  Portfolio=Portfolio+Total
#Calculating Largest value is of which compnay
  if Total>Largest:
   Largest=Total
   HighestCompany=ask[0]
 else:
  print("The Largest upholding was of company ",HighestCompany,"with the amount of",Largest)
  print("your total portfolio amount was",Portfolio)
  break


 
 