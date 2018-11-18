"""This module provides a Reservations class."""

from reservation import Reservation

class Reservations:
    """This class provides the methods for maintaiing rental reservations."""

    def __init__(self):
        """Initializes empty collection of reservations."""
        
        self.__reservations = dict()
        

    def isReserved(self, vin):
        """Returns True if reservation for vin found, else returns False."""

        return vin in self.__reservations
    

    def getVinForReserv(self, credit_card):
        """Returns vin of vehicles reserved with credit_card."""
        
        return self.__reservations[credit_card].getVin()

    
    def addReservation(self, resv):
        """Adds new reservation."""

        self.__reservations[resv.getCreditCard()] = resv
        

    def findReservation(self, credit_card):
        """Returns True if reservation for credit_card, else returns False."""

        return credit_card in self.__reservations

        
    def cancelReservation(self, credit_card) -> object:
        """Deletes reservation matching provided credit card number."""

        del(self.__reservations[credit_card])


