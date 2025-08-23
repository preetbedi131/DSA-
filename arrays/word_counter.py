"""You’re given n words. Then you’re given q queries, each a word.
For each query, print how many times that word appeared in the list.
Goal: Do it in O(n + q) using a dictionary instead of looping through the list every time.
    
6
apple
banana
apple
orange    3 2 0
banana
apple
3
apple
banana
grape"""

from collections import Counter
n = int(input())
words = [input() for _ in range(n)]
m = int(input())
queries = [input() for _ in range(m)]  
d = Counter(words)
li=[]
for i in queries:
    if i in d:
        li.append(d[i])
    else:
        li.append(0)
for i in li:
    print(i)
        
        
        
    
    

