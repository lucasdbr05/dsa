class Queue:
    def __init__(self):
        self._size = 0
        self.first = None
        self.last = None
        
    def push(self, item): 
        node = Node(item)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if self.first is None:
            self.first = node
        self._size +=1
        
    
        
    def pop(self): 
        if self.first is not None:
            item = self.first.data
            self.first = self.first.next
            self._size -= 1
            return item
        raise IndexError('the queue is empty')
        
    
    def peek(self): 
        if self.last is not None:
            return self.first.data
        raise IndexError('the queue is empty')
        
    def  __len__(self): 
        return self._size
    
    def to_list(self):
        pointer = self.first
        lista = []
        while pointer:
            lista.append(pointer.data)
            pointer = pointer.next
        return lista
    
    def __repr__(self):
        if self._size:
            r = ""
            pointer = self.first
            while pointer:
                r = r + str(pointer.data) + "  "
                pointer = pointer.next
            return r
        return "Empty Queue"
    
    def __str__(self):
        return self.__repr__()
        



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
        
    

class BinarySearchTree:
    def __init__(self):
        self.root = None 
        
    def inorder_traversal(self, node = None):
        if self.root is None: return
        if(node is None):
            node = self.root
        
        if node.left:
            self.inorder_traversal(node.left)
        print(node.data)
        if node.right:
            self.inorder_traversal(node.right)
            
            
    def preorder_traversal(self, node = None):
        if self.root is None: return
        if(node is None):
            node = self.root
        
        print(node.data)
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)
            
            
    def posorder_traversal(self, node = None):
        if self.root is None: return
        if(node is None):
            node = self.root
        
        if node.left:
            self.posorder_traversal(node.left)
        if node.right:
            self.posorder_traversal(node.right)
        print(node.data)
            
    
    def height(self, node = None):
        if (node is None):
            node = self.root
        if (node is None): return 0
        
        if not node.left is None:left_height = self.height(node.left)
        if not node.right is None:right_height = self.height(node.right)
        
        return 1+ max(left_height, right_height)
        
    
    
    def bfs(self, node= None):
        if self.root is None: return
        if node is None:
            node = self.root 
            
        q = Queue()
        q.push(node)
        while len(q):
            curr = q.pop()
            print(curr.data)
            if curr.left:q.push(curr.left)
            if curr.right: q.push(curr.right)
    
    
    
    def insert(self, data):
        
        parent = None
        curr = self.root 
        while curr:
            parent = curr
            if data <= curr.data: curr = curr.left 
            else : curr = curr.right 
        
        if parent is None:
            self.root = Node(data)
        elif data <= parent.data:
            parent.left = Node(data)
        else:
            parent.right = Node(data)
            
            
    def search(self, value):
        if self.root: return self._search(value, self.root)
        return None 
    
    def _search(self, value, node):
        if node is None: return None 
        
        if node.data==value:         return BinarySearchTree(node)
        elif node.data < value:
            return self._search(value, node.left)
        elif node.data > value:
            return self._search(value, node.right)
        
        
    def minimun(self, node= None):
        if node is None:
            node = self.root
        while node.left:
            node = node.left
        return node.data
    
    def maximun(self, node= None):
        if node is None:
            node = self.root
        while node.right:
            node = node.right
        return node.data
            
    def remove(self, value, curr = None):
        if curr is None:
            curr = self.root
    
        if curr.data == value:
            if curr.left is None and curr.right is None:
                return None 
            elif curr.left is None:
                return curr.right
            elif curr.right is None:
                return curr.left 
            else:
                aux = self.maximun(curr.left)
                curr.data = aux 
                curr.left = self.remove(aux, curr.left)
                return curr
                
        elif curr.data > value:
            return self.remove(value, curr.left) 
        elif curr.data < value:
            return self.remove(value, curr.right) 
        
        
        
        
            

    

        
    
    
    
    