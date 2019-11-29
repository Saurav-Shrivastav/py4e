fname = input("Enter file name: ")
fh = open(fname)
avg = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    count = count + 1
    beg = line.find('0')
    line = line.rstrip()
    line = line[beg:]
    avg = avg + float(line)
avg = (avg/count)
print('Average spam confidence:', avg)
