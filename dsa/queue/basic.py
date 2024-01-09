class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        
        self.queue.pop(0)

    def display_queue(self):
        print('Your queue : ', self.queue)


q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)

q1.display_queue()

q1.dequeue()
q1.display_queue()