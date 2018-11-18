'''This module provides a Vehicle class.'''

class Vehicle:
    """ The Vehicle class holds the mpg, vin and reserved flag of a vehicle.

        Contains attributes common to all vehicles: mpg, vin, and reserved
        (Boolean). Provides polymorphic behavior for method getDescription.
    """
    
    def __init__(self, mpg, vin):
        ''' Initializes a Vehicle object with mpg and vin.'''

        self.__mpg = mpg
        self.__vin = vin
        self.__reserved = False


    def getType(self):
        '''Returns the type of vehicle (car, van, truck.)'''
        
        return type(self).__name__


    def getVin(self):
        '''Returns the vin of vehicle.'''
        
        return self.__vin


    def getDescription(self):
        '''Returns general description of car, not specific to type'''
        
        descript = 'mpg:' + format(self.__mpg, '>3') + '   ' + \
                   'vin:' + format(self.__vin, '>12')
        
        return descript


    def isReserved(self):
        '''Returns True if vehicle is reserved, otherwise returns False.'''
        
        return self.__reserved


    def setReserved(self, reserved):
        '''Sets reserved flag of vehicle to provided Boolean value.'''

        self.__reserved = reserved

