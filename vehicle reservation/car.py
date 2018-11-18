"""This module provides a Car class, a subtype of the Vehicle class."""

from vehicle import Vehicle

class Car(Vehicle):
    """This class is a subtype of the Vehicle class.

       Contains additional attributes of make and model, num of passengers, and
       num of doors. Supports polymorphic behavior of method getDescription.
    """
    
    def __init__(self, make_model, mpg, num_passengers, num_doors, vin):
        """Initialized with provided parameter values."""
        
        super().__init__(mpg, vin)

        self.__make_model = make_model
        self.__num_passengers = num_passengers
        self.__num_doors = num_doors


    def getDescription(self):
        """Returns description of car as a formatted string."""

        spacing = '   '
        descript = format(self.__make_model, '<18') + spacing + \
                   'passengers: ' + self.__num_passengers + spacing + \
                   'doors: ' + format(self.__num_doors, '<2') + spacing + \
                   Vehicle.getDescription(self)
          
        return descript

