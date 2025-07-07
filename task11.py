import json

with open("Input/students.json",'r') as f1:
    students_read = f1.read()
    students = json.loads(students_read)
    count = len(students)
    
    result = {
        "count":count
    }
    
    dump_file = json.dumps(result,indent=4)

with open("Output/output11.json",'w') as f2:
    f2.write(dump_file)