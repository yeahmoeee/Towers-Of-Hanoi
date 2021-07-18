class Node:
    next_node = None
    def __init__(self,data):
        self.data = data
    
    def __repr__(self):
        return str(self.data)


class Stack:
    def __init__(self, max_size = None):
        self.top = None
        self.max_size = max_size
        self.size = 0

    def isempty(self):
        return self.size == 0

    def hasspace(self):
        
        if self.max_size == None:
            return True

        elif self.max_size > self.size:
            return True
        else:
            return False
    
    def push(self,data):
        new_node = Node(data)
        if self.isempty():
            self.top = new_node
            self.size += 1
        else:
            if self.hasspace():
                new_node.next_node = self.top
                self.top = new_node
                self.size += 1
            else:
                return

    def pop(self):
        top = self.top
        if not self.isempty():
            self.top = top.next_node
            self.size -= 1
            return top.data 
        else:
            return
    
    def peek(self):
        top = self.top
        if not self.isempty():
            return top.data
        else:
            return
        

    def __repr__(self):
        nodes = []
        current = self.top 
        while current:
            if current is self.top:
                nodes.append("[%s]" %current.data)
            elif current.next_node is None:
                nodes.append("[%s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)
            current = current.next_node 
        return "\n".join(nodes) 
            




