


import pandas as pd
import matplotlib.pyplot as plt

#  Create Expense Dataset

data = {
    "Month": ["January", "February", "March", "April", "May", "June"],
    "Rent": [12000, 12000, 12000, 12000, 12000, 12000],
    "Food": [4500, 4800, 5000, 4700, 5200, 5100],
    "Transport": [1500, 1600, 1550, 1700, 1650, 1600],
    "Entertainment": [2000, 1800, 2200, 2100, 2500, 2300]
}

df = pd.DataFrame(data)

#  Total per Month

df["Total_Expense"] = df[["Rent", "Food", "Transport", "Entertainment"]].sum(axis=1)


#  Calculations

total_expense = df["Total_Expense"].sum()
average_expense = df["Total_Expense"].mean()
median_expense = df["Total_Expense"].median()


#  Identify High Expense Months

high_expense_months = df[df["Total_Expense"] > average_expense]


#  Display Results
print("\n----- Monthly Expense Data -----")
print(df)

print("\nTotal Expense (6 Months): ₹", total_expense)
print("Average Monthly Expense: ₹", round(average_expense, 2))
print("Median Monthly Expense: ₹", median_expense)

print("\nHigh Expense Months (Above Average):")
print(high_expense_months[["Month", "Total_Expense"]])

#  Line Chart 

plt.figure()
plt.plot(df["Month"], df["Total_Expense"], marker='o')
plt.xlabel("Month")
plt.ylabel("Total Expense")
plt.title("Monthly Expense Trend")
plt.show()


#  Bar Chart 

plt.figure()
plt.bar(df["Month"], df["Total_Expense"])
plt.xlabel("Month")
plt.ylabel("Total Expense")
plt.title("Monthly Expense Comparison")
plt.show()
