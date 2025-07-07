with open("Input/numbers.txt",'r') as f1:
    numbers = f1.read().split()
    tartiblangan = sorted(map(int,numbers),key=lambda x:x,reverse=False)
    
    
with open("Output/output10.txt",'w') as f2:
    for i in tartiblangan:
        f2.write(f"{i}\n")