import csv

with open("Input/grades.csv",'r') as f1:
    reader = csv.DictReader(f1)
    maksimum = max(reader,key=lambda user:user['grade'])
    

with open("Output/output15.txt",'w') as f2:
    f2.write(f"Bahosi eng yuqori o'quvchi: {maksimum['name']}-{maksimum['grade']}")