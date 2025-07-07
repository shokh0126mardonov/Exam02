import json

with open("Input/students.json",'r') as f1:
    students = json.loads(f1.read())
    new_list = []
    for student in students:
        new_list.append(student['name'])
        
new_list.sort()
dump_file = json.dumps(new_list,indent=4)
with open("Output/output12.json",'w') as f2:
    f2.write(dump_file)