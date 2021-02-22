#1. addFirst()
#2. addLast()
#3. addBefore(data1, data2);
#3. addAfter(data1, data2);
#4. indexOf(data)
#5. contains(data)
#6. removeFirst()
#7. removeLast()
#8. removeAt(data)
#9. removeDuplicates()
#10. reverse()
#11. pairsWithSum()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        if self.head == self.tail == self.__isEmptyList():
            return
        current = self.head
        while current:
            print(f"\u001b[31m <-\u001b[0m{current.data}", end="\u001b[31m->\u001b[0m  ")
            current = current.next

    def prepend(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.head = self.tail = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.head = self.tail = newNode
        else:
            newNode.next = None
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def addBefore(self, dataAfter, data):
        newNode = Node(data)
        if self.head == self.tail and self.head.data == dataAfter:
            self.prepend(data)
            return
        current = self.head
        while current:
            if current.data == dataAfter:
                prv = current.prev
                prv.next = newNode
                current.prev = newNode
                newNode.next = current
                newNode.prev = prv
            current = current.next

    def addAfter(self, nodeBefore, data):
        newNode = Node(data)
        if self.head == self.tail and self.head.data == nodeBefore:
            self.append(data)
            return
        current = self.head
        while current:
            if current.data == nodeBefore:
                nxt = current.next
                nxt.prev = newNode
                current.next = newNode
                newNode.prev = current
                newNode.next = nxt
            current = current.next

    def removeFirst(self):
        if self.__isEmptyList():
            return -1
        if self.head == self.tail:
            self.head = self.tail = None
            return
        nxt = self.head.next
        self.head.next = None
        self.head = nxt

    def removeLast(self):
        if self.__isEmptyList():
            return -1
        if self.head == self.tail:
            self.head = self.tail = None
            return
        previous = self.__getPrevious(self.tail)
        last = previous
        last.next = None

    def removeWithData(self, data):
        current = self.head
        while current:
            if current.data == data and current == self.head:  # case 1
                if not current:
                    current = None
                    self.head = None
                    return
                else:   # case 2
                    nxt = current.next
                    current.next = None
                    current = None
                    self.head = nxt
                    return
            elif current.data == data:  # case 3
                if current.next:
                    nxt = current.next
                    prv = current.prev
                    prv.next = nxt
                    nxt.prev = prv
                    current.next = None
                    current.prev = None
                    current = None
                    return
                else:
                    prv = current.prev
                    prv.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def removeWithNode(self, node):
        current = self.head
        while current:
            if current.data == node and current == self.head:  # case 1
                if not current:
                    self.head = None
                    return
                else:  # case 2
                    nxt = current.next
                    current.next = None
                    self.head = nxt
                    return
            elif current == node:  # case 3
                if current.next:
                    nxt = current.next
                    prv = current.prev
                    prv.next = nxt
                    nxt.prev = prv
                    current.next = None
                    current.prev = None
                    return
                else:
                    prv = current.prev
                    prv.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def removeDuplicates(self):
        current = self.head
        checklist = []
        while current:
            if current.data not in checklist:
                checklist.append(current.data)
                current = current.next
            else:
                nxt = current.next
                self.removeWithData(current.data)
                current = nxt

    def reversed(self):
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def indexOf(self, data):
        index = 0
        current = self.head
        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, data):
        return self.indexOf(data) != -1

    def pairsWithSum(self, target):
        pairs = []
        p1 = self.head
        p2 = None
        while p1:
            p2 = p1.next
            while p2:
                if p1.data + p2.data == target:
                    pairs.append([p1.data, p2.data])
                p2 = p2.next
            p1 = p1.next
        return pairs

    def __getPrevious(self, node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next

    def __getPrevious(self, node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next

    def __isEmptyList(self):
        return self.head == None

dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(30)
dll.append(50)
dll.append(50)
dll.append(50)

dll.printList()
print()
dll.removeDuplicates()
dll.printList()
