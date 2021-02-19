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

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        if self.head == self.tail == None:
            print("The List is Empty!")
        else:
            current = self.head
            while current:
                print(current.data, "=>", end=" ")
                current = current.next
                if current == self.head:
                    return

    def prepend(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.head = self.tail = newNode
            self.head.next = self.tail.next = self.head
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.head = self.tail = newNode
            self.head.next = self.tail.next = self.head
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode

    def addBefore(self, dataAfter, data):
        if self.__isEmptyList():
            return
        newNode = Node(data)
        if self.head == self.tail and self.head.data == dataAfter:
            self.prepend(data)
            return
        current = self.head
        while current:
            if current.data == dataAfter:
                break
            current = current.next
        prev = self.__getPrevious(current)
        prev.next = newNode
        newNode.next = current

    def addAfter(self, dataBefore, data):
        if self.__isEmptyList():
            return
        newNode = Node(data)
        if self.head == self.tail and self.head.data == dataBefore:
            self.append(data)
            return
        curr = self.head
        while curr:
            if curr.data == dataBefore:
                break
            curr = curr.next
        tmp = curr.next
        curr.next = newNode
        newNode.next = tmp

    def __getPrevious(self, node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next

    def __isEmptyList(self):
        return self.head == None

csll = CircularSLL()
csll.prepend(2)

csll.printList()
print()
csll.addBefore(2, 13)
csll.addAfter(2, 7)

csll.printList()
print()