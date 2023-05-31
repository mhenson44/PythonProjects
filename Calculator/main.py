n1 = input("Enter a number: ")
n2 = input("Enter a number: ")
decision = input("Do you want to Multiply, Divide, Add, or Subtract?: ")
if decision == "Multiply":
    total = float(n1) * float(n2)
elif decision == "Divide":
    total = float(n1)/float(n2)
elif decision == "Add":
   total = float(n1) + float(n2)
elif decision == "Subtract":
   total = float(n1) - float(n2)

print(total)