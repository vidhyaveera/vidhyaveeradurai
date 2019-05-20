class node:
    def __init__(self,d):
        self.data=d
        self.nextt=None
class stack:
    def __init__(self):
        self.head=None
    def printstack(self):
        temp=self.head
        while(temp!=None):
            print("|",temp.data,"|")
            print(" ----")
            temp=temp.nextt
        print("None")
       
    def push(self):
        print("Enter the value")
        data=input()
        temp=node(data)
        if(self.head!=None):
            temp.nextt=self.head
            self.head=temp
        else:
            self.head=temp
        self.printstack()
    def pop(self):
        temp=self.head
        if temp==None:
            print("there is no element in stack to delete")
        else:
            self.head=self.head.nextt
            temp.nextt=None
        self.printstack()
obj=stack()
ch=0
while ch!=4:
    print("###Stack Implementation###")
    print("1.Push into stack 2.pop from stack 3.display stack 4.exit")
    ch=int(input())
    if ch==1:
        obj.push()
    elif ch==2:
        obj.pop()
    elif ch==3:
        obj.diplay()
