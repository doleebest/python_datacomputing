import re

text_phone = 'his phone number is 010-1234-5678'
n = re.search('(\d+)-(\d+)-(\d+)', text_phone)

print(n.group(1),n.group(2))
