# Singly Linked List implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def display(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        return nodes


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    print("Linked List:", ll.display())
    ll.delete(20)
    print("After Deletion:", ll.display())
    print("Search 10:", ll.search(10))
