"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):
    def test_singleton_instance(self):
        counter1 = Counter()
        counter2 = Counter()
        self.assertIs(counter1, counter2, "Counter is not a singleton")

    def test_shared_count(self):
        counter1 = Counter()
        counter2 = Counter()
        counter1.increment()
        self.assertEqual(counter1.count, counter2.count, "Count is not shared")

    def test_count_not_reset(self):
        counter1 = Counter()
        counter1.increment()
        count_before = counter1.count
        counter2 = Counter()
        self.assertEqual(count_before, counter2.count, "Count was reset")
