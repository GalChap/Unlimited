import unittest
from Unlimited import Unlimited




class TestUnlimited(unittest.TestCase):

    # Unit test for equal operator
    def test_equalOperator(self):
            test1 = Unlimited(1234)
            test2 = Unlimited(1234)
            self.assertEquals( test1 == test2, True)
            test1.unlimitedNumber = 123
            self.assertEquals(test1 == test2, False)

    # Unit test for not equal operator
    def test_notEqualOperator(self):
        test1 = Unlimited(1234)
        test2 = Unlimited(1234)
        self.assertEquals(test1 != test2, False)
        test1.unlimitedNumber = 123
        self.assertEquals(test1 != test2, True)

    # Unit test for less equal operator
    def test_lessEqualOperator(self):
        test1 = Unlimited(1234)
        test2 = Unlimited(1234)
        self.assertEquals(test1 <= test2, True)
        test1.unlimitedNumber = 12345
        self.assertEquals(test1 <= test2, False)
        test1.unlimitedNumber = 123
        self.assertEquals(test1 <= test2, True)

    # Unit test for greater equal operator
    def test_greaterEqualOperator(self):
        test1 = Unlimited(1234)
        test2 = Unlimited(1234)
        self.assertEquals(test1 >= test2, True)
        test1.unlimitedNumber = 12345
        self.assertEquals(test1 >= test2, True)
        test1.unlimitedNumber = 123
        self.assertEquals(test1 >= test2, False)

    # Unit test for add operator
    def test_addOperator(self):
        test1 = Unlimited(12)
        test2 = Unlimited(12)
        addResult = test1 + test2
        self.assertEquals(addResult.unlimitedNumber, 24)
        test1.unlimitedNumber = -5
        addResult = test1 + test2
        self.assertEquals(addResult.unlimitedNumber, 7)
        test2.unlimitedNumber = -3
        addResult = test1 + test2
        self.assertEquals(addResult.unlimitedNumber, -8)
        test1.unlimitedNumber = 5
        addResult = test1 + test2
        self.assertEquals(addResult.unlimitedNumber, 2)

    # Unit test for add with assignment to left side operator
    def test_iaddOperator(self):
        test1 = Unlimited(12)
        test2 = Unlimited(12)
        test1 += test2
        self.assertEquals(test1.unlimitedNumber, 24)
        test1.unlimitedNumber = -5
        test1 += test2
        self.assertEquals(test1.unlimitedNumber, 7)
        test1.unlimitedNumber = -5
        test2.unlimitedNumber = -3
        test1 += test2
        self.assertEquals(test1.unlimitedNumber, -8)
        test1.unlimitedNumber = 5
        test1 += test2
        self.assertEquals(test1.unlimitedNumber, 2)

    # Unit test for add post-increment operator
    def test_postIncrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.postIncrement().unlimitedNumber, 13)
        self.assertEquals(test1.unlimitedNumber, 13)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.postIncrement().unlimitedNumber, -9)
        self.assertEquals(test1.unlimitedNumber, -9)

    # Unit test for add pre-increment operator
    def test_preIncrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.preIncrement().unlimitedNumber, 12)
        self.assertEquals(test1.unlimitedNumber, 13)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.preIncrement().unlimitedNumber, -10)
        self.assertEquals(test1.unlimitedNumber, -9)

    # Unit test for sub operator
    def test_subOperator(self):
        test1 = Unlimited(12)
        test2 = Unlimited(12)
        subResult = test1 - test2
        self.assertEquals(subResult.unlimitedNumber, 0)
        test1.unlimitedNumber = -5
        subResult = test1 - test2
        self.assertEquals(subResult.unlimitedNumber, -17)
        test1.unlimitedNumber = 5
        test2.unlimitedNumber = 3
        subResult = test1 - test2
        self.assertEquals(subResult.unlimitedNumber, 2)
        test2.unlimitedNumber = -5
        subResult = test1 - test2
        self.assertEquals(subResult.unlimitedNumber, 10)

    # Unit test for sub with assignemnet to left side operator
    def test_isubOperator(self):
        test1 = Unlimited(12)
        test2 = Unlimited(12)
        test1 -= test2
        self.assertEquals(test1.unlimitedNumber, 0)
        test1.unlimitedNumber = -5
        test1 -= test2
        self.assertEquals(test1.unlimitedNumber, -17)
        test1.unlimitedNumber = 5
        test2.unlimitedNumber = 3
        test1 -= test2
        self.assertEquals(test1.unlimitedNumber, 2)
        test2.unlimitedNumber = -3
        test1 -= test2
        self.assertEquals(test1.unlimitedNumber, 5)

    # Unit test for sub post-decrement operator
    def test_postDecrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.postDecrement().unlimitedNumber, 11)
        self.assertEquals(test1.unlimitedNumber, 11)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.postDecrement().unlimitedNumber, -11)
        self.assertEquals(test1.unlimitedNumber, -11)

    # Unit test for sub post-decrement operator
    def test_preDecrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.preDecrement().unlimitedNumber, 12)
        self.assertEquals(test1.unlimitedNumber, 11)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.preDecrement().unlimitedNumber, -10)
        self.assertEquals(test1.unlimitedNumber, -11)

    # Unit test for print operator
    def test_printOperator(self):
        test1 = Unlimited(12)
        # auto invoke __str__
        self.assertEqual(str(test1), '12')
        self.assertNotEquals(str(test1), '13')
        test1.unlimitedNumber = -5
        self.assertEqual(str(test1), '-5')
        self.assertNotEquals(str(test1), '5')


if __name__ == '__main__':
    unittest.main()
