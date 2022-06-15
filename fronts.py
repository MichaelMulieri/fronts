
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self, head):
        self.head = head

    def addFront(self, val):
        new_node = Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def front(self):
        if self.head:
            print(self.head.val)
        return self

    def removeFront(self):
        if self.head:
            self.head = self.head.next
        return self.head

    def display(self):
        runner = self.head
        while runner:
            print(runner.val)
            runner = runner.next
        return self

    def addBack(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self


firstList = SLL(Node(45))
firstList.addFront(100)
firstList.addFront("hello world!")
print(firstList.head.val)
print(firstList.head.next.next.val)
firstList.display()
firstList.removeFront()
firstList.display()
firstList.front()
firstList.addBack(899)
firstList.display()












