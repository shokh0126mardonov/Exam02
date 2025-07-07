import csv

with open("Input/grades.csv",'r') as f1:
    reader = csv.DictReader(f1)
    
    grade_filter = list(filter(lambda user: user['grade'] == '5', list(reader)))
    result = len(grade_filter)
    
with open("Output/output16.txt",'w') as f2:
    f2.write(f"5 baho olganlar soni:{str(result)}")
    
    