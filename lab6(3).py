D=[0, 1,  3, 5, 10, 7];
 
print(sum(x for i,x in enumerate(D) if i % 2 == 1))
print([2*x if x < 15 else x for x in D])
