import re
f=open('allvalid2011 (detailed titles headings).txt',encoding='latin_1')

icd10={}

for line in f.readlines() :
    m=re.search('([A-Z]＼d+|[A-Z]＼d+＼.＼)＼s+"?(.*[^"])"?$',line.rstrip()) #코드검토
    if m :
        icd10[m.group(1)]=m.group(2)

print(icd10)

