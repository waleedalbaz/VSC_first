"""
This my stuff.. You know :)
I want to disturb this to git

another try
"""
class _Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class LinkedList():
    """
    create a new list
    """
    def __init__(self):
        self._head_ = _Node()
        self._len_ = 0
    
    def append(self, data):
        """
        add a new element to the list
        """
        new_node = _Node(data)
        current = self._head_
        while current.next is not None:
            current = current.next
        current.next = new_node
        self._len_ +=1
    
    def length(self):
        """
        return length of the list
        """
        return self._len_

    def display(self):
        """
        print the elements of the list
        """
        current = self._head_
        elem = []
        while current.next is not None:
            current = current.next
            elem.append(current.data)
        print elem
    
    def get(self, index):
        """
        return value for a specific index
        """
        if index >= self.length():
            print "ERROR: 'Get' Index out of range!"
            return None
        cur_idx = 0
        cur_node = self._head_
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1
    
    def erase(self, index):
        """
        erase an element from the list
        """
        if index >= self.length():
            print "ERROR: 'Erase' Index out of range!"
            return None
        cur_idx = 0
        cur_node = self._head_
        while True: # continue till match the index input
            last_node = cur_node # hold value before move
            cur_node = cur_node.next # move step
            if cur_idx == index:
                last_node.next = cur_node.next # slide the next value back
                self._len_ -= 1
                return # out after erasing
            cur_idx += 1 # move th index one step


# ================= Functions =============
def make_2d_grid(a_list, width, height):
    """
    create a 2D grid (rows and columns)
    """
    result = ""
    for row in range(height):
        result += str(LETTERS[row])+": "
        for colum in range(width):
            result += "| "+str(a_list[row][colum])+"| "
        result += "\n"
    print result