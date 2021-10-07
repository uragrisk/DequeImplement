import unittest

from deque import Deque


class TestDeque(unittest.TestCase):

    def test_push_left(self):
        deque = Deque()
        deque.push_left(1)
        deque.push_left(9)
        deque.push_left(11)
        deque.push_left(22)
        deque = deque.deque_to_list()
        result_deque = [22, 11, 9, 1]
        self.assertEqual(deque, result_deque)

    def test_push_right(self):
        deque = Deque()
        deque.push_right(1)
        deque.push_right(9)
        deque.push_right(11)
        deque.push_right(22)
        deque = deque.deque_to_list()
        result_deque = [1, 9, 11, 22]
        self.assertEqual(deque, result_deque)

    def test_pop_left(self):
        deque = Deque()
        deque.push_left(1)
        deque.push_left(9)
        deque.push_left(11)
        deque.push_left(22)
        deque.pop_left()
        deque = deque.deque_to_list()
        result_deque = [11, 9, 1]
        self.assertEqual(deque, result_deque)

    def test_pop_right(self):
        deque = Deque()
        deque.push_left(1)
        deque.push_left(9)
        deque.push_left(11)
        deque.push_left(22)
        deque.pop_right()
        deque = deque.deque_to_list()
        result_deque = [22, 11, 9]
        self.assertEqual(deque, result_deque)

    def test_find_by_value(self):
        deque = Deque()
        deque.push_left(1)
        deque.push_left(9)
        deque.push_left(11)
        deque.push_left(22)
        element1 = deque.find_by_value(9)
        element2 = deque.find_by_value(155)
        self.assertEqual(element1, True)
        self.assertEqual(element2, False)
