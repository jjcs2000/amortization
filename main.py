from tkinter import *
import pandas as pd
from pandastable import Table, TableModel

root = Tk()

mortgage = Label(root, text="Enter your mortgage payment: ")
mortgage.pack()
mortgageText = Entry(root, width=50)
mortgageText.pack()

monthOryear = Label(root, text="Enter month or year: ")
monthOryear.pack()
monthOryearText = Entry(root, width=50)
monthOryearText.pack()

numberOf = Label(root, text="Enter the number of " + monthOryearText.get() + ": ")
numberOf.pack()
numberOfText = Entry(root, width=50)
numberOfText.pack()

interest = Label(root, text="Enter the interest rate: ")
interest.pack()
interestText = Entry(root, width=50)
interestText.pack()


def cal_sum():
    mortgage = float(mortgageText.get())
    interest = float(interestText.get())
    if monthOryearText.get() == 'month':
        actual_number = int(numberOfText.get())
    else:
        actual_number = int(numberOfText.get())
        actual_number = actual_number * 12

    monthlyamount = float(mortgageText.get()) * interest/1200 * \
                    (1+interest/1200)**actual_number / \
                    ((1+interest/1200)**actual_number - 1)

    monthlyAmount = Label(root, text="Your monthly amount is: " + str(round(monthlyamount, 2)))
    monthlyAmount.pack()


    paymentList=[]
    interestList=[]
    principalList=[]
    totalInterestList=[]
    balanceList=[]
    arraySize = actual_number

    for i in range(arraySize):
        paymentList.append(round(monthlyamount, 2))
        interestList.append(round(mortgage*interest/1200, 2))
        principalList.append(round(monthlyamount - interestList[i], 2))
        if i == 0:
            totalInterestList.append(round(interestList[i], 2))
        else:
            totalInterestList.append(round(interestList[i] + totalInterestList[i-1], 2))
        mortgage=round(mortgage-principalList[i], 2)
        balanceList.append(round(mortgage, 2))

    df = pd.DataFrame(columns=['payment', 'principal', 'interest', 'total interest', 'balance'])
    df['payment']=paymentList
    df['interest']=interestList
    df['principal']=principalList
    df['total interest']=totalInterestList
    df['balance']=balanceList
    df.to_csv("output.csv", encoding='utf-8', index=False)


myButton = Button(root, text="Calculate Sum", command=cal_sum)
myButton.pack()



root.mainloop()
