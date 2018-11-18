"""Vehicles class module. Raises InvalidFileFormatError and InvalidVinError."""

from vehicle import Vehicle
from car import Car
from van import Van
from truck import Truck

class InvalidVinError(Exception):
    """Exception indicating that a provided vin was not found."""
    pass


class Vehicles:
    """This class maintains a collection of Vehicle objects."""

    def __init__(self):
        """Initializes empty list of vehicles."""
        
        self.__vehicles = []


    def getVehicle(self, vin: object) -> object:
        """Returns Vehicle for provided vin. Raises InvalidVinError."""

        for vehicle in self.__vehicles:
            if vehicle.getVin() == vin:
                return vehicle
       
        raise InvalidVinError


    def addVehicle(self, vehicle):
        """Adds new vehicle to list of vehicles."""
        
        self.__vehicles.append(vehicle)


    def numAvailVehicles(self, vehicle_type):
        """Returns number of available vehicles of vehicle_type."""
        
        return len(self.getAvailVehicles(vehicle_type))
        

    def getAvailVehicles(self, vehicle_type):
        """Returns a list of unreserved Vehicles objects of vehicle_type."""
       
        return [veh for veh in self.__vehicles \
                if veh.getType() == vehicle_type and not veh.isReserved()]

    def unreserveVehicle(self, vin):
        """Sets reservation status of vehicle with vin to unreserved."""
       
        k = 0
        found = False
        
        while not found:
            if self.__vehicles[k].getVin() == vin:
                self.__vehicles[k].setReserved(False)
                found = True

        






    
