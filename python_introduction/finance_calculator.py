income = int(input("Enter your monthly income: "))
expences = int(input("Enter your total monthly expenses: "))
savings = income - expences
interest_rate = .05
total_saving = (12 * savings) + (savings * 12 * interest_rate)
print("Projected savings after one year, with interest, is:",total_saving, ".")