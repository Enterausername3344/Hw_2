#IF tax problem
salary=int(input("What is your Monthly Salary in USD? "))
children = input("Do you have any kids? ")
if children == "Yes" or children == "yes":
    childrenyes = int(input("How many children do you have? "))
    if salary < 1000 and childrenyes > 0:
        net_salary= float(salary-(salary*(0.1-(0.01*childrenyes))))
        if childrenyes >10:
            print(f"your net salary is: ${salary}")
        else:
            print(f"your net salary is: ${net_salary}")
    elif 1000 <= salary < 2000 and childrenyes > 0:
        net_salary= float(salary-(salary*(0.12-(0.01*childrenyes))))
        if childrenyes > 12:
            print(f"your net salary is: ${salary}")
        else:
            print(f"your net salary is: ${net_salary}")
    elif 20000 <= salary < 4000 and childrenyes>0:
        net_salary = float(salary - (salary * (0.14 - (0.005 * childrenyes))))
        if childrenyes > 28:
            print(f"your net salary is: ${salary}")
        else:
            print(f"your net salary is: ${net_salary}")
    elif salary >= 4000 and childrenyes>0:
        net_salary = float(salary - (salary * (0.18 - (0.005 * childrenyes))))
        if childrenyes>36:
            print(f"your net salary is: ${salary}")
        else:
            print(f"your net salary is: ${net_salary}")
else:
    if salary < 1000:
        net_salary= float(salary-(salary*(0.1*salary)))
        print(f"your net salary is: ${net_salary}")
    elif 1000<= salary < 2000:
        net_salary = float(salary - (0.12 *salary))
        print(f"your net salary is: ${net_salary}")
    elif 2000 <=salary< 4000:
        net_salary = float(salary - (0.14 *salary))
        print(f"your net salary is: ${net_salary}")
    elif salary >= 4000:
        net_salary = float(salary - (0.18 *salary))
        print(f"your net salary is: ${net_salary}")