import string
def ccount(filename):
    translator=str.maketrans('','',string.punctuation)
    f=open(filename,'r')
    lines=f.readlines()
    f.close()
    f1=open(filename,'w')
    for line in lines:
        f1.write(line.translate(translator).lower())        
    f1.close()


fname=input("enter the name of the file")
ccount(fname)
print("punctuation marks have been removed from {}".format(fname))
    
