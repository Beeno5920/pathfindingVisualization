class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def add(self, data):
        self.queue.append(data)

    def dequeue(self):
        try:
            minIdx = 0
            for i in range(len(self.queue)):
                if self.queue[i].f < self.queue[minIdx].f:
                    minIdx = i
            item = self.queue[minIdx]
            del self.queue[minIdx]
            return item
        except IndexError:
            print()
            exit()