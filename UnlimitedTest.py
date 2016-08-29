import unittest
from Unlimited import Unlimited
import  sys



class TestUnlimited(unittest.TestCase):

    global test_unlimitedTypeLimitsLoop
    test_unlimitedTypeLimitsLoop = 100

    global test_unlimitedTypeLimitsSizeOfNumner
    test_unlimitedTypeLimitsSizeOfNumner = 100000

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
        self.assertEquals(test1.postIncrement().unlimitedNumber, 12)
        self.assertEquals(test1.unlimitedNumber, 13)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.postIncrement().unlimitedNumber, -10)
        self.assertEquals(test1.unlimitedNumber, -9)

    # Unit test for add pre-increment operator
    def test_preIncrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.preIncrement().unlimitedNumber, 13)
        self.assertEquals(test1.unlimitedNumber, 13)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.preIncrement().unlimitedNumber, -9)
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
        self.assertEquals(test1.postDecrement().unlimitedNumber, 12)
        self.assertEquals(test1.unlimitedNumber, 11)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.postDecrement().unlimitedNumber, -10)
        self.assertEquals(test1.unlimitedNumber, -11)

    # Unit test for sub post-decrement operator
    def test_preDecrement(self):
        test1 = Unlimited(12)
        self.assertEquals(test1.preDecrement().unlimitedNumber, 11)
        self.assertEquals(test1.unlimitedNumber, 11)
        test1.unlimitedNumber = -10
        self.assertEquals(test1.preDecrement().unlimitedNumber, -11)
        self.assertEquals(test1.unlimitedNumber, -11)

    # Unit test for print operator
    def test_printOperator(self):
        test1 = Unlimited(12)
        self.assertEqual(str(test1), '12')
        self.assertNotEquals(str(test1), '13')
        test1.unlimitedNumber = -5
        self.assertEqual(str(test1), '-5')
        self.assertNotEquals(str(test1), '5')

    # Unit test for random function
    def test_randomUnlimitedNumber(self):
        test1 = Unlimited()
        test1.randomUnlimitedNumber(100)
        self.assertIsInstance(test1.unlimitedNumber,int)
        self.assertRaises(Exception, test1.randomUnlimitedNumber(sys.maxsize*10))

    # Unit test for check multiple pair of Unilmited type instance
    def test_unlimitedTypeLimits(self):
        for number in range (test_unlimitedTypeLimitsLoop):
            test1 = Unlimited()
            # Use of create random number function
            test1.randomUnlimitedNumber(test_unlimitedTypeLimitsSizeOfNumner)
            test2 = Unlimited()
            # Use of create random number function
            test2.randomUnlimitedNumber(test_unlimitedTypeLimitsSizeOfNumner)
            if test1 >= test2:
                self.assertGreaterEqual(test1, test2)
                self.addOperatorTest(test1, test2)
                self.iaddOperatorTest(test1, test2)
                self.postIncrementOperatorTest(test1)
                self.preIncrementOperatorTest(test1)
                self.subOperatorTest(test1, test2)
                self.isubOperatorTest(test1, test2)
                self.postDecrementOperatorTest(test1)
                self.preDecrementOperatorTest(test1)
                #Use of printOperator
                print("Test number 1:",test1, "\nIs greater equal from", "\nTest number 2:",test2, "\n")
            else:
                self.assertLessEqual(test1, test2)
                self.addOperatorTest(test1, test2)
                self.iaddOperatorTest(test1, test2)
                self.postIncrementOperatorTest(test1)
                self.preIncrementOperatorTest(test1)
                self.subOperatorTest(test2, test1)
                self.isubOperatorTest(test2, test1)
                self.postDecrementOperatorTest(test1)
                self.preDecrementOperatorTest(test1)
                # Use of printOperator
                print("Test number 1:",test1, "\nIs less equal from", "\nTest number 2:",test2, "\n")

    # Help function for add operator
    def addOperatorTest(self, test1Param, test2Param):
        result = test1Param + test2Param
        self.assertEquals(result, test1Param + test2Param)

    # Service function for iadd operator
    def iaddOperatorTest(self, test1Param, test2Param):
        result = test1Param
        test1Param += test2Param
        self.assertEquals(test1Param, result + test2Param)

    # Service function for post-increment operator
    def postIncrementOperatorTest(self, test1Param):
        result = test1Param.unlimitedNumber
        self.assertEquals(test1Param.postIncrement().unlimitedNumber, result)
        # to show that test1 value incremented after reading it's value
        self.assertEquals(test1Param.unlimitedNumber, result + 1)

    # Service function for pre-increment operator
    def preIncrementOperatorTest(self, test1Param):
        result = test1Param.unlimitedNumber
        self.assertEquals(test1Param.preIncrement().unlimitedNumber, result + 1)
        # to ensure that test1Param value incremented before reading the value
        self.assertEquals(test1Param.unlimitedNumber, result + 1)

    # Service function for sub operator
    def subOperatorTest(self, test1Param, test2Param):
        result = test1Param - test2Param
        self.assertEquals(result, test1Param - test2Param)

    # Service function for isub operator
    def isubOperatorTest(self, test1Param, test2Param):
        result = test1Param
        test1Param -= test2Param
        self.assertEquals(test1Param, result - test2Param)

    # Service function for post-increment operator
    def postDecrementOperatorTest(self, test1Param):
        result = test1Param.unlimitedNumber
        self.assertEquals(test1Param.postDecrement().unlimitedNumber, result)
        # to show that test1 value incremented after reading it's value
        self.assertEquals(test1Param.unlimitedNumber, result - 1)

    # Service function for pre-increment operator
    def preDecrementOperatorTest(self, test1Param):
        result = test1Param.unlimitedNumber
        self.assertEquals(test1Param.preDecrement().unlimitedNumber, result - 1)
        # to ensure that test1Param value incremented before reading the value
        self.assertEquals(test1Param.unlimitedNumber, result - 1)


if __name__ == '__main__':
    unittest.main()
