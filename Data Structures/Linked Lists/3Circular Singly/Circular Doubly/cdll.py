#1. prepend()
#2. append()
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

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def printList(self):
        if self.head == self.tail == None:
            print("The List is Empty!")
        else:
            current = self.head
            while current:
                print(f"{self.colors('cyan')} <--{self.colors('reset')} {current.data} ", end=f"{self.colors('cyan')}--> {self.colors('reset')}")
                current = current.next
                if current == self.head:
                    return

    def prepend(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.head = self.tail = newNode
            self.head.next = self.tail.next = self.head
            self.head.prev = self.tail.prev = self.head
        else:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.__isEmptyList():
            self.head = self.tail = newNode
            self.head.next = self.tail.next = self.head
            self.head.prev = self.tail.prev = self.head

        else:
            newNode.next = self.head
            newNode.prev =self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode

    def addBefore(self, dataAfter, data):
        if self.__isEmptyList():
            return

        if self.head.data == dataAfter:
            self.prepend(data)
            return

        newNode = Node(data)
        current = self.head
        while current.next != self.head:
            if current.data == dataAfter:
                break
            current = current.next
        prv = self.__getPrevious(current)
        prv.next = newNode
        current.prev = newNode
        newNode.next = current
        newNode.prev = prv


    def addAfter(self, dataBefore, data):
        if self.__isEmptyList():
            return

        newNode = Node(data)
        if self.head.data == dataBefore:
            if self.head == self.tail:  # /* only 1 node in list
                self.append(data)
            else:   # /* at least 2 nodes in list
                temp = self.head.next
                self.head.next = newNode
                newNode.prev = self.head
                temp.prev = newNode
                newNode.next = temp
            return

        curr = self.head
        while curr.next != self.head:
            if curr.data == dataBefore:
                break
            curr = curr.next
        tmp = curr.next
        curr.next = newNode
        tmp.prev = newNode
        newNode.prev= curr
        newNode.next = tmp

    def indexOf(self, data):
        index = 0
        current = self.head
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self, data):
        return self.indexOf(data) != -1

    def removeFirst(self):
        if self.__isEmptyList():
            return -1
        if self.head == self.tail:
            self.head = self.tail = None
            return
        nxt = self.head.next
        prv = self.head.prev
        self.head.next = None
        self.head.prev = None
        nxt.prev = prv
        prv.next = nxt
        self.head = nxt

    def __getPrevious(self, node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next

    def __isEmptyList(self):
        return self.head == None

    def colors(self, color):
        colorDict = {
            "red": "\u001b[31m",
            "yellow": "\u001b[33m",
            "cyan": "\u001b[36m",
            "reset": "\u001b[0m"
        }
        return colorDict[color]

cdll = CircularDLL()
cdll.append(1)
cdll.append(2)
cdll.append(3)
cdll.append(5)
cdll.addBefore(5, 4)

cdll.printList()
print()
print("Index of 5: ", cdll.indexOf(5))
print("Contains 5: ", cdll.contains(5))
cdll.removeFirst()

cdll.printList()

print()
print("Head: ", cdll.head.data)
print("Head.Next: ", cdll.head.next.data)
print("Head.Prev: ", cdll.head.prev.data)
print("Tail: ", cdll.tail.data)
print("Tail.Next: ", cdll.tail.next.data)
print("Tail.Prev: ", cdll.tail.prev.data)

