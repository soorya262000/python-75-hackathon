class calculator:
    def __init__(self,op1,op2):
        self.a=op1
        self.b=op2
    def add(self):        
        return self.a+self.b
    def sub(self):     
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def divide(self):
        if(op2==0):
            return "division not possible"
        else:
            return self.a/self.b
op1=float(input("enter the first operand"))
op2=float(input("enter the second operand"))
ch=int(input("ENTER THE CHOICE 1.ADD..2.SUB..3.MUL..4.DIVIDE"))
c1=calculator(op1,op2)
if ch==1:
    print(c1.add())
elif ch==2:
    print(c1.sub)
elif ch==3:
    print(c1.mul)
elif ch==4:
    print(c1.divide)
        
    
        
        
