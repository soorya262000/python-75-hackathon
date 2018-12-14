l=[1,2,3,4,5,6,7]
print("the list is :",l)
print("a slice of list l :l[1:4]--prints 2,3,4",l[1:4])
print("a slice of list l :l[1:6:2]--prints 2,4,6--here 2 indicates the steps",l[1:6:2])
#use of slice function
print("[1:6:2] can be given a name with slice function")
print("sl=slice(1,6,2)")
sl=slice(1,6,2)
print(" l[sl] prints the same result",l[sl])
