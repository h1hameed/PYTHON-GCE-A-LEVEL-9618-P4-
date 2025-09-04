# Queue implementation using Python list (FIFO)

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        return self.items


if __name__ == "__main__":
    q = Queue()
    q.enqueue("Taha")
    q.enqueue("Ali")
    q.enqueue("Amjad")
    print("Queue:", q.display())
    q.dequeue()
    print("After Dequeue:", q.display())
