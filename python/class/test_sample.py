import sample, unittest

class TestSample(unittest.TestCase):
	def test_add(self):
		result = sample.add(1, 2)
		self.assertEqual(result, 13)
#		self.assertEqual(result, 3)

if __name__ == "__main__":
	unittest.main()
	