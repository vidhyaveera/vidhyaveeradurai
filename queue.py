class node:
    def __init__(self,d):
        self.data=d
        self.nextt=None
class queue:
    def __init__(self):
        self.head=None
    def printqueue(self):
        temp=self.head
        while(temp!=None):
            print(temp.data,"",end="")
            temp=temp.nextt
        print("None")
    def insert(self):
        print("Enter the vlue of node")
        data=input()
        temp1=node(data)
        temp=self.head
        if(self.head!=None):
            while(temp.nextt!=None):
                temp=temp.nextt
            temp.nextt=temp1
        else:
            self.head=temp1
        self.printqueue()
    def delete(self):
        temp=self.head
        self.head=self.head.nextt
        temp.nextt=None
        self.printqueue()
obj=queue()
ch=0
print("####Queue Implementation####")
while ch!=4:
    print("1.enter the queue 2.leave the queue 3.display queue 4.exit")
    ch=int(input())
    if ch==1:
        obj.insert()
    elif ch==2:
        obj.delete()
    elif ch==3:
        obj.printqueue()
