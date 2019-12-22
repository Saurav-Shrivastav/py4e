name = input("Enter File :")
try :
    fhand = open(name)
except :
    print("Enter Correct file name.")
    exit()

counts = dict()

for line in fhand :
    line.strip()
    if line.startswith('From '):
        words = line.split()
        s = words[5]
        f = s[:2]
        counts[f] = counts.get(f, 0) + 1

sortc = sorted( counts.items() )

for k, v in sortc :
    print(k, v)
