import unittest
from src.calc import add, subtract

class TestCalculator(unittest.TestCase):

	def test_add(self):
		self.assertEqual(add(1, 2), 3)
		elf.assertEqual(add(-1, 1), 0)
		self.assertEqual(add(-1, -1), -2)

	def test_subtract(self):
		self.assertEqual(subtract(1, 2), -1)
		self.assertEqual(subtract(-1, 1), -2)
		self.assertEqual(subtract(-1, -1), 0)


if __name__ == '__main__’:
	unittest.main()
