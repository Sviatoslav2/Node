class Node(object):
    def __init__(self, data , next=None):
        self.data = data
        self.next = next
def writhe_list_to_node(lst):
    head = None
    lst = lst[::-1]
    for value in lst:
        head = Node(value, head)
    return head
def find_the_index_of_element(head ,value):
    n = 0
    while head != None:
        head = head.next
        n+=1
        if value == head.data:
            return n
def histogram(head):
    lst = []
    dct = {}
    while head != None:
        lst.append(head.data)
        head = head.next
    for i in lst:
        dct[i] = dct.get(i, 0) + 1
    return dct
def change(head,targetItem,newItem):
    probe = head
    while probe != None and targetItem != probe.data:
        probe = probe.next
    if probe != None:
        probe.data = newItem
    return head
def print_node(head):
    while head != None:
        print(head.data)
        head = head.next
def append_to_end(head,newItem):
    newNode = Node(newItem)
    if head is None:
        head = newNode
    else:
        probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = newNode
    return head
def remuve_from_begin(head):
    removedItem = head.data
    head = head.next
    return head
def remuve_from_end(head):
    removedItem = head.data
    if head.next is None:
        head = None
    else:
        probe = head
    while probe.next.next != None:
        probe = probe.next
    removedItem = probe.next.data
    probe.next = None
    return head
def append_to_playse(head,index,newItem):
    if head is None or index <= 0:
        head = Node(newItem, head)
    else:
        probe = head
        while index > 1 and probe.next != None:
            probe = probe.next
            index -= 1
    probe.next = Node(newItem,probe.next)
    return head
#####################################
#####################################
#####################################
lst = [1,2,3,4,5]
#head = writhe_list_to_node(lst)
#head = change(head,3,6)
#print_node(head)
#print("#################")
#append_to_end(head,8)
#print_node(head)
#print("#################")
#head  = remuve_from_begin(head)
#print_node(head)
#head = remuve_from_end(head)
#print("#################")
#print_node(head)
#print("#################")
#head = append_to_playse(head,2,10)
#print_node(head)
####################################
####################################
####################################
#Liste realisation by node##########
class NodlistX1 :
    def __init__(self, first = float("inf") ):
        self.first = first
        self.head = Node(self.first)
    def writhe_list_to_node(self,lst):
        self.head = None
        lst = lst[::-1]
        for value in lst:
            self.head = Node(value, self.head)
        return self.head
    def __str__(self):
        s = ""
        while self.head != None:
            s+=str(self.head.data) +"-->"
            self.head = self.head.next
        s = s + "end"
        return s
    def find_the_index_of_element(self, value):
        n = 0
        while self.head != None:
            self.head = self.head.next
            n += 1
            if value == self.head.data:
                return n
    def histogram(self):
        lst = []
        dct = {}
        while self.head != None:
            lst.append(self.head.data)
            self.head = self.head.next
        for i in lst:
            dct[i] = dct.get(i, 0) + 1
        return dct
    def change(self, targetItem, newItem):
        probe = self.head
        while probe != None and targetItem != probe.data:
            probe = probe.next
        if probe != None:
            probe.data = newItem
        return self.head
    def append_to_end(self, newItem):
        if self.head.data==self.first:
            newNode = Node(newItem)
            if self.head is None:
                self.head = newNode
            else:
                probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = newNode
            self.remuve_from_begin()
            return self.head
        else:
            newNode = Node(newItem)
            if self.head is None:
                self.head = newNode
            else:
                probe = self.head
            while probe.next != None:
                probe = probe.next
            probe.next = newNode

            return self.head
    def remuve_from_begin(self):
        removedItem = self.head.data
        self.head = self.head.next
        return self.head
    def append_to_playse(self, index, newItem):
        if self.head is None or index <= 0:
            self.head = Node(newItem, self.head)
        else:
            probe = self.head
            while index > 1 and probe.next != None:
                probe = probe.next
                index -= 1
        probe.next = Node(newItem, probe.next)
        return self.head
    def remuve_from_end(self):
        removedItem = self.head.data
        if self.head.next is None:
            self.head = None
        else:
            probe = self.head
        while probe.next.next != None:
            probe = probe.next
        removedItem = probe.next.data
        probe.next = None
        return self.head
    def iterator(self):
        while self.head != None:
            yield (self.head.data)
            self.head = self.head.next
    def node_to_list(self):
        return [i for i in self.iterator()]
    def append_to_begin(self,NewItem):
        if self.head.data==self.first:
            newNode = Node(NewItem)
            newNode.next = self.head
            self.head = newNode
            self.remuve_from_end()
        else:
            newNode = Node(NewItem)
            newNode.next = self.head
            self.head = newNode
##############################################
##############################################
##############################################
##############################################
##############################################
##############################################
class Node(object):
    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next
class TwoWayNode(Node):
    def __init__(self, data, previous = None, next = None):
        """Instantiates a TwoWayNode."""
        Node.__init__(self, data, next)
        self.previous = previous
class NodelistX2:
    def __init__(self,first = 0 ):
        self.head = TwoWayNode(first)
    def writhe_list_to_nodeX2(self,lst):
        lst = lst[::-1]
        self.previous = self.head
        for data in lst:
            self.previous.next = TwoWayNode(data,self.previous)
            self.previous = self.previous.next
        return self.head
    def append_to_end(self,data):
        self.head.next = TwoWayNode(data, self.previous)
        self.head = self.head.next
