from collections import deque

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = list()
        for x in range(k):
            self.queue.append(0)
        self.head = -1
        self.tail = -1
        self.maxSize = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.maxSize
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.maxSize
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return ((self.tail + 1) % self.maxSize) == self.head

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque(maxlen=size)

    def next(self, val: int) -> float:
        self.q.append(val)
        return float(sum(self.q)/len(self.q))

# Need to come back to this one...
class WallsAndGates:
    # def wallsAndGates(self, rooms: List[List[int]]) -> None:
    def wallsAndGates(self, rooms):
        q = [(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r]
        for i, j in q:
            for I, J in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= I < len(rooms) and 0 <= J < len(rooms[0]) and rooms[I][J] > 2**30:
                    rooms[I][J] = rooms[i][j] + 1
                    q += (I, J)

# Need to come back to this one...
# https://www.python-course.eu/python3_lambda.php
class NumberOfIslands:
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

# Need to come back to this one...
class OpenTheLock:
    def openTheLock(self, lock):
        return None

# Need to come back to this one...
class PerfectSquare:
    def numSquares(self, n): # n is int, return type is int
        if n < 2:
            return n

        list = []
        i = 1
        while i * i <= n:
            list.append(i * i)
            i += 1
        count = 0
        dict = {n}

        while dict:
            count += 1
            temp = set()
            for x in dict:
                for y in list:
                    if x == y:
                        return count
                    if x < y:
                        break
                    temp.add(x - y)
            dict = temp

        return count

def main():
    #########################
    # Circular Q Test Cases #
    #########################

    # q = MyCircularQueue(3)
    # print("Enqueue 1: " + str(q.enQueue(1)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 2: " + str(q.enQueue(2)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 3: " + str(q.enQueue(3)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 4: " + str(q.enQueue(4)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Rear: " + str(q.Rear()))
    # print("Is it full? " + str(q.isFull()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 4: " + str(q.enQueue(4)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Rear: " + str(q.Rear()))

    # q = MyCircularQueue(5)
    # print("Is it empty?: " + str(q.isEmpty()))
    # print("Enqueue 1: " + str(q.enQueue(1)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 2: " + str(q.enQueue(2)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 3: " + str(q.enQueue(3)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 4: " + str(q.enQueue(4)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 5: " + str(q.enQueue(5)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Front: " + str(q.Front()))
    # print("Rear: " + str(q.Rear()))
    # print("Is it full? " + str(q.isFull()))
    # print("Can I add one more...trying to enqueue 6: " + str(q.enQueue(6)))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 6: " + str(q.enQueue(6)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 7: " + str(q.enQueue(7)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Enqueue 8: " + str(q.enQueue(8)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("©Enqueue 9: " + str(q.enQueue(9)) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()) + " Front: " + str(q.Front()) + " Rear: " + str(q.Rear()))
    # print("Is it empty?: " + str(q.isEmpty()))

    # q = MyCircularQueue(6)
    #
    # print("Enqueue 6: " + str(q.enQueue(6)))
    # print("Rear: " + str(q.Rear()))
    # print("Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()))
    # print("Enqueue 5: " + str(q.enQueue(5)))
    # print("Rear: " + str(q.Rear()))
    # print("Dequeueing..." + str(q.deQueue()))
    # print("Front: " + str(q.Front()))
    # print("Dequeueing..." + str(q.deQueue()))
    # print("Dequeueing..." + str(q.deQueue()))
    # print("Dequeueing..." + str(q.deQueue()))

    ########################
    # Moving Avg Test Case #
    ########################
    # obj = MovingAverage(10)
    # result = obj.next(5)
    # print(result)
    # result = obj.next(10)
    # print(result)
    # result = obj.next(50)
    # print(result)
    # result = obj.next(100)
    # print(result)

    ###############################
    # Number of Islands Test Case #
    ###############################
    # obj = NumberOfIslands()
    # grid1 = [["1","1","1","1","0"],
    #          ["1","1","0","1","0"],
    #          ["1","1","0","0","0"],
    #          ["0","0","0","0","0"]]
    # result = obj.numIslands(grid1) # 1
    # print(result)
    # print("Should be 1")
    #
    # grid2 = [["1","1","0","0","0"],
    #          ["1","1","0","0","0"],
    #          ["0","0","1","0","0"],
    #          ["0","0","0","1","1"]]
    # result = obj.numIslands(grid2) # 3
    # print(result)
    # print("Should be 3")

    #############################
    # Perfect Squares Test Case #
    #############################
    obj = PerfectSquare()
    answer = obj.numSquares(12)
    print(answer)
    print("Should be 3")

    answer = obj.numSquares(13)
    print(answer)
    print("Should be 2")

if __name__ == "__main__":
    main()


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
