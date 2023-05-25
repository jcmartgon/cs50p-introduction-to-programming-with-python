# Jesus Carlos Martinez Gonzalez
# 24/05/2023
# Cookie Jar

# Simulate a cookie jar

class Jar:
    def __init__(self, capacity=12):
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        """Prints cookies in jar as emojis"""
        return '🍪' * self.size

    def deposit(self, n):
        """Adds n cookies to jar"""
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Too many cookies")

    def withdraw(self, n):
        """Removes cookies from jar"""
        if self.size - n < 0:
            raise ValueError("There aren't that many cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, n):
        n = int(n)

        if n <= 0:
            raise ValueError("Wrong amount of cookies")

        self._capacity = n

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n