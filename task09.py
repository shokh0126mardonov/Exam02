with open("Input/numbers.txt",'r') as f1:
    numbers = f1.read().split()
    yigindi = max(map(int,numbers))

with open("Output/output09.txt",'w') as f2:
    f2.write(str(yigindi))