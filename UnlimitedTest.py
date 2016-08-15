import unittest
from main import Unlimited




class TestUnlimited(unittest.TestCase):

    def test_equalOperator(self):
            test1 = Unlimited(1234)
            test2 = Unlimited(1234)
            self.assertEquals( test1 == test2, True)
            test1.unlimitedNumber = 123
            self.assertEquals(test1 == test2, False)

    def test_notEqualOperator(self):
        test1 = Unlimited(1234)
        test2 = Unlimited(1234)
        self.assertEquals(test1 != test2, False)
        test1.unlimitedNumber = 123
        self.assertEquals(test1 != test2, True)

    def test_lessEqualOperator(self):
        test1 = Unlimited(1234)
        test2 = Unlimited(1234)
        self.assertEquals(test1 <= test2, True)
        test1.unlimitedNumber = 12345
        self.assertEquals(test1 <= test2, False)
        test1.unlimitedNumber = 123
        self.assertEquals(test1 <= test2, True)

    def test_greaterEqualOperator(self):
        test1 = Unlimited(1234)
        test2 = Unlimited(1234)
        self.assertEquals(test1 >= test2, True)
        test1.unlimitedNumber = 12345
        self.assertEquals(test1 >= test2, True)
        test1.unlimitedNumber = 123
        self.assertEquals(test1 >= test2, False)

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


if __name__ == '__main__':
    unittest.main()
