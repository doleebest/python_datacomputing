import unicodedata
import json
from unicodedata import normalize

f = open('k리그.json')
data = json.load(f)

tags = []
posts = data['posts']

for p in posts :
    for t in p['tags'] :
        L=p['like_count']
        tags.append([L,normalize('NFC',t).lower()])


rank = {}


for (l.t) in tags :
    if not t in rank :
        rank[t] = 0

    rank[t]+= 1

L = sorted(rank.items(), key=itemgetter(1), reverse=True)

print('count', len(tags))
print('tags', len(L))

for (t,l) in L[:30] :
    print(l,t)
