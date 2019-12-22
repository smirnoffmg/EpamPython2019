"""
Написать тесты(pytest or unittest) к предыдущим 2 заданиям, запустив которые, я бы смог бы проверить их корректность
Обязательно проверить всю критическую функциональность
"""
<<<<<<< HEAD
import unittest
import time
from task2 import Message
from task1 import SiamObj


class SiamTest(unittest.TestCase):

    def test_siam(self):
        test1 = SiamObj('1', '2', a=1)
        test2 = SiamObj('1', '2', a=1)
        self.assertTrue(test1 is test2)

    def test_not_siam(self):
        test1 = SiamObj('1', '2', a=1)
        test2 = SiamObj('1', '2', a=2)
        self.assertTrue(test1 is not test2)

    def test_siam_connect(self):
        test1 = SiamObj('1', '2', a=1)
        test2 = SiamObj('1', '2', a=1)
        test3 = SiamObj('3', '4', a=5)
        test3.connect('1', '2', 1).a=2
        self.assertTrue(test1.a == test2.a == 2)


class PropertyTest(unittest.TestCase):

    def test_creating(self):
        m = Message()
        self.assertEqual(type(m.msg), str)

    def test_reset_timer(self):
        m = Message()
        message = m.msg
        self.assertEqual(m.msg, message)
        time.sleep(1)
        self.assertEqual(m.msg, message)
        m.msg = 'test_message'
        self.assertNotEqual(m.msg, message)
        message = m.msg
        time.sleep(1)
        self.assertEqual(m.msg, message)

    def test_cache_dump(self):
        m = Message()
        message = m.msg
        self.assertEqual(m.msg, message)
        time.sleep(1)
        self.assertEqual(m.msg, message)


if __name__ == '__main__':
    unittest.main()
=======
>>>>>>> upsteam/master
