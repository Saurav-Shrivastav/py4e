fhand = open("mbox-short.txt")
count = 0
for line in fhand :
    line.rstrip()
    if line.startswith('From:') :
        continue
    if line.startswith('From ') :
        words = line.split()
        # Guardian pattern - skips a line when it is blank.
        if len(words) < 1 :
            continue
        print(words[1])
        count = count + 1
print('There were', count, 'lines in the file with From as the first word')
