"""
This my stuff.. You know :)
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
def make_2d_grid(a_list, width, height, side=None):
    """
    create a 2D grid (rows and columns)
    """
    result = ""
    for row in range(height):
        if side is not None:
            result += str(side[row])+": "
        for colum in range(width):
            result += "| "+str(a_list[row][colum])+"| "
        result += "\n"
    return result


def traverse_grid(a_list, start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction
    
    Both start_cell is a tuple(row, col) denoting the
    starting cell
    
    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        print "Processing cell", (row, col), 
        print "with value", a_list[row][col]


def average(numbers):
    """
    compute the average of a sequence of numbers

    :parm numbers: iterable
    :return: float
    """
    result = sum(numbers)/float(len(numbers))
    return result

# ================= Test class =============
"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""

class TestSuite:
    """
    Create a suite of tests similar to unittest
    """
    def __init__(self):
        """
        Creates a test suite object
        """
        self.total_tests = 0
        self.failures = 0
    
    
    def run_test(self, computed, expected, message = ""):
        """
        Compare computed and expected
        If not equal, print message, computed, expected
        """
        self.total_tests += 1
        if computed != expected:
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print msg
            self.failures += 1
    
    def report_results(self):
        """
        Report back summary of successes and failures
        from run_test()
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print msg
