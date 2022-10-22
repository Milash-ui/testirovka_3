import unittest
from main import budilnik

class test(unittest.TestCase):
    def setUp(self):
        self.budilnik = budilnik()
    def hour(self):
        self.assertEqual(self.budilnik.validate_time[0:2](16), 16)
        self.assertEqual(self.budilnik.validate_time[3:5](31), 31)
        self.assertEqual(self.budilnik.validate_time[6:8](50), 50)

if __name__ == '__main__':
    unittest.main()
