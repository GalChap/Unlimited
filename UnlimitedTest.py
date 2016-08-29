import unittest
from Unlimited import Unlimited
import  sys



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
    '''
    # Unit test for check Unilmited type limits
    def test_unlimitedTypeLimits(self):
        test1 = Unlimited()
        test1.randomUnlimitedNumber(100)
        test2 = Unlimited()
        test2.randomUnlimitedNumber(100)
        if test1 >= test2:
            print("if")
            self.assertGreaterEqual(test1, test2)
            result = test1 + test2
            self.assertEqual(result, test1 + test2)
            result.unlimitedNumber = 0
            result+= test1
            self.assertEqual(result, test1)
            self.assertEqual(result.postIncrement().unlimitedNumber, test1.unlimitedNumber + 1)
            test1.postIncrement()
            self.assertEqual(result.preIncrement().unlimitedNumber, test1.unlimitedNumber)
            print(test1)
            print(test2)
        elif test1 <= test2:
            print("else")
            self.assertLessEqual(test1, test2)
            result = test2 + test1
            self.assertEqual(result, test2 + test1)
            print(test1)
            print(test2)
    '''

    # Help function for equal operator
    def equalOperatorTest(self, test1, test2):
     self.assertEquals(test1 == test2, True)

    # Help function for add operator
    def addOperatorTest(self, test1, test2):
        result = test1 + test2
        self.assertEquals(result, test1 + test2)

    # Help function for iadd operator
    def iaddOperatorTest(self, test1, test2):
        result = test1
        test1 += test2
        self.assertEquals(test1, result + test2)

    # Help function for postIncrement operator
    def postIncrementOperatorTest(self, test1):
        result = test1.unlimitedNumber
        self.assertEquals(test1.postIncrement().unlimitedNumber, result)
        # to show that test1 value change after reading it's value
        self.assertEquals(test1.unlimitedNumber, result + 1)


    # Help function for preIncrement operator
    def preIncrementOperatorTest(self, test1):
        result = test1.unlimitedNumber
        self.assertEquals(test1.preIncrement().unlimitedNumber, result + 1)
        # to ensure that test1 value change before reading the value
        self.assertEquals(test1.unlimitedNumber, result + 1)

    # Unit test for check Unilmited type limits
    def test_unlimitedTypeLimits(self):
        test1 = Unlimited()
        test1.randomUnlimitedNumber(100)
        test2 = Unlimited()
        test2.randomUnlimitedNumber(100)
        if test1 >= test2:
            print("if")
            self.assertGreaterEqual(test1, test2)
           # self.equalOperatorTest(test1, test2)
            self.addOperatorTest(test1, test2)
            self.iaddOperatorTest(test1, test2)
            self.postIncrementOperatorTest(test1)
            self.preIncrementOperatorTest(test1)
            print("end if")
        else:
            print("else")





if __name__ == '__main__':
    unittest.main()
