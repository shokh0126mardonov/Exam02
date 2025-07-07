def add(a, b):
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Bo'linuvchi nolga teng bo'lishi mumkin emas"

print("Sonlarni kiriting(a + b)")
num1 = int(input("Son 1 :"))
amal = input("Amalni kiriting ")
num2 = int(input("Son 2 :"))

if amal == '+':
    print(add(num1,num2))
    
elif amal == '-':
    print(subtract(num1,num2))
    
elif amal == '*':
    print(multiply(num1,num2))
    
elif amal == '/':
    print(divide(num1,num2))