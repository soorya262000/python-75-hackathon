l=[1,2,4,3,2,1,6,5,4]
print("list :",l)
length=len(l)
a=[]
for x in l:
    if x not in a:
        a.append(x)
del l#use of del keyword
print("the new list :",a)
