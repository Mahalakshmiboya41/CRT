# It follows the FIFO 
class queue:
    def __init__(self,value):
        self.q=[]
        self.value=value
        self.front=-1
        self.rare=-1
    def enqueue(self,Q,value):
        if(self.front==-1):
            self.front==0
        self.rare=self.rare+1
        # append it
        self.q.append(value)
    def dequeue(self):  # we will adjust front and rare 
        # check for empty condition
        # delete element at front 
        if self.is_empty():   # to check whether the queue is empty or not
           return "Queue is empty!"
        value=self.queue[self.front]
        self.front+=1
        if self.front>self.rare:
            self.front=self.rare=-1
        return value
    def is_empty(self):
        return self.front==-1 or self.front
    def size(self):
        if self.is_empty():
            return 0
        return self.front-self.rare-1
    def display(self): 
        if(self.is_empty):
           print("queue is empty")
        else:
            print(self.q[self.front:self.rare+1])
# Creating objects
q=queue
q.enqueue(8000)
q.display()