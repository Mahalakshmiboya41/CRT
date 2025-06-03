class Node: # We just created a node here
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None #Staring point of linked list(First we give and take care of the other nodes later)
    def insert(self,data): #To insert the data we have to first create a node 
        new_node=Node(data) #We will pass the data from the main function and that is called here
        if(self.head is None):
            self.head=new_node #Link the new node to the head node
        else:
            temp=self.head
            while(temp.next):
               temp=temp.next # moves temp node for traversal
            temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end=",")
            temp=temp.next #To move the temp and print the data
        print("None")
    def add_l1(self):
        temp=self.head
        sum=0
        while temp:
            sum=sum+temp.data
            temp=temp.next
        return sum
    def count(self):
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count
    #def end_insert(self, data):
    # if not self.head:
     #    self.head = Node(data)
      # else:
       #  curr = self.head
        # while curr.next: curr = curr.next
         #curr.next = Node(data)

    def start_insert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def delete_beginning(self):
        self.head=self.head.next
    def delete_end(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
        temp.next=None
    def pos_insert(self,pos,data):
        if(pos==0):
            self.start_insert(data)
        else:
            new_node=Node(data)
            temp=self.head
            for _ in range(pos-1):
                if temp is None:
                    print("Position out of bounds")
                    return
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def pos_delete(self,pos,data):
        if(pos==0):
            self.start_insert(data)
        else:
            new_node=Node(data)
            temp=self.head
            for _ in range(pos-1):
                if temp is None:
                    print("Position out of bounds")
                    return
                temp=temp.next
            temp.next=temp.next.next
    def delete_value(self,value):
        if self.head.data==value:
            self.head=self.head.next
            return
        temp=self.head
        while temp.next and temp.next.data!=value:
            temp=temp.next
        if temp.next is None:
            print("Value not found")
            return
l1=LinkedList()
l1.insert(10)
l1.start_insert(20)
l1.start_insert(880)
l1.insert(30)
l1.pos_insert(2,59)
l1.pos_delete(3,40)
l1.display()
l1.delete_beginning()
l1.delete_end()
l1.delete_value(40)
l1.display()
print(l1.add_l1())
print(l1.count())


