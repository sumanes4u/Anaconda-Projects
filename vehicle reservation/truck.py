"""This module provides a Truck class. a subtype of the Vehicle class."""

from vehicle import Vehicle

class Truck(Vehicle):

    """This class is a subtype of the Vehicle class.

       Contains additional attributes length and num of rooms storage capacity.
       Supports polymorphic behavior of method getDescription.
    """
    
    def __init__(self, mpg, length, num_rooms, vin):
        """ Initializes with mpg, length, num_rooms, vin."""

        super().__init__(mpg, vin)
        
        self.__length = length
        self.__num_rooms = num_rooms


    def getDescription(self):
        """Returns complete description of truck."""

        spacing = '   '
        descript = 'length(feet):' + format(self.__length, '>3') + spacing + \
                  'rooms:' + format(self.__num_rooms, '>2') + spacing + \
                  Vehicle.getDescription(self)
                  
        return descript

