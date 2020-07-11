
a = list(map(int,input().split()))
k = list(map(int,input().split()))
u = list(map(int,input().split()))
t = []

for i in k:
    for j in u:
        if i+j<=a[0]:
            t.append(i+j)
if len(t) == 0:
    print("-1")
else:
    print(max(t))
 
 
