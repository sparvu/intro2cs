from queue import Queue
q = Queue()
q.put(1) # Add 1 to queue
q.put(2)
q.put(3)
print(q.qsize()) # Prints 3
print(q.get()) # Prints 1
print(q.get()) # Prints 2
