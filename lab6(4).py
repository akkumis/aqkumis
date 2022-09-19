x=[3,4,6,7,5,4]
d=[]
for i in range(len(x)):
    if i%2==0:
        d.append(x[i])
d.sort(reverse=True)
print(d)
