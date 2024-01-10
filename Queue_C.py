class Queue_C:
    def __init__ (self,k):
        self.k=k
        self.queue=[None]*k
        self.front=-1
        self.rear=-1

#اضافه کردن به کلاس صف چرخشی
    def insqueue_C(self,data):
        if (self.rear+1)%k==self.front:
            print('Full')
        
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=data

        else:
            self.rear+=1
            self.queue[self.rear]=data

#حذف از کلاس صف چرخشی
    def delqueue_C(self):
        if self.front==-1:
            print('empty')

        elif self.front==self.rear:
            t=self.queues[self.front]
            self.front=-1
            self.rear=-1
            return t 
        
        else:
            t=self.queue[self.front]
            self.front=(self.front+1)%k 
            return t