class Queue:
    def __init__(self):
        self.item = []

    def enque(self, elem):
        self.item.append(elem)
    
    def dequeue(self):
        if len(self.item) < 1:
            return None
        else:
            self.item.pop(0)

    def size(self):
        return len(self.item)

    def display(self):
        print(self.item)

q = Queue()
q.enque(5)
q.enque(10)
q.enque(34)
q.display()
q.dequeue()
q.display()
