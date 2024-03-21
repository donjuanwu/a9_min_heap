# a9_min_heap
SDDE assignment 9 - create a min heap


Recall from class that a min heap is a complete binary tree in which the value of each node is greater than or equal to the value of its parent. We'll be building upon the functions written in lab that allow you to write an array-backed min heap.

In order to test these two problems, you will have to port your traversal methods written in the week 6 assignment so they work with an array. Allow your min heap class to accept an array in its constructor, and ensure that all three traversal methods pass testing before proceeding.

Next, implement an interface for your min heap that allows values to be inserted and deleted.

1. Start by writing a function which can Insert a value to your min heap, in order to do this, you will need a HeapifyUp function that will maintain the heap property of the tree.
2. Next, write a ExtractMin function that will return the smallest element of the min heap and then HeapifyDown by swapping with the smaller of the node's two children until the order of the heap is satisfied.


def insert_node(self, value):
    # append value to end of list
    # get last index
    # call heapify to set new value in proper place



def heapify(self, last_index):
    # loop while there is a parent and parent is greater than current node
    # set current node to parent index




delete root_node(self):
    # replace root node with last node
    # call has_less_child() to determine if there is children and children is less than current node
    # call 


def has_lesser_child(self, node)
    # return true, if there left child and child is less than parent
    # return true, if there is right child and child is less than parent
    # else, return false

def get_smaller_child(self, node)
    # if there is no right child, return left child index
    # if right child is less than left child, return right child index
    # else, return left child index

def get_left_child(self, node):
    left_child_index = (node * 2) + 1
    return left_child_index

def get_right_child(self, node):
    right_child_index = (node * 2) + 2
    return right_child_index
        
