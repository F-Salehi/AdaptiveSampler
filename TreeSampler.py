
import numpy as np

class Node:
    def __init__(self, val,par,n_id):
        self.l = None
        self.r = None
        self.parent = par
        self.v = val
        self.node_id = n_id

class Tree:
    def __init__(self,N):
        self.num_leaves = N
        self.root = Node(N,None,0)
        if N > 1:
            n_id = 0
            self.add(N,self.root,n_id)
        else:
            return
    def add(self, val, par, n_id):
        '''
        Adding a node to the tree with value v, parent node par, and node id n_id
        '''
        if val >1:
            sep = int(val/2.0)
            par.l = Node(sep, par, n_id)
            n_id = self.add(sep, par.l, n_id)
            par.r = Node(val-sep, par, n_id)
            n_id = self.add(val-sep, par.r, n_id)
            return n_id
        else:
            par.node_id = n_id
            n_id += 1
            return n_id

    def getRoot(self):
        '''
        Getting the root of tree.
        '''
        return self.root

    def find_id(self,n_id):
        '''
        Finding the node of the tree with a specific id.
        n_id: int
        '''
        if(self.root != None):
            return self._find_id(n_id, self.root)
        else:
            return None
    def _find_id(self,n_id,node):
        if node.l == None:
            return node
        else:
            value = node.r.node_id
            if n_id < value:
                return self._find_id(n_id,node.l)
            else:
                return self._find_id(n_id,node.r)

    def find(self, val):
        '''
        Finding the node with the specific value val
        val: float
        '''
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if node.l == None:
            return node
        else:
            value = node.l.v
            if val <= value:
                return self._find(val,node.l)
            else:
                return self._find(val-value,node.r)

    def sample(self):
        '''
        Sampling according to the unnormalized distribution of the leaves
        '''
        num = np.random.uniform() * self.getRoot().v
        node = self.find(num)
        return node.node_id, node

    def initialize(self, value_list):
        '''
        Initializing the values of the leaves of the tree with value_list
        value_list: list with length self.num_leaves
        '''
        if len(value_list) > self.num_leaves:
            raise ValueError("The length of input is larger than the number of leaves")
        for i, v in enumerate(value_list):
            node = self.find_id(i)
            self.update(node, v)

    def update(self, node, value_new):
        '''
        Updating the value of a node
        '''
        value_old = node.v
        diff_value = value_new - value_old
        node.v = value_new
        while (node.parent != None):
            node = node.parent
            node.v += diff_value
        return

    def deleteTree(self):
        # garbage collector will do this for us
        self.root = None

    def printTree(self):
        '''
        In-order traversal of the tree
        '''
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.r)
            print(str(node.v) + ' '+str(node.node_id))
            self._printTree(node.r)