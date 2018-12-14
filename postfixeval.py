def evaluate(postfix):
    a=[]
    for ch in postfix:
        if ch.isnumeric():
            a.append(int(ch))
        else:
            c=a.pop()
            b=a.pop()
            if ch=='+':
                a.append(b+c)
            elif ch=='-':
                a.append(b-c)
            elif ch=='*':
                a.append(b*c)
            elif ch=='/':
                a.append(b/c)
    print("the answer is\t",a[0])
postfix=input("enter the postfix expression")
evaluate(postfix)
                
            
            
