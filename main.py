import pandas as pd

mortgage = float(input("Enter your mortgage payment: "))
#print(mortgage)
monthOryear = input("Enter month or year: ")
#print(monthOryear)
numberOf = int(input("Enter the number of " + monthOryear + ": "))
#print(numberOf)
interest = float(input("Enter the interest rate: "))
#print(interest)
if monthOryear.lower() == 'month':
    actual_number = numberOf
else:
    actual_number = numberOf * 12

monthlyamount = mortgage * interest/1200 * \
                (1+interest/1200)**actual_number / \
                ((1+interest/1200)**actual_number - 1)
print("monthly payment is: ")
print(round(monthlyamount, 2))

monthOryearDF = input("Enter monthly or yearly amortization schedule: ")
if monthOryearDF.lower() == 'monthly':
    arraySize = actual_number
    isYear = False
else:
    arraySize = actual_number
    isYear = True

paymentList=[]
interestList=[]
principalList=[]
totalInterestList=[]
balanceList=[]
for i in range(arraySize):
    paymentList.append(round(monthlyamount, 2))
    interestList.append(round(mortgage*interest/1200, 2))
    principalList.append(round(monthlyamount - interestList[i], 2))
    if i == 0:
        totalInterestList.append(interestList[i])
    else:
        totalInterestList.append(interestList[i] + totalInterestList[i-1])
    mortgage=mortgage-principalList[i]
    balanceList.append(mortgage)

df = pd.DataFrame(columns=['payment', 'principal', 'interest', 'total interest', 'balance'])
df['payment']=paymentList
df['interest']=interestList
df['principal']=principalList
df['total interest']=totalInterestList
df['balance']=balanceList

print(df)






