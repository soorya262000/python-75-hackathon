import string
def ccount(strin):
    d={}
    translator=str.maketrans("","",string.punctuation)
    for letter in strin.translate(translator).lower():
      d[letter]=d.get(letter,0)+1
    print(d.items())
strin=input("enter the string")
ccount(strin)
            
