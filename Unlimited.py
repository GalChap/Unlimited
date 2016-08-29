import random


class Unlimited:

    # Constructor for unlimited class
    def __init__(self, unlimitedNumber = 0):
            self.unlimitedNumber = unlimitedNumber

    # comparision operators

    # Equal to operator ( == )
    def __eq__(self, other):
        if isinstance(other,Unlimited):
            return self.unlimitedNumber == other.unlimitedNumber

    # Not equal to operator ( != )
    def __ne__(self, other):
        if isinstance(other, Unlimited):
            return self.unlimitedNumber != other.unlimitedNumber

    # Less than or equal to operator ( <= )
    def __le__(self, other):
        if isinstance(other, Unlimited):
            return self.unlimitedNumber <= other.unlimitedNumber

    # Greater than or equal to operator ( >= )
    def __ge__(self, other):
        if isinstance(other, Unlimited):
            return self.unlimitedNumber >= other.unlimitedNumber

    #  Add operators

    # Add operator ( + )
    def __add__(self, other):
        if isinstance(other, Unlimited):
            return Unlimited(self.unlimitedNumber + other.unlimitedNumber)

    # Add with assignment to left side operator ( += )
    def __iadd__(self, other):
        if isinstance(other, Unlimited):
            self = self + other
            return self

    # Postincrement operator ( self++ )
    def postIncrement(self):
        self.unlimitedNumber = self.unlimitedNumber+1
        return  Unlimited(self.unlimitedNumber-1)

    # Preincrement operator ( ++self )
    def preIncrement(self):
        self.unlimitedNumber = self.unlimitedNumber + 1
        return self

    # Sub operators

    # Sub operator ( - )
    def __sub__(self, other):
        if isinstance(other, Unlimited):
            return Unlimited(self.unlimitedNumber - other.unlimitedNumber)

    # Sub with assignemnet to left side operator ( -= )
    def __isub__(self, other):
        if isinstance(other, Unlimited):
            self = self - other
            return self

    # Postdecrement operator ( self-- )
    def postDecrement(self):
        self.unlimitedNumber = self.unlimitedNumber-1
        return  Unlimited(self.unlimitedNumber+1)

    # Predecrement operator ( --self )
    def preDecrement(self):
        self.unlimitedNumber = self.unlimitedNumber-1
        return self

    # Print operator
    def __str__(self):
        return str(self.unlimitedNumber)

    # Create random number to Unlimited object.
    # return Unlimited object
    def randomUnlimitedNumber(self,upperRange):
        try:
         randNumber = random.randint(1,upperRange)
         self.unlimitedNumber = random.randrange(random.getrandbits(randNumber));
        except Exception as e:
            print ("Couldn't create random number", e)
        if (False == random.choice((True,False))):
            self.unlimitedNumber = -self.unlimitedNumber
        return self

'''
test1 = Unlimited()
for number in range(100):
    test1.randomUnlimitedNumber(100000)
    print('\n')
    print(test1)


for number in range(10):
    print('\n')
    test1 = Unlimited()
    test1.randomUnlimitedNumber(1000)
    test2 = Unlimited()
    test2.randomUnlimitedNumber(1000)
    if test1 >= test2:
        test1 -= test2
        print(test1)
    else:
        test2 -= test1
        print(test2)
'''