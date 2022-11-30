import unittest


class TestSetMethods(unittest.TestCase):

    def test_difference(self):
        set1 = {1, 2, 3}
        set2 = {2, 3, 4}
        self.assertNotEqual(set1.difference(set2), set2.difference(set1))
        self.assertNotEqual(set2, set1)

    def setUp(self):
        print("hehe")

    def tearDown(self):
        print("haha")


if __name__ == "__main__":
    unittest.main()
