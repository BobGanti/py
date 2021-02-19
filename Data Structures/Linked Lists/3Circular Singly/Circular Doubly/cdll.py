#1. prepend()
#2. append()
#3. addBefore(data1, data2);
#3. addAfter(data1, data2);
#4. indexOf(data)
#5. contains(data)
#6. removeFirst()
#7. removeLast()
#8. removeAt(data)
#8. removeAt(node)
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
                print(f"{self.__colors('red')} <--{self.__colors('reset')} {current.data} ",
                      end=f"{self.__colors('red')}--> {self.__colors('reset')}")
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

    def removeLast(self):
        if self.__isEmptyList():
            return -1
        if self.head == self.tail:
            self.head = self.tail = None
            return
        previous = self.__getPrevious(self.tail)
        head = self.tail.next
        self.tail.prev = None
        self.tail.next = None
        previous.next = head
        self.head.prev = previous
        self.tail = previous

    def removeWithData(self, data):
        if self.__isEmptyList():
            return -1
        if self.head.data == data:
            if self.head == self.tail:  # delete head node with only 1 node in list
                self.head = self.tail = None
            else:   # delete head node with at least 2 nodes in list
                nxt = self.head.next
                prv = self.head.prev
                self.head.prev = None
                self.head.next = None
                nxt.prev = prv
                prv.next = nxt
                self.head = nxt
            return
        curr = self.head
        while curr.next != self.head:
            if curr.data == data:
                break
            curr = curr.next
        prv = curr.prev
        nxt = curr.next
        curr.next = None
        curr.prev = None
        prv.next = nxt
        nxt.prev = prv

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

    def removeNthNode(self, n):
        if self.__isEmptyList():
            return -1
        if n == 1:
            self.removeFirst()
            return
        if n == self.__lengthLl():
            self.removeLast()
            return
        curr = self.head
        while curr.next != self.head:
            if self.indexOf(curr.data)+1 == n:
                break
            curr = curr.next
        self.removeWithData(curr.data)

    def removeDuplicates(self):
        current = self.head
        checks = dict()
        while current.next != self.head:
            if current.data not in checks:
                checks[current.data] = 1
                current = current.next
            else:
                nxt = current.next
                self.removeWithNode(current)
                current = nxt

    def reversedLl(self):
        prev = None
        current = self.head
        while current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def __lengthLl(self):
        return self.indexOf(self.tail.data)+1

    def __getPrevious(self, node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next

    def __isEmptyList(self):
        return self.head == None

    def __colors(self, color):
        colorDict = {
            "red": "\u001b[31m",
            "yellow": "\u001b[33m",
            "cyan": "\u001b[36m",
            "reset": "\u001b[0m"
        }
        return colorDict[color]

cdll = CircularDLL()
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
cdll.append(50)

cdll.printList()
print()
cdll.reversedLl()
cdll.printList()


# if cdll.head:
#     print()
#     print("Head: ", cdll.head.data)
#     print("Head.Next: ", cdll.head.next.data)
#     print("Head.Prev: ", cdll.head.prev.data)
#     print("Tail: ", cdll.tail.data)
#     print("Tail.Next: ", cdll.tail.next.data)
#     print("Tail.Prev: ", cdll.tail.prev.data)

