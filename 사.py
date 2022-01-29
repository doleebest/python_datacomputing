import unicodedata
import json
from unicodedata import normalize

f = open('k리그.json')
data = json.load(f)

posts = data['posts']

tags = []

for p in posts :
    for t in p['tags'] :
        tags.append(normalize('NFC',t).lower() )

print(len(tags))
print(tags[:30])
