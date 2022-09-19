n=[2,3,5,0,5,0]
x=sum(n)/len(n)
for i in range(len(n)):
    if n[i]==0: n[i]=x
print('list ',n)
