import unittest
from arithmetic import *



class Test_Arithmetic(unittest.TestCase):
    def setUp(self):
        self.a = Arithmetic()

    def test_add(self):
        self.assertEqual(5, self.a.add(2, 5))
