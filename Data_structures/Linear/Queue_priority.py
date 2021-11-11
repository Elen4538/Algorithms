class prior_queue:
    def __init__(self):
        self.queue = []
    
    def display(self):
        print(self.queue)
    
    def insert(self,num):
        self.queue.append(num)

    def isempty(self):
        return len(self.queue)==0

    def delete_elem(self):
        max = 0
        for i in range(len(self.queue)): # ищем число с высшим приоритетом
            if self.queue[i] > self.queue[max]:
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item

myQueue = prior_queue()
myQueue.insert(12)
myQueue.insert(1)
myQueue.insert(14)
myQueue.insert(7)
myQueue.display()

while not myQueue.isempty():
        print(myQueue.delete_elem()) 
