import json
m = []
import sys
ending = sys.argv[1]
for i in json.load(open("english_words.json"))['words']:
    if i.endswith(ending):
        m.append(i)


for i in sorted(m, key=len):
    print(i)
        
