#1. prepend()
#2. append()
#3. addBefore(data1, data2);
#3. addAfter(data1, data2);
#4. indexOf(data)
#5. contains(data)
#6. removeFirst()
#7. removeLast()
#8. removeWithData(data)
#8. removeNthNode(node)
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

    # prints all data in the list
    def printList(self):
        if self.__isEmptyList():
            print("The List is Empty!")
        else:
            current = self.head
            while current:
                print(f"{self.__colors('red')} <-]{self.__colors('reset')}[{current.data}]",
                      end=f"{self.__colors('red')}[-> {self.__colors('reset')}")
                current = current.next
                if current == self.head:
                    return

    # Adds node in front of the list ( addFirst() )
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

    # Adds node at the end of the list ( addLast() )
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

    # Adds node before a given node
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

    # Adds node after a given node
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

    # Finds the index of a given node in the list
    def indexOf(self, data):
        index = 0
        current = self.head
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    # Checks if a given node is in the list
    def contains(self, data):
        return self.indexOf(data) != -1

    # Removes the 1st node in the list
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

    # Removes the last node in the list
    def removeLast(self):
        if self.__isEmptyList():
            return -1
        if self.head == self.tail:
            self.head = self.tail = None
            return
        previous = self.tail.prev
        head = self.tail.next
        self.tail.prev = None
        self.tail.next = None
        previous.next = head
        self.head.prev = previous
        self.tail = previous

    ## Removes the node with a given data
    def removeWithData(self, nodeData):
        if self.__isEmptyList():
            return
        if self.head.data == nodeData:
            self.removeFirst()
            return
        if self.tail.data == nodeData:
            self.removeLast()
            return
        if self.contains(nodeData):
            curr = self.head
            while curr.next != self.head:
                if curr.data == nodeData:
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

    ## Removes node from the list ( eg: 1st node, 2nd node, ...50th node ...)
    def removeNthNode(self, n):
        if n <= self.__getLength():
            if self.__isEmptyList():
                return

            if n == 1:  # 1st node in the list
                self.removeFirst()
                return

            if n == self.__getLength():  # last node in the list
                self.removeLast()
                return

            curr = self.head
            while curr.next != self.head:
                if self.indexOf(curr.data)+1 == n:
                    break
                curr = curr.next

            self.removeWithData(curr.data)
        else:
            return

    # Removes all duplicates in the list
    def removeDuplicates(self):
        current = self.head
        while current:
            p1 = current
            p2 = current.next
            while p2 != self.tail.next:
                if current.data == p2.data:
                    p1.next = p2.next
                else:
                    p1 = p2
                p2 = p2.next
            current = current.next
            if current.next == self.head:
                break

    # Reverses the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Finds all the pairs that sum up to a given target
    def pairsWithSum(self, target):
        pairs = []
        p1 = self.head
        while p1 != self.tail:
            p2 = p1.next
            while p2 != self.head:
                if p1.data + p2.data == target:
                    pairs.append([p1.data, p2.data])
                p2 = p2.next
            p1 = p1.next
        return pairs

    # Finds the total number of nodes in the list
    def __getLength(self):
        return self.indexOf(self.tail.data)+1

    # Finds the previous to the current node
    def __getPrevious(self, node):
        current = self.head
        while current:
            if current.next == node:
                return current
            current = current.next

    # Checks if the list is empty
    def __isEmptyList(self):
        return self.head == None

    # Defines a colour dictionary
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
cdll.append(20)
cdll.append(30)
cdll.append(50)
cdll.append(30)
cdll.append(10)


print()
cdll.printList()
cdll.removeDuplicates()
print()
cdll.printList()
print()

if cdll.head:
    print()
    print("Head: ", cdll.head.data)
    print("Head.Next: ", cdll.head.next.data)
    print("Head.Prev: ", cdll.head.prev.data)
    print("Tail: ", cdll.tail.data)
    print("Tail.Next: ", cdll.tail.next.data)
    print("Tail.Prev: ", cdll.tail.prev.data)

