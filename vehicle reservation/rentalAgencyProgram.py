# Rental Agency Program

""" This program performs the tasks of a vehicle rental agency, including the
    display of vehicle information and the ability to make/cancel reservations.
"""
from systemInterface import SystemInterface
from rentalAgencyUI import RentalAgencyUI

try:
    # create system with populated data from file
    sys = SystemInterface()

    # associate user interface with system
    ui = RentalAgencyUI(sys)

    # start the user interface
    ui.start()
    
except IOError:
    print('** PROGRAM TERMINATION (IO Error) **')

       

