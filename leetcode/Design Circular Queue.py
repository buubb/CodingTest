class MyCircularQueue:
    def __init__(self, k:int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 #front
        self.p2 = 0 #rear

    def enQueue(self, val:int) -> bool:
        if self.q[self.p2] is None:
            self.q[self.p2] = val
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.p1] else self.q[self.p1]

    def Rear(self) -> int:
        return -1 if self.q[self.p2 -1] else self.q[self.p2 -1]

    def isEmpty(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        return self.p1 == self.p2 and self.q[self.p1] is not None