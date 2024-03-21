"""
Student: Don Dang
Date: 3/18/24
Class: SDDE 310 A
Instructor: Sanjeev Qazi
TA:  David Clayton
Week: 9
Assignment: Lesson 9
Subject: Priority Queue/Heap

References:
    1. lab max-heap
    A Common-Sense Guide to Data Structures and Algorithms, Second Edition, 2nd Edition
        -   https://learning.oreilly.com/library/view/a-common-sense-guide/9781680508048/f_0162.xhtml#d24e25476

    2. Binary Heap - GeeksforGeeks
        - https://www.geeksforgeeks.org/binary-heap/
    3. Difference between / vs. //
        -   https://www.geeksforgeeks.org/difference-between-vs-operator-in-python/

Notes:
    1. heap itself can be an abstract data type that really uses an array under the hood



Date        Developer       Activities
3/18/24     Don D.          Create max-heap


"""


class MinHeap:
    def __init__(self):
        """
        create empty array to hold min heap elements
        """
        self.heap = []  # create empty array to hold binary heap elements

    def insert_node(self, value):
        # append value to end of list
        # get last index
        # call heapify to set new value in proper place
        self.heap.append(value)
        last_index = len(self.heap) - 1
        self.heapify(last_index)  # percolate up to place added value in the proper place

    def heapify(self, index):
        # loop while there is a parent and parent is greater than current node
        # set current node to parent index
        while index > 0:  # loop while last_index > 0
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:  # if child value is less than parent value
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[
                    index]  # swap child with parent value
                index = parent_index  # assign index to be parent index
            else:  # child is greater than parent
                break

    def delete_root_node(self):
        # replace root node with last node
        # call has_less_child() to determine if there is children and children is less than current node
        # call
        self.heap[0] = self.heap.pop()  # pop last node and assign to root node
        parent_index = 0  # assign root index
        while self.has_lesser_child(parent_index):  # while parent has child(s) and their value is less than parent
            lesser_child_index = self.get_lesser_child_index(parent_index)  # get lesser child index
            self.heap[parent_index], self.heap[lesser_child_index] = self.heap[lesser_child_index], self.heap[
                parent_index]  # swap parent index with lesser child index
            parent_index = lesser_child_index  # update parent new index

    def has_lesser_child(self, parent_index):
        """
        determine if left or right child exist and one of their value is less than parent value
            return True
        else
            return false
        """
        heap_length = len(self.heap)
        # the left and right child index must still be within the lenght of the array
        if self.get_left_child_index(parent_index) < heap_length and self.heap[self.get_left_child_index(parent_index)] < self.heap[
            parent_index]:
            return True  # return true, if left child exist and its value less than parent
        elif self.get_right_child_index(parent_index) < heap_length and self.heap[self.get_right_child_index(parent_index)] < \
                self.heap[parent_index]:
            return True  # return true, if right child exist and its value less than parent
        else:  # neither children exist and either children value is greater than parent
            return False  # else, return false

    def get_lesser_child_index(self, node):
        """
        return the child index with the lesser value
        :param node: parent index
        :return: child index with lesser value
        """
        if self.get_right_child_index(node) > len(self.heap) - 1:  # right child index is greater than the last element index
            return self.get_left_child_index(node)  # if there is no right child, return left child index
        elif self.heap[self.get_right_child_index(node)] < self.heap[self.get_left_child_index(node)]:
            return self.get_right_child_index(node)
        else:  # left child value is less than right child value
            return self.get_left_child_index(node)

    def get_left_child_index(self, node):
        left_child_index = (node * 2) + 1
        return left_child_index

    def get_right_child_index(self, node):
        right_child_index = (node * 2) + 2
        return right_child_index

    def print_heap(self):
        for element in self.heap:
            print(element, end=' ')

    @staticmethod
    def create_heap():
        """
        build min-heap
        :return:
        """
        h = MinHeap()
        h.insert_node(50)
        h.insert_node(20)
        h.insert_node(35)
        h.insert_node(15)
        h.insert_node(0)
        return h


heap = MinHeap.create_heap()
heap.print_heap()
print()
print("Add more elements to min heap: 65, 35, 5, 70")
heap.insert_node(65)
heap.insert_node(35)
heap.insert_node(5)
heap.insert_node(70)
heap.print_heap()
print()
print("Delete root node")
heap.delete_root_node()
heap.print_heap()
print()
print("Add new elements: -1")
heap.insert_node(-1)
heap.print_heap()
print()
print("Add new elements: -5")
heap.insert_node(-5)
heap.print_heap()
