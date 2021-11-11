class Stack:
    def __init__(self):
        self.stack = []
        
    def  push(self,num):
        self.stack.append(num)

    def delete(self):
        self.stack.pop()

    def display(self):
        print(self.stack)

    def peek(self):
        print(self.stack[-1])
    
    def isEmpty(self):
        return self.stack == []


a = Stack()

a.push(4)
a.push(78)
a.push(1)
a.push(2)
a.display()
a.peek()

#сортировка стека

def sort_stack(s):
    t = []                            
    while s:                          
        x = s.pop()
        while t and t[-1] > x:        
            s.append(t.pop())         
        t.append(x)                   
    return t
