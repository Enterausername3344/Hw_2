salary = int(input("What is your Monthly Salary? "))
children = input("Do you have any kids? ").strip().lower()  # Normalize input

if children == "yes":
    childrenyes = int(input("How many children do you have? "))
    if salary < 1000:
        net_salary = salary - (salary * (0.1 - (0.01 * childrenyes)))
        print(f"Your net salary is: ${net_salary:.2f}")