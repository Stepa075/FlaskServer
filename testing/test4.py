
lines1 = []
with open('list_of_objects.txt', 'r') as fp:
    for n, line in enumerate(fp, 1):
        line = line.rstrip('\n')
        lines1.append(line)

print(lines1)
