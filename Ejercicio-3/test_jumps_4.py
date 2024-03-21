import unittest
from ejercicio3 import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_min_jumps(self):
        print(min_jumps(4))

if __name__ == '__main__':
    unittest.main()
    