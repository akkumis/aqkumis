mylist = []
num = int(input("telements: "))
for i in range(0,num):
    ele = int(input("Element: "))
    mylist.append(ele)
newlist = [] 
replist = []
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        replist.append(i)
print("List of duplicates", replist)
print("Unique Item List", newlist)
