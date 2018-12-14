print(""" It's fun to learn "Python" """)#usage of ""&'' in the string
#printing varaibles using various techniques
a=10
b=5
print("the value of a is:",a,"the value of b is :",b)
print("the value of a is:%d the value of b is :%d"%(a,b))
print("the value of a is:{0} the value of b is :{1}".format(a,b))
#getting values from the user
c=input("enter a value for the variable c")#python by default sees the keyboard input as string
print(c)
print(type(c))
d=input("enter a value for the variable d")
print(c+d)#as it is a string,instead of addition string concatenation takes place
#to add the above to numbers eval() function can be used
print("usage of eval()",eval("3+2"))
# or casting may be used while getting input from the user
x=int(input("enter the value for x"))
y=int(input("enter the value for y"))
print("sum of x and y",x+y)
#a string representing a binary number can be casted to a integer
n="100"
m=int(n,2)
print("the integer equivalent of",n,"is",m)






 
