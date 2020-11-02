import string, re

with open('t9Dictionary') as f:
    words = { word: 1 for word in re.findall(r'([a-zA-Z][a-zA-Z\-\']*[a-zA-Z])|[a-zA-Z]', f.read()) }

with open('t9TextCorpus') as f:
    for word in re.findall(r'([a-zA-Z][a-zA-Z\-\']*[a-zA-Z])|[a-zA-Z]', f.read()):
        if word in words:
            words[word] += 1

keys = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

for _ in xrange(input()):
    good = words
    for i,c in enumerate(raw_input()):
        good = filter(lambda s: i<len(s) and s[i] in keys[int(c)], good)
    print ';'.join(sorted(good, key=lambda s:(-words[s], s))[:5]) if len(good) else 'No Suggestions'
        