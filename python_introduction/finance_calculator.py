income = int(input("Enter your monthly income: "))
expences = int(input("Enter your total monthly expenses: "))
savings = income - expences
interest_rate = 0.05
total_saving = (savings * 12) + (savings * 12 * interest_rate)
print("Projected savings after one year, with interest, is:",total_saving, ".")