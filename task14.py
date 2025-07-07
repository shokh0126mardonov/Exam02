import json

with open("Input/students.json",'r') as f1:
    students = json.loads(f1.read())
    new_list = []
    for student in students:
        if student['name'].startswith("A"):
            new_list.append(student['name'])

    result = {
        "a_names":new_list
    }
    
    dump_file = json.dumps(result,indent=4)
    
with open("Output/output14.json",'w') as f2:
    f2.write(dump_file)