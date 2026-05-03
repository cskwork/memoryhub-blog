---
title: "Linked List Introduced"
date: 2024-05-29T08:07:11+09:00
slug: "161-Linked-List-Introduced"
original_url: "https://memoryhub.tistory.com/161"
tistory_id: 161
draft: false
---

*Linked lists are a fundamental data structure used in computer science to organize and store data in a linear sequence, where each element points to the next, making it easy to insert or delete elements.*

### The Big Picture

Imagine a linked list as a chain of paper clips. Each paper clip is a node, and the way they are linked together forms the chain. Unlike an array where elements are stored in contiguous memory locations, each node in a linked list is separate and contains a reference (or link) to the next node in the sequence.

### Core Concepts

1. **Node**: The basic unit of a linked list, which contains data and a reference (or pointer) to the next node.
2. **Head**: The first node in the linked list. If the list is empty, the head is null.
3. **Pointer/Reference**: The link part of a node that points to the next node in the list.
4. **Null Reference**: The end of the list is indicated by a node that has a null reference, meaning it points to nothing.

### Detailed Walkthrough

1. **Node Structure**:

   - Each node typically has two parts: the data it holds and a pointer to the next node.
   - In a singly linked list, each node points only to the next node.
   - In a doubly linked list, each node has two pointers: one to the next node and one to the previous node.
2. **Creating a Linked List**:

   - Start with the head node.
   - Each new node is added by adjusting the pointers.
   - For example, to add a node to the end, find the last node and update its pointer to the new node.
3. **Operations**:

   - **Insertion**: Adding a new node to the list, which involves changing pointers.
     - At the beginning: Adjust the head to the new node.
     - At the end: Find the last node and update its pointer.
     - In the middle: Adjust the pointers of the surrounding nodes.
   - **Deletion**: Removing a node, which involves bypassing the node to be removed and adjusting the pointers.
   - **Traversal**: Accessing each node sequentially from the head to the end to perform operations like searching or printing the list.

### Understanding Through an Example

Let's consider a simple singly linked list with the nodes containing integers.

1. **Creating the List**:

   ```
   class Node:
       def __init__(self, data):
           self.data = data
           self.next = None

   class LinkedList:
       def __init__(self):
           self.head = None

       def append(self, data):
           new_node = Node(data)
           if not self.head:
               self.head = new_node
               return
           last = self.head
           while last.next:
               last = last.next
           last.next = new_node

       def print_list(self):
           current = self.head
           while current:
               print(current.data)
               current = current.next

   # Example Usage
   ll = LinkedList()
   ll.append(1)
   ll.append(2)
   ll.append(3)
   ll.print_list()
   ```

   In this example:

   - We define a `Node` class with `data` and `next` attributes.
   - We define a `LinkedList` class with methods to append nodes and print the list.
   - We create a linked list and append three nodes with values 1, 2, and 3.
2. **Traversing the List**:

   - The `print_list` method iterates through the nodes starting from the head, printing each node's data.

### Conclusion and Summary

Linked lists are a flexible and dynamic data structure that allows for efficient insertion and deletion of elements. Each node contains data and a pointer to the next node, forming a chain-like structure. This structure is particularly useful in scenarios where the size of the list can change frequently, and memory allocation needs to be dynamic.

### Test Your Understanding

1. What is the difference between a singly linked list and a doubly linked list?
2. How would you modify the `LinkedList` class to include a method that deletes a node with a specific value?
3. Can you explain how you would find the middle element of a linked list?

### Reference

- [GeeksforGeeks: Linked List Data Structure](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [Wikipedia: Linked List](https://en.wikipedia.org/wiki/Linked_list)

Would you like to dive into any specific operation or concept related to linked lists in more detail?
