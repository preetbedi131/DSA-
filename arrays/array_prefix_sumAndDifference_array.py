"""you have an array of size n (initially all zeros). You’ll be given q spells. Each spell adds k health to every warrior in positions [l, r]. After all spells, print the final health of each warrior.
"""


n,q = map(int,input().split())
arr = [0] * (n+2)
spells = [list(map(int,input().split())) for i in range(q)] 
for l, r, k in spells:
    arr[l] = arr[l] + k   # intial marker 
    arr[r+1] = arr[r+1] - k # end + 1 marker to stop the propogation using prefix sum

sum = 0 
lis = []        
for i in range(len(arr)): 
    sum = sum + arr[i]  
    lis.append(sum)
print(lis)    
"""
[0,0,0,0,0,0,0]
2 4 100: [0,0,100,0,0,-100,0]  p = [0 0 100 100 100 0 0 ]
3 5 100: [0,0,100,100,0,-100,-100] p = [0 0 100 200 200 100 0 ] """
3 4 100: [0,0,100,200,0,-200,-100] p = [0 0 100 300 300 100 0]  
