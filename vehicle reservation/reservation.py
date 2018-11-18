"""This module contains a Reservation class for storing details of a rental."""

class Reservation:
    """This class provides the methods for maintaining reservations info."""
    
    def __init__(self, name, address, credit_card, vin):
        """ Initialzes a Reservation object with name, address, credit_card
            and vin.
        """

        self.__name = name
        self.__address = address
        self.__credit_card = credit_card
        self.__vin = vin
        
    def getName(self):
        """Returns first and last name for reservation."""
        
        return self.__name

    def getAddress(self):
        """Returns address for reservation."""
        
        return self.__address

    def getCreditCard(self):
        """Returns credit card on reservation."""
        
        return self.__credit_card

    def getVin(self):
        """Returns vehicle identification number on reservation."""
        
        return self.__vin

