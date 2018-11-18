"""This module provides a Van class, a subtype of the Vehicle class."""

from vehicle import Vehicle

class Van(Vehicle):

    """This class is a subtype of the Vehicle class.

       Contains additional attributes of make and mode, and num of passengers.
       Supports polymorphic behavior of method getDescription.
    """
    
    def __init__(self, make_model, mpg, num_passengers, vin):
        """ Initializes with make-model, mpg, num_passengers, vin."""
        
        super().__init__(mpg, vin)

        self.__make_model = make_model
        self.__num_passengers = num_passengers


    def getDescription(self):
        """Returns complete description of van"""

        spacing = '  '
        descript = format(self.__make_model, '<22') + spacing + \
                   'passengers:' + format(self.__num_passengers, '>2') + \
                   spacing + Vehicle.getDescription(self)
                  
        return descript
