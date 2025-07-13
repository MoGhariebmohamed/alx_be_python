income = float(input("Enter your monthly income: "))
expences = float(input("Enter your total monthly expenses: "))
savings = income - expences
total_saving = (savings * 12) + (savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:",total_saving, ".")