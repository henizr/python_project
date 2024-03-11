import unittest
from main import Account


class TestAccount(unittest.TestCase):
    def test_id(self):

        result = Account(1).get_id()
        self.assertEqual(result, 1000)



if __name__ == "__main__":
    unittest.main()

