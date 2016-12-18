import re

pattern = re.compile(r'(\w+ed)\b')
file = open('newnewnew.txt', 'r')
short_file = open('new.txt', 'w+')
lines = file.readlines()
for i in lines:
    result = re.findall(pattern, i)
    if not result:
        print(result)
        short_file.write(i)

file.close()
