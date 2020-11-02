# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
N = int(raw_input())
data = sys.stdin.readlines()

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=1)
tfidf = vectorizer.fit_transform(data)
sim = (tfidf * tfidf.T)

usedA = set()
usedB = set()
solution = dict()

vals = [(-sim[i,N+1+j], i, j) for i in range(N) for j in range(N)]

for v,i,j in sorted(vals):
    #print v,i,j
    if i in usedA or j in usedB: continue
    usedA.add(i)
    usedB.add(j)
    solution[i]=j

for i in range(N):
    print solution[i]+1
