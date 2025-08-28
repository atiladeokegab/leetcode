class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # your current enqueue
    def enqueue(self, value):
        if len(self.stack1) == 0:
            self.stack1.append(value)
        elif len(self.stack1) > 0:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
            self.stack1.append(value)
            for _ in range(len(self.stack2)):
                self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if len(self.stack1) == 0:
            raise IndexError('Queue is empty')
        return self.stack1.pop()

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0


if __name__ == "__main__":
    q = MyQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Front of the queue:", q.peek())
    print("Is the queue empty?", q.is_empty())

    def test_enqueue_order():
        q = MyQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(9)

        try:
            assert q.peek() == 1, f"Expected front to be 1, got {q.peek()}"
            print("Test 1 passed: Peek is correct")
        except AssertionError as e:
            print("Test 1 failed:", e)

        try:
            q.dequeue()
            assert q.peek() == 2, f"Expected front to be 2 after one dequeue, got {q.peek()}"
            print("Test 2 passed: Order maintained after dequeue")
        except AssertionError as e:
            print("Test 2 failed:", e)

        try:
            q.dequeue()
            q.dequeue()
            assert q.peek() == 9, f"Expected front to be 9 after dequeuing 1,2,3 got {q.peek()}"
            print("Test 3 passed: Last element correct after multiple dequeues")
        except AssertionError as e:
            print("Test 3 failed:", e)

    test_enqueue_order()
