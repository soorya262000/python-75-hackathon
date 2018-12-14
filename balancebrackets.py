def matched(exp):
    s=[]
    for e in exp:
        if(e=='{' or e=='[' or e=='('):
            s.append(e)
        if(e=='}' or e==']' or e==')'):
            if len(s)==0:
                return 0
            elif(not ismatch(s.pop(),e)):
                return 0
    if len(s)==0:
        return 1
    else:
        return 0
def ismatch(a,b):
    if(a=='{' and b=='}'):
        return 1
    elif(a=='[' and b==']'):
        return 1
    elif(a=='(' and b==')'):
        return 1
    else:
        return 0
expression=input("enter the bracket string")
result=matched(expression)
if result:
    print("matched")
else:
    print("mismatch")
    
                
            
    
