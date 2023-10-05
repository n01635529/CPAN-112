name = input("Enter your name: ")
income = int(input("Input your income: $"))
if income <= 44701 :
    tax = income * 0.15
elif income > 44701 and income <= 89401 :
    tax = 44701 * 0.15 + (income - 44701) * 0.22
elif income > 89401 and income <= 138586 :
    tax = 44701 * 0.15 + (89401 - 44701) * 0.22 + (income - 89401) * 0.29
elif income > 138586 :
    tax = 44701 * 0.15 + (89401 - 44701) * 0.22 + (138586 - 89401) * 0.29 + (income - 138586) * 0.29
print("Hello " + name)
print("Your tax is: $" + str(tax))