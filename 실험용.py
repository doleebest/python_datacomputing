import re

text_phone = 'His name is song and phone number is 010-1234-5678'

m=re.search('name is (.*) and', text_phone)

print (m.group(1))
