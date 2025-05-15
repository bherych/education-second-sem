import unittest, avl_priority_queue as queue

class TestPriorityQueueAVL(unittest.TestCase):
    
    def test_insert(self):
        pq = queue.PriorityQueueAVL()
        pq.insert(3, "key A")
        pq.insert(1, "key B")
        pq.insert(2, "key C")
        pq.insert(1, "key D")
        pq.print_queue()

        self.assertEqual(pq.pop(), "key B")


if __name__ == '__main__':
    unittest.main()