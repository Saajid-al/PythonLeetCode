class node:
    def __init__(self,data = None):
        self.data = data #data
        self.next = None #next



class linkedList:
    def __init__(self):
        self.head = None    

    def addNode(self, data):
        newNode = node(data) #have the new node set to a node.
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = newNode 
        else:
            currentNode = self.head #we set the current Node to the head so we can traverse
            while currentNode.next is not None:  # Traverse to the end of the list
                currentNode = currentNode.next
            currentNode.next = newNode  # Add the new node at the end
     
    def printData(self):
        currentNode = self.head
        
        while currentNode!=None:
            print(currentNode.data)
            currentNode = currentNode.next

    def printHead(self):
        print(self.head.data)
        
    def insert(self, data, index):
        val = 0
        newNode = node(data)
        currentNode = self.head
        while currentNode != index:
            val += 1
            currentNode = currentNode.next
        currentNode.next = newNode


        #[2] [3] [4]
        #1  2   3

    def addNodeBeginning(self, data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode

        return self.head
        #what do we want to do
        # [0] ->    [1]->[2]->[3]
        # []
        # while currentNode.next is not None:  # Traverse to the end of the list
        #     currentNode = currentNode.next
        # currentNode.next = newNode  # Add the new node at the end


                   
p = linkedList()
p.addNode(5)
p.addNode(4)
p.addNode(2)
p.addNodeBeginning(120)
p.addNodeBeginning(230)
p.addNode(2)
p.addNode(2)
p.printData()
