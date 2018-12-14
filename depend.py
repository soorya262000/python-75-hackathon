def depend(dicto):
    a=[]
    b=len(dicto)
    print(b)
    while len(a)!=b:
        fl=0
        for x in dicto.copy():
            if len(dicto.get(x))==0:
                a.append(x)
                del dicto[x]
            else:
                for y in dicto.get(x):
                    if y in a:
                        fl=fl+1
                if fl==len(dicto.get(x)):
                    a.append(x)
                    del dicto[x]
    print(a)
    
pack=int(input("enter the no of packages to be installed"))
d={}
for i in range(pack):
    pa=input("enter the package name")
    de=int(input("enter the no of dependecy"))
    x=[]
    for j in range(de):
        dee=input("enter the name of the dependency")
        x.append(dee)
    d[pa]=x    
        
depend(d)    
