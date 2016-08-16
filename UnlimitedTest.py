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

    def test_postincrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.postincrement().unlimitedNumber, 13)
        self.assertEquals(test1.unlimitedNumber, 13)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.postincrement().unlimitedNumber, -9)
        self.assertEquals(test1.unlimitedNumber, -9)

    def test_preincrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.preincrement().unlimitedNumber, 12)
        self.assertEquals(test1.unlimitedNumber, 13)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.preincrement().unlimitedNumber, -10)
        self.assertEquals(test1.unlimitedNumber, -9)

    def test_postdecincrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.postdecincrement().unlimitedNumber, 11)
        self.assertEquals(test1.unlimitedNumber, 11)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.postdecincrement().unlimitedNumber, -11)
        self.assertEquals(test1.unlimitedNumber, -11)

    def test_predecincrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.predecincrement().unlimitedNumber, 12)
        self.assertEquals(test1.unlimitedNumber, 11)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.predecincrement().unlimitedNumber, -10)
        self.assertEquals(test1.unlimitedNumber, -11)

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
