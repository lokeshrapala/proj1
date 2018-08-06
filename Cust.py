class Cust:
    """cust app"""
    cbname="sbi"
    def __init__(self,cname,cadd,cacno,cbal):
        self.cname=cname
        self.cadd=cadd
        self.cacno=cacno
        self.cbal=cbal
    def __str__(self):
        return self.cname+" "+self.cadd+" "+str(self.cacno)+" "+str(self.cbal)+" "+Cust.cbname
    def deposit(self,damt):
        self.cbal=self.cbal+damt
    def withdraw(self,wamt):
        self.cbal=self.cbal-wamt
    def display(self):
        print(self.cname)
        print(self.cadd)
        print(self.cacno)
        print(self.cbal)
        print(Cust.cbname)
c1=Cust("ravana","srilanka",1001,100000.00)
c2=Cust("sita","india",1002,1000.00)
c3=Cust("blake","dallas",1003,3000.00)
x=[c1,c2,c3]
print("before sorting")
for p in x:
    print(p)
#print("after sorting")
#x.sort(key=lambda c:c.cname,reverse=True)
#for q in x:
   # print(q)
#print("end")
        
