import random
import sys

class Unlimited:

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

    # Add operator ( + )
    def __add__(self, other):
        if isinstance(other, Unlimited):
            return Unlimited(self.unlimitedNumber + other.unlimitedNumber)

    # Add with assignemnet to left side operator ( += )
    def __iadd__(self, other):
        if isinstance(other, Unlimited):
            self = self + other
            return self

    # Postincrement operator ( self++ )
    def postincrement(self):
        self.unlimitedNumber = self.unlimitedNumber+1
        return self

    # Preincrement operator ( ++self )
    def preincrement(self):
        self.unlimitedNumber = self.unlimitedNumber+1
        return  Unlimited(self.unlimitedNumber-1)

    # Sub operator ( - )
    def __sub__(self, other):
        if isinstance(other, Unlimited):
            return Unlimited(self.unlimitedNumber - other.unlimitedNumber)

    # Sub with assignemnet to left side operator ( -= )
    def __isub__(self, other):
        if isinstance(other, Unlimited):
            self = self - other
            return self

    # Postdecincrement operator ( self-- )
    def postdecincrement(self):
        self.unlimitedNumber = self.unlimitedNumber-1
        return self

    # Preincrement operator ( --self )
    def predecincrement(self):
        self.unlimitedNumber = self.unlimitedNumber-1
        return  Unlimited(self.unlimitedNumber+1)

    def __str__(self):
        return str(self.unlimitedNumber)

    def randomunlimitednumber(self):
        try:
         #randNumber = random.randint(1,1000000)
         self.unlimitedNumber = random.randrange(random.getrandbits(sys.maxsize));
        except Exception as e:
            print ("Couldn't create random number", e)
        if (False == bool(random.getrandbits(1))):
            return  -self.unlimitedNumber
        return self.unlimitedNumber



un1 = Unlimited(1235)
un2 = Unlimited(123)

un1 = un1 + un2
for number in range(100):
    un2.unlimitedNumber = un2.randomunlimitednumber();
    if (un2.unlimitedNumber <1000):
        print("\n")
        print(un2)



