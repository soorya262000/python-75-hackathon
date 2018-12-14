l=[]
length=int(input("enter the size of the list"))
for i in range(length):
    l.append(int(input("enter value {} :".format(i+1))))#use of append function
summ=0
for x in l:
    summ=summ+x
print("the sum of the list elements is :",summ)    
    
