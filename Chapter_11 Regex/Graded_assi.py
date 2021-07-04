import re

data = open('regex_sum_1295117.txt')
output = []

for line in data:
    line = line.rstrip()
    matches = re.findall('[0-9]+', line)
    matches = [int(match) for match in matches]
    output = output + matches

print(sum(output))
