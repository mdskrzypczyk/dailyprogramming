from sys import argv
import re
in_file = argv[1]
in_text = open(in_file).read()
in_text = re.sub('\|.*\|', '', in_text)
in_text = re.sub('\+.*\+', '', in_text)
in_text = re.sub('\|', '', in_text)
in_text = in_text.splitlines()
del in_text[0]
decolumned = ""
for line in in_text:
    line = line.strip()
    if len(line) == 0:
        decolumned += '\n'
        continue
    if line[len(line)-1] == '-':
        line = line[:len(line)-1]
    else:
        line += ' '
    decolumned += line

print decolumned
