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
cdll.prepend(5)
cdll.prepend(4)
cdll.prepend(3)
cdll.prepend(2)
cdll.prepend(1)

cdll.printList()
print()
print("Head: ", cdll.head.data)
print("Head.Next: ", cdll.head.next.data)
print("Head.Prev: ", cdll.head.prev.data)
print("Tail: ", cdll.tail.data)
print("Tail.Next: ", cdll.tail.next.data)
print("Tail.Prev: ", cdll.tail.prev.data)