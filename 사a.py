import unicodedata
import json
from unicodedata import normalize

f = open('k리그.json')
data = json.load(f)

posts = data['posts']

tags = []
for p in posts :
    for t in p['tags'] :
        tags.append(normalize('NFC',t).lower())


S = set(tags)

rank = []

for t in S :
    rank.append([tags.count(t), t])

rank.sort(reverse=True)

print('count', len(tags))
print('tags', len(rank))

for (c,t) in rank[:30] :
    print(c,t)
