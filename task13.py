import json
with open("Input/students.json",'r') as f1:
    students = json.loads(f1.read())
    new_list =[]
    for student in students:
        if len(student['name']) > 5:
            new_list.append(student['name'])
            
    korinish = {"long_names":new_list}
    
    dump_file = json.dumps(korinish,indent=4)
with open("Output/output13.json",'w') as f2:
    f2.write(dump_file)