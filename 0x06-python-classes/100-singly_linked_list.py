#!/usr/bin/python3
"""Singly Linked List
Module representing a singly linked list

Contains two classes:
Node: representing a Node
SinglyLinkedList: representing the whole list
"""


class Node:
    """A node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializer
        Args:
            data (int): the data to insert into the node
            next_node (Node): points to the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter method for the data of the node

        Returns:
            the data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """setter method for the data of the node

        Args:
            value (int): the data to set
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter method for the next_node

        Returns:
            the next node in the list
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """setter method for the next_node

        Args:
            value: the next_node
        """
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

    def __lt__(self, other):
        """see which of two nodes is lesser

        Args:
            other: the other node to compare

        Returns:
            result of comparison
        """
        return (self.__data < other.__data)


class SinglyLinkedList:
    """class to represent a singly linked list"""

    def __init__(self):
        """initializer"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into the singly linked list
        The list should be in ascending order
        Args:
            value: value of data for new node
        """
        new = Node(value)
        if self.__head is None:
            new.__next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.__next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while current.__next_node is not None and\
                    current.__next_node.data < value:
                current = current.__next_node
            new.__next_node = current.__next_node
            current.__next_node = new

    def __str__(self):
        """print the sorted node

        Returns:
            the string to print
        """
        literal = []
        current = self.__head
        while current is not None:
            literal.append(str(current.data))
            current = current.__next_node
        return ('\n'.join(literal))
