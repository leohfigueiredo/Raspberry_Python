import unittest

class TestClass12(unittest.TestCase):

	def test_case01(self):
		"""This is a test method..."""
		print("\nIn test_case01()...")
		print(self.id())
		self.fail()
