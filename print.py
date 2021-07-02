import json

f = open('zoom_links.json', 'r')
links = json.load(f)
print(links['links']['ICS123'])
