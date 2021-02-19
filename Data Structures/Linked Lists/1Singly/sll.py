#1. addFirst()
#2. addLast()
#3. addBefore()
#4. addAfter();
#5. indexOf()
#6. contains()
#7. removeFirst()
#8. removeLast()
#9. removeAt()
#10 removeAll()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,):
        self.first = None
        self.last = None

    def printLinkedList(self):
        if self.first is self.last is None:
            print("linked list is empty")
        else:
            current = self.first
            while current:
                print(current.data, "=>", end=" ")
                current = current.next

    def addFirst(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.first = self.last = newNode
        else:
            newNode.next = self.first
            self.first = newNode

    def addLast(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

    def addBefore(self, dataAfter, data):
        newNode = Node(data)
        if self.first == self.last and self.first.data == dataAfter:
            self.prepend(data)
            return
        current = self.first
        while current:
            if current.data == dataAfter:
                prv = self.__getPrevious(self.last)
                prv.next  = newNode
                newNode.next = current
            current = current.next

    def addAfter(self, nodeInfront, data):
        newNode = Node(data)
        current = self.first
        while current:
            if current.data == nodeInfront:
                break
            current = current.next
        if current is None:
            print(f"Node {nodeInfront} is not found in the list")
        else:
            newNode.next = current.next
            current.next = newNode

    def indexOf(self, item):
        index = 0
        current = self.first
        while current is not None:
            if current.data == item:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self,item):
        return self.indexOf(item) != -1

    def removeFirst(self):
        if self.__isEmptyList():
            print("The list is empty!")
            return -1
        if self.first == self.last:
            self.first = self.last = None
            return
        tempNode = self.first.next
        self.first.next = None
        self.first = tempNode

    def removeLast(self):
        if self.__isEmptyList():
            print("The list is empty!")
            return -1
        if self.first == self.last:
            self.first = self.last = None
            return
        previous = self.__getPrevious(self.last)
        last = previous
        last.next = None

    def __getPrevious(self, node):
        current = self.first
        while current is not None:
            if current.next == node:
                return current
            current = current.next

    def __isEmptyList(self):
        return self.first == None

sll = LinkedList()
sll.addLast(5)
sll.addLast(10)
sll.addFirst(1)
sll.addLast(20)
sll.addFirst(100)
sll.addAfter(100, 15)
sll.printLinkedList()
sll.addBefore(20, 200)
print(f"\nContains {200}: ", sll.contains(200))
print(f"Index Of {200}: ", sll.indexOf(200))
#sll.removeFirst()
#sll.removeLast()

sll.printLinkedList()
