class MaxHeap():
    def __init__(self, initValues = []) -> None:
        self.heap = [0]
        for v in initValues:
            self.push(v)

    def push(self, value):
        # append new value to end of list
        self.heap.append(value)
        # call floatUp with index of added value
        self.__floatUp(self.__getLastIndex())

    def peek(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return False
    
    def pop(self):
        # if list is empty there is no item to return
        if len(self.heap) < 2:
            return False
        # if list has only one item no need to rearange. hust pop and return the item
        if len(self.heap) == 2:
            return self.heap.pop()

        self.__swap(1, self.__getLastIndex())
        head = self.heap.pop()
        self.__floatDown(1)
        return head

    def __floatDown(self, index):
        iLeft = self.__getIndexLeftChild(index)
        iRight = self.__getIndexRightChild(index)
        largest = index

        if self.__getLastIndex() > iLeft and self.heap[largest] < self.heap[iLeft]:
            largest = iLeft
        if self.__getLastIndex() > iRight and self.heap[largest] < self.heap[iRight]:
            largest = iRight
        if largest != index:
            self.__swap(index, largest)
            self.__floatDown(largest)
    

    def __getIndexLeftChild(self, index):
        return index * 2

    def __getIndexRightChild(self, index):
        return self.__getIndexLeftChild(index) + 1

    def __floatUp(self, index):
        # if len of smaller or equal than 1 there is only 1 item.
        if len(self.heap) <= 1:
            return True
        if self.__parentIndex(index) == 0:
            return True
        
        if self.__getParent(index) < self.heap[index]:
            self.__swap(index, self.__parentIndex(index))
            self.__floatUp(self.__parentIndex(index))
            return True

    def __swap(self, n, m):
        self.heap[n], self.heap[m] = self.heap[m], self.heap[n]

    def __getParent(self, index):
        return self.heap[self.__parentIndex(index)]

    def __parentIndex(self, index):
        return index // 2

    def __getLastIndex(self):
        return len(self.heap) - 1

    def __str__(self) -> str:
        '''returns entry of table as string'''
        res = str(self.heap)
        res += "\n"
        for index, v in enumerate(self.heap[1:]):
            iLeft = self.__getIndexLeftChild(index + 1)
            iRigth = self.__getIndexRightChild(index + 1)
            left = 0
            right = 0
            if self.__getLastIndex() > iLeft:
                left = self.heap[iLeft]
            if self.__getLastIndex() > iRigth:
                right = self.heap[iRigth]
            res += f"{'ERROR! ' if left > v or right > v else ''}{v} -> ({left}, {right})\n"
        return res
