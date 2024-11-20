import re
from sys import stdin

stipendia = []
for students in stdin:
    if not re.findall(r".* (.)\.\1\. P3111", students):
        stipendia.append(students)
print(*[i for i in stipendia], sep='')
