sonastik = {}
file=open("TextFile1.txt",'r')
for line in file:
    k, v=line.strip().split('-')
    sonastik[k.strip()] = v.strip()

print(sonastik)