import unittest
from heapq import heappush, heappop, heapreplace, heappushpop, heapify

class TestHeapq(unittest.TestCase):

    def setUp(self):
        
        self.heap = []
        self.sample_list = [5, 3, 8, 1, 6, 9, 2]

    def test_heappush(self):
        
        heappush(self.heap, 5)
        heappush(self.heap, 3)
        heappush(self.heap, 8)
        heappush(self.heap, 1)
        self.assertEqual(self.heap[0], 1)

    def test_heappop(self):
        
        for item in self.sample_list:
            heappush(self.heap, item)
        popped_item = heappop(self.heap)
        self.assertEqual(popped_item, 1)  

    def test_heapreplace(self):
        
        for item in self.sample_list:
            heappush(self.heap, item)
        replaced_item = heapreplace(self.heap, 0)
        self.assertEqual(replaced_item, 1)  
        self.assertEqual(self.heap[0], 0)   

    def test_heappushpop(self):
        # Test heappushpop
        for item in self.sample_list:
            heappush(self.heap, item)
        result = heappushpop(self.heap, 0)
        self.assertEqual(result, 0)  

    def test_heapify(self):
        
        heapify(self.sample_list)
        self.assertEqual(self.sample_list[0], 1)  

if __name__ == '__main__':
    unittest.main()
