def calculate_tax(salary):
    if salary > 5_000_000:
        soliq = salary * 0.2
    else:
        soliq = salary * 0.13
        
    return soliq

def calculate_net_salary(salary):
    net_salary = salary - calculate_tax(salary)
    return net_salary

salary = float(input("Maoshingizni kiriting = "))

print(f"Sizdan ushlanadigan soliq miqdori : {calculate_tax(salary):,.2f}")

print(f"Sof maoshingiz : {calculate_net_salary(salary):,.2f}")