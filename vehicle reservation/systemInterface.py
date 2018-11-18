"""This module provides a SystemInterface class for the Vehicle Rental Program.

   Vehicles File Format
   --------------------
   The format for the vehicles file contains comma-separated values with the
   indicated header lines for cars, vans, and trucks.

     #CARS#
     make-model, mpg, num-passengers, vin
     .
     #VANS#
     make-model, mpg, num passengers, vin
     .
     #TRUCKS#
     mpg, length, num rooms, vin
     .


   Vehicle Cost File Format
   ------------------------
   The format for the rental costs file includes a header line, followed
   by three lines of comma-separated values for cars, vans and trucks.

     daily, weekly, weekend, free miles, mileage charge, insurance

   The following exceptions are raised: IOError.
"""   
from vehicles import Vehicles, Car, Van, Truck
from vehicleCosts import VehicleCost, VehicleCosts
from reservations import Reservations

# symbolic constants
VEHICLE_TYPES = ('Car', 'Van', 'Truck')
VEHICLES_FILENAME = 'VehiclesStock.txt'
VEHICLE_COSTS_FILENAME = 'RentalCost.txt'

# exception class
class InvalidFileFormatError(Exception):
    """Exception indicating invalid file in file_name."""

    def __init__(self, header, file_name):
        self.__header = header
        self.__file_name = file_name

    def __str__(self):
        return 'FILE FORMAT ERROR: File header ' + self.__header + \
               ' expected in file ' + self.__file_name


class SystemInterface:
    """This class provides the system interface of the vehicle rental
       system.
    """
    def __init__(self):
        """Populates vehicles and rental costs from file. Raises IOError."""
        
        self.__vehicles = Vehicles()
        self.__vehicle_costs = VehicleCosts()
        self.__reservations = Reservations()
        self.__vehicle_info_file = None

        try:
            self.__vehicle_info_file = open(VEHICLES_FILENAME, 'r')
            self.__rental_cost_file = open(VEHICLE_COSTS_FILENAME, 'r')
            
            self.__populateVehicles(self.__vehicle_info_file)
            self.__populateCosts(self.__rental_cost_file)
        except InvalidFileFormatError as e:
            print(e)
            raise IOError
        except IOError:
            if self.__vehicle_info_file == None:
                print('FILE NOT FOUND:', VEHICLES_FILENAME)
            else:
                print('FILE NOT FOUND:', VEHICLE_COSTS_FILENAME)
            raise IOError

    def numAvailVehicles(self, vehicle_type):
        """Returns the number of available vehiles. Returns 0 if no
           no vehicles available.
        """
        
        return self.__vehicles.numAvailVehicles(vehicle_type)


    def getVehicle(self, vin):
        """Returns Vehicle type for given vin."""

        return self.__vehicles.getVehicle(vin)


    def getVehicleTypes(self):
        """Returns all vehicle types as a tuple of strings."""

        return VEHICLE_TYPES


    def getVehicleCosts(self, vehicle_type):
        """Returns vehicle costs for provided vehicle type as a list.

           List of form [daily rate, weekly rate, weekend rate,
                         num free miles, per mile charge, insur rate]
        """

        return self.__vehicle_costs.getVehicleCost(vehicle_type).getCosts()


    def getAvailVehicles(self, vehicle_type):
        """Returns a list of descriptions of unreserved vehicles."""
        
        avail_vehicles = self.__vehicles.getAvailVehicles(vehicle_type)
        return [veh for veh in avail_vehicles]
        

    def isReserved(self, vin):

        return self.__reservations.isReserved(vin)


    def findReservation(self, credit_card):

        return self.__reservations.findReservation(credit_card)

    
    def addReservation(self, resv):
        """Creates reservation and marks vehicles as reserved."""

        self.__reservations.addReservation(resv)


    def cancelReservation(self, credit_card):
        """Cancels reservation made with provided credit card."""

        vin = self.__reservations.getVinForReserv(credit_card)

        self.__vehicles.unreserveVehicle(vin)
        self.__reservations.cancelReservation(credit_card)
        

    def calcRentalCost(self, vehicle_type, rental_period,
                       want_insurance, miles_driving):
        """Returns estimate of rental cost for provided parameter values.

           Returns dictionary with key values: {'base_charges', 'insur_rate',
           'num_free_miles', 'per_mile_charge', 'estimated_mileage_charges'}
        """

        return self.__vehicle_costs.calcRentalCost(vehicle_type, rental_period,
                                            want_insurance, miles_driving)

    # ---- Private Methods

    def __populateVehicles(self, vehicle_file):
        """Gets vehicles from vehicle_file. Raises InvalidFileFormatError."""
        
        empty_str = ''

        # init vehicle string file headers
        vehicle_file_headers = ('#CARS#', '#VANS#', '#TRUCKS#')
        vehicle_type_index = 0
        
        # read first line of file (#CARS# expected)
        vehicle_str = vehicle_file.readline()
        vehicle_info = vehicle_str.rstrip().split(',')
        file_header_found = vehicle_info[0]
        expected_header = vehicle_file_headers[0]

        if file_header_found != expected_header:
            raise InvalidFileFormatError(expected_header, VEHICLES_FILENAME)
        else:
            # read next line of file after #CARS# header line
            vehicle_str = vehicle_file.readline()
            
            while vehicle_str != empty_str:

                # convert comma-separated string into list of strings
                vehicle_info = vehicle_str.rstrip().split(',')

                if vehicle_info[0][0] == '#':
                    vehicle_type_index = vehicle_type_index + 1
                    file_header_found = vehicle_info[0]
                    expected_header = vehicle_file_headers[vehicle_type_index]

                    if file_header_found !=  expected_header:
                        raise InvalidFileFormatError(expected_header,
                                                     VEHICLES_FILENAME)
                else:    

                    # create new vehicle object of the proper type
                    if file_header_found == '#CARS#':
                        vehicle = Car(*vehicle_info)
                    elif file_header_found == '#VANS#':
                        vehicle = Van(*vehicle_info)
                    elif file_header_found == '#TRUCKS#':
                        vehicle = Truck(*vehicle_info)
                    
                    # add new vehicle to vehicles list
                    self.__vehicles.addVehicle(vehicle)

                # read next line of vehicle information
                vehicle_str = vehicle_file.readline()


    def __populateCosts(self, cost_file):
        """Populates RentalCost objects from provided file object."""
               
        # skip file header / read first line of file
        cost_file.readline()
        cost_str = cost_file.readline()
        
        for veh_type in VEHICLE_TYPES:
            # strip off newline (last) character and split into list
            cost_info = cost_str.rstrip().split(',')

            for cost_item in cost_info:
                cost_item = cost_item.strip()
                
            # add Vehicle Type/Rental Cost key/value to dictionary
            self.__vehicle_costs.addVehicleCost(veh_type, VehicleCost(*cost_info))    

            # read next line of vehicle costs
            cost_str = cost_file.readline() 
