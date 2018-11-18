# MixedFraction Class

from fraction import *

class MixedFraction(Fraction):

    def __init__(self, *args):
        
        if len(args) == 2:
            Fraction.__init__(self, args[0], args[1])    
        elif len(args) == 3:
            Fraction.__init__(self, args[1] + args[0] * args[2], args[2])
        else:
            raise TypeError('MixedFraction takes 2 or 3 arguments ' + \
               '(' + str(len(args)) + ' given)')
        
            
    def __str__(self):

        empty_str = ''
        blank = ' '
        
        displayFrac = Fraction.copy(self)
        displayFrac.reduce()

        whole_num = 0
        numer = displayFrac.getNumerator()
        denom = displayFrac.getDenominator()

        if numer == 0:
            return '0'

        if denom == 1:
            return str(numer)

        if numer < 0:
            numer = abs(numer)
            sign = '-'
        else:
            sign = empty_str
            
        if abs(numer) > abs(denom):
            whole_num = abs(numer) // abs(denom)
            numer = abs(numer) % abs(denom)
            
        if whole_num == 0:
            return sign + str(numer) + '/' + str(denom)
        else:
            return sign + str(whole_num) + blank + \
                   str(numer) + '/' + str(denom)     

    def __repr__(self):
        
        return self.__str__()
    

    def getWholeNum(self):
        
        return self.getNumerator() // self.getDenominator()
        

    def setWholeNum(self, value):
        
        self.setNumerator(self.getNumerator() + \
                              value * self.getDenominator())
        

    def set(self, whole_num, numer, denom):
        
        Fraction.set(self, numer + whole_num * denom, denom)
        

    def __neg__(self):
                
        return MixedFraction(-Fraction.getNumerator(self),
                             Fraction.getDenominator(self))

    def __sub__(self, rfraction):
        
        tempFrac = Fraction.__sub__(self, rfraction)
        
        return self.__createMixedFraction(tempFrac)
    

    def __add__(self, rfraction):

        tempFrac = Fraction.__add__(self, rfraction)
        
        return self.__createMixedFraction(tempFrac)
    

    def __mul__(self, rfraction):
        
        tempFrac = Fraction.__mul__(self, rfraction)
        
        return self.__createMixedFraction(tempFrac)
    

    def __createMixedFraction(self, frac):
        
        numer = frac.getNumerator()
        denom = frac.getDenominator()

        return MixedFraction(numer, denom)
        
