import json

f = open('k리그.json')
data = json.load(f)

posts = data['posts']

print(posts[0]['like_count'])
print(posts[0]['tags'])

print(posts[1]['like_count'])
print(posts[1]['tags'])
