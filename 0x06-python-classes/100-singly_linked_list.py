#!/usr/bin/python3
#-*- coding: utf-8 -*-
"""Module for handling a singly linked list"""

class Node:
    """This class is a node."""
    def __init__(self, data, next_node=None):
        """Initialize a Node class

        Args:
            data (integer): value to be stored
            next_node (Node): pointer to the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """accessor for data attribute

        Returns: value of data attribute
        """
        return self.__data

    @data.setter
    def data(self, value):
        """accessor for data attribute

        Args:
            value (integer): value to be stored in the node

        Raises:
            TypeError: if value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """accessor for next_node attribute

        Returns: value of next_node attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """accessor for next_node attribute

        Args:
            value (Node): pointer to next node

        Raises:
            TypeError: if next_node is not None or a Node object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """This class is a Singly Linked List."""
    def __init__(self):
        """Initialize the SinglyLinkedList object"""
        self.__head = None

    def __str__(self):
        """Print to stdout the content of the list"""
        s = ""
        current = self.__head
        while current:
            s += "{:d}\n".format(current.data)
            current = current.next_node
        return s[:-1]

    def sorted_insert(self, value):
        """Insert a new node into the correct sorted position
        in the list (increasing order)

        Args:
            value (integer): value of the new node
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        if self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        previous = None
        while current:
            if current.data > new.data:
                break
            previous = current
            current = current.next_node

        if previous:
            previous.next_node = new
        new.next_node = current
