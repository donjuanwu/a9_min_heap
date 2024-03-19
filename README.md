# a9_min_heap
SDDE assignment 9 - create a min heap


Recall from class that a min heap is a complete binary tree in which the value of each node is greater than or equal to the value of its parent. We'll be building upon the functions written in lab that allow you to write an array-backed min heap.

In order to test these two problems, you will have to port your traversal methods written in the week 6 assignment so they work with an array. Allow your min heap class to accept an array in its constructor, and ensure that all three traversal methods pass testing before proceeding.

Next, implement an interface for your min heap that allows values to be inserted and deleted.

1. Start by writing a function which can Insert a value to your min heap, in order to do this, you will need a HeapifyUp function that will maintain the heap property of the tree.
2. Next, write a ExtractMin function that will return the smallest element of the min heap and then HeapifyDown by swapping with the smaller of the node's two children until the order of the heap is satisfied.
