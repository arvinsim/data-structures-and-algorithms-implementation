class BinaryHeap:
    """
    BinaryHeap() creates a new, empty, binary heap.
    This is the minimum heap version
    """
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def get_left_child_index(self, parent_index):
        return (parent_index * 2) + 1

    def get_right_child_index(self, parent_index):
        return (parent_index * 2) + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.currentSize

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.currentSize

    def has_parent(self, index):
        return self.get_parent_index(index) >= size

    def left_child(self, index):
        return self.heapList[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.heapList[self.get_right_child_index(index)]

    def parent(self):
        return self.heapList[self.get_parent_index(index)]

    def swap(self, i, j):
        """
        Swap items
        """
        self.heapList[i], self.heapList[j] = self.heapList[j], self.heapList[i]

    def heapify_up(self, i):
        """
        Swap values up until the parent is lesser than the inserted value
        """
        while i // 2 > 0:
            # Swap if parent is greater than child
            if self.heapList[i] < self.heapList[self.get_parent_index(i)]:
                self.swap(i, self.get_parent_index(i))
            i = i // 2

    def heapify_down(self):
        index = 0
        # Insert the last element into the first index
        while self.has_left_child(index):
            # set the smaller child
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)
            
            # If smaller child index item is less than current index item, stop
            if self.heapList[index] < self.heapList[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)

            index = smaller_child_index

    def insert(self, k):
        """
        insert(k) adds a new item to the heap.
        """
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.heapify_up(self.currentSize-1)

    def peek(self, k):
        """
        Returns the item with the minimum key value, leaving item in the heap.
        """
        return self.heapList[0]

    def poll(self):
        """
        returns the item with the minimum key value, removing the item from the heap.
        """
        item = self.heapList[0]
        self.heapList[0] = self.heapList.pop()
        self.currentSize -= 1
        self.heapify_down()
        return item

if __name__ == '__main__':
    bh = BinaryHeap()
    bh.insert(10)
    bh.insert(15)
    bh.insert(20)
    bh.insert(17)
    bh.insert(25)

    print(bh.heapList)

    print('Do poll. Item: ', bh.poll())
    print(bh.heapList)
