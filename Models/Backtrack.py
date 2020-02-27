from abc import ABC, abstractmethod


class Backtrack(ABC):
    """
    > Implements a general Stack based Backtracking algorithm
    """

    def __init__(self):
        self.stack = []

    def backtrack(self, node):
        while self.is_finished() is False:
            if node:
                self.accept(node)
                self.stack.append(node)
                node = self.next_node(node)
            elif len(self.stack) > 0:
                node = self.stack[-1]
                self.reject(node)
                node = self.next_alt(node)
                self.stack.pop()
            else:
                break
            while node:
                if self.is_valid(node):
                    break
                node = self.next_alt(node)
            self.act()

    @abstractmethod
    def accept(self, node):
        pass

    @abstractmethod
    def reject(self, node):
        pass

    @abstractmethod
    def is_finished(self):
        """
        > checks whether the backtrack has finished its task
        :return Boolean:
        """
        pass

    @abstractmethod
    def next_node(self, node):
        """
        > returns the next node(choice) based on the current node
        > if there is no possible next node, it returns None
        :param node:
        :return Node:
        """
        pass

    @abstractmethod
    def next_alt(self, node):
        pass

    @abstractmethod
    def is_valid(self, node):
        """
        > checks whether the node is a valid candidate for the solution
        > returns true if it is and false if it isn't
        :param node:
        :return Boolean:
        """
        pass

    @abstractmethod
    def act(self):
        """
        > allows for custom actions during each iteration
        :return:
        """
        pass
