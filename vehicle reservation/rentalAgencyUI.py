"""
    This module provides class RentalAgencyUI, a console user interface.

    Method start begins execution of the interface. Raises IOError exception.
"""
from systemInterface import VEHICLE_TYPES
from vehicles import InvalidVinError
from vehicleCosts import DAILY_RENTAL, WEEKLY_RENTAL, WEEKEND_RENTAL
from reservations import Reservation

class RentalAgencyUI:
    """This class provides a console interface for the rental agency system."""

    def __init__(self, sys):
        """Stores the provided reference to the vehicle rental system."""
        self.__sys = sys


    def start(self):
        """Begins the command loop."""
        
        self.__displayWelcomeScreen()
        self.__displayMenu()
        
        selection = self.__getSelection(7)
        
        while selection != 7:
            self.__executeCmd(selection)
            self.__displayMenu()
            selection = self.__getSelection(7)
   
        print('Thank you for using the Friendly Rental Agency')
        

    # Private Methods

    def __displayWelcomeScreen(self):
        """PRIVATE: Displays welcome message and general instructions."""

        print('*****************************************************')
        print('  * Welcome to the Friendly Vehicle Rental Agency *')
        print('*****************************************************')


    def __displayMenu(self):
        """PRIVATE: Displays a list of menu options on the screen."""
	  	  		   	 	 	 
        print('\n<<< MAIN MENU >>>')
        print('1 - Display vehicle types')
        print('2 - Check rental costs')
        print('3 - Check available vehicles')
        print('4 - Get cost of specific rental')
        print('5 - Make a reservation')
        print('6 - Cancel a reservation')
        print('7 - Quit\n')


    def __getSelection(self, num_selections, prompt='Enter: '):
        """PRIVATE: Returns user-entered value in range 1-num_selections."""
        
        valid_input = False

        selection = input(prompt)
        
        while not valid_input:
            try:
                selection = int(selection)

                if selection < 1 or selection > num_selections:
                    print('* Invalid Entry*\n')
                    selection = input(prompt)
                else:
                    valid_input = True
            except ValueError:
                selection = input(prompt)

        return selection


    def __displayDivLine(self, title = ''):
        """PRIVATE: Displays line of dashes, with optional title."""
        
        if len(title) != 0:
            title = ' ' + title + ' '
        print(title.center(70,'-'))

	
    def __executeCmd(self, selection):
        """PRIVATE: Executes command for provided menu selection."""
        
        if selection == 1:
            self.__CMD_DisplayVehicleTypes()
        elif selection == 2:
            self.__CMD_DisplayVehicleCosts()
        elif selection == 3:
            self.__CMD_PromptAndDisplayAvailVehicles()
        elif selection == 4:
            self.__CMD_DisplaySpecificRentalCost()
        elif selection == 5:    
            self.__CMD_MakeReservation()
        elif selection == 6:    
            self.__CMD_CancelReservation()
            

    def __CMD_DisplayVehicleTypes(self):
        """PRIVATE: Displays vehicle types (Cars, Vans, Trucks)."""
        
        self.__displayDivLine('Types of Vehicles Available for Rent')
        self.__displayVehicleTypes()
        self.__displayDivLine()
        

    def __CMD_DisplayVehicleCosts(self):
        """PRIVATE: Displays rental costs for Cars, Vans, Trucks."""
        
        empty_str = ''
        blank_char = ' '

        # get vehicle type from user
        self.__displayVehicleTypes()
        vehicle_type_num = self.__getSelection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]

        # set column headings
        row1_colheadings = blank_char * 24 + format('Free', '7') + \
                           format('Per Mile', '10') + format('Insurance', '17')

        row2_colheadings = format('Daily', '7') + format('Weekly', '8') + \
                           format('Weekend', '9') + format('Miles', '7') + \
                           format('Charge', '10') + format('(per day)', '17')      
            
        # get vehicle costs
        costs = self.__sys.getVehicleCosts(vehicle_type)

        # build costs line to display
        costs_str = empty_str

        field_widths = ('7', '8', '9', '7', '10', '17')
        for k in range(0, len(costs)):
            costs_str = costs_str + format(costs[k],'<' + field_widths[k])

        # display headings and costs line
        self.__displayDivLine('Rental Charges for ' + vehicle_type + 's')
        print()
        print(row1_colheadings + '\n' + row2_colheadings + '\n' + costs_str)
        self.__displayDivLine()


    def __CMD_DisplayAvailVehicles(self, vehicle_type, numbered=False):
        """PRIVATE: Displays unreserved vehicles of selected type.
           When default argument is True, lists vehicles with sequential
           numbers at the start of the line of each vehicle description.
        """
        
        avail_vehicles_list = self.__sys.getAvailVehicles(vehicle_type)
        self.__displayDivLine('Available ' + vehicle_type + 's')

        if avail_vehicles_list == []:
            print('* No Vehicles Available of this Type *')
        elif numbered:
            k = 1
            for veh in avail_vehicles_list:
                print(str(k) + '-' + veh.getDescription())
                k = k + 1
        else:    
            for veh in avail_vehicles_list:
                print(veh.getDescription())                           


    def __CMD_PromptAndDisplayAvailVehicles(self):
        """PRIVATE: Prompts user for vehicle type, and displays all
           available vehicles of that type.
        """
        
        self.__displayVehicleTypes()
        vehicle_type_num = self.__getSelection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]
        self.__CMD_DisplayAvailVehicles(vehicle_type)

    def __CMD_DisplaySpecificRentalCost(self):
        """PRIVATE: Prompts user for selections and displays rental cost."""

        # get vehicle type and rental period from user
        self.__displayVehicleTypes()
        vehicle_type_num = self.__getSelection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]

        # assign tuple, e.g. ('DAILY_RENTAL', '4')
        rental_period = self.__getRentalPeriod()

        # prompt user for optional insurance
        want_insurance = input('Would you like the insurance? (y/n): ')
        
        while want_insurance not in ('y', 'Y', 'n', 'N'):
            want_insurance = input('Would you like the insurance? (y/n): ')
        
        # convert to Boolean value
        want_insurance = want_insurance in ('y', 'Y')

        # prompt user for num of miles expected to drive
        print('\nNumber of miles expect to drive?')
        num_miles = self.__getSelection(1000, prompt = 'Miles: ')
    
        # calc base rental cost
        rental_cost = self.__sys.calcRentalCost(vehicle_type, rental_period,
                                                want_insurance, num_miles)
        # display estimated rental cost
        print()
        self.__displayDivLine('ESTIMATED ' + vehicle_type + ' RENTAL COST')
        
        if want_insurance:
            print('Insurance rate of', rental_cost['insur_rate'], 'per day')
        else:
            print('* You have opted out of insurance coverage *')

        if rental_period[0] == DAILY_RENTAL:
            print('\nDaily rental for', rental_period[1],
                  'days would be $', format(rental_cost['base_charges'], '.2f'))
        elif rental_period[0] == WEEKLY_RENTAL:
            print('\nWeekly rental for', rental_period[1],
                  'weeks would be $', format(rental_cost['base_charges'], '.2f'))
        elif rental_period[0] == WEEKEND_RENTAL:
            print('\nWeekend rental is $', rental_cost['base_charges'])
            
        est_total_cost = rental_cost['base_charges'] + \
                         rental_cost['estimated_mileage_charges']

        print('\nYour cost with an estimated mileage of',
              num_miles, 'miles would be', format(est_total_cost, '.2f'))
        
        print('which includes', rental_cost['num_free_miles'],
              'free miles and a charge of',
              format(rental_cost['per_mile_charge'], '.2f' ), 'per mile')
        
        self.__displayDivLine()
            

    def __CMD_MakeReservation(self):
        """PRIVATE: Prompts user for vehicle vin and reserves vehicle."""

        # get vehicle type
        self.__displayVehicleTypes()
        vehicle_type_num = self.__getSelection(len(VEHICLE_TYPES))
        vehicle_type = VEHICLE_TYPES[vehicle_type_num - 1]

        if self.__sys.numAvailVehicles(vehicle_type) == 0:
            print('Sorry - No available', \
                  VEHICLE_TYPES[vehicle_type_num - 1] + 's', 'at the moment')
        else:
            self.__CMD_DisplayAvailVehicles(vehicle_type, numbered=True)
            avail_vehicles = self.__sys.getAvailVehicles(vehicle_type)
        
            valid_input = False
            
            while not valid_input:
                selected = input('\nEnter number of vehicle to reserve: ')

                if not selected.isdigit():
                    print('Please enter the number preceeding the vehicle')
                elif int(selected) < 1 or \
                      int(selected) > self.__sys.numAvailVehicles(vehicle_type):
                    print('\nINVALID SELECTION - Please re-enter: ')
                else:
                    valid_input = True
 
            vin = avail_vehicles[int(selected) - 1].getVin()
            vehicle = self.__sys.getVehicle(vin)
            print(vehicle.getDescription())
            
            vehicle.setReserved(True)
            
            name = input('\nEnter first and last name: ')
            addr = input('Enter address: ')
            credit_card = input('Enter credit card number: ')

            reserv = Reservation(name, addr, credit_card, vin)
            self.__sys.addReservation(reserv)
            print('* Reservation Made *')


    def __CMD_CancelReservation(self):
        """PRIVATE: Prompts user for credit card and cancels reservation."""

        credit_card = input('Please enter your credit card number: ')
        
        if self.__sys.findReservation(credit_card):
            print('Calling cancelReservation of sys')  # **************
            self.__sys.cancelReservation(credit_card)
            print('** RESERVATION CANCELLED **')
        else:
            print('* Reservation not Found - Invalid Credit Card Entered *')

            
    def __displayVehicleTypes(self):
        """PRIVATE: Displays the numbered selection of vehicle types."""
        
        print('\nEnter type of vehicle')
        vehicle_types = self.__sys.getVehicleTypes()

        k = 1
        
        for veh_type in vehicle_types:
            print(k, '-', veh_type)
            k = k + 1
            
        print()
        
    
    def __getRentalPeriod(self):
        """PRIVATE: Prompts user for desired rental period.

           Returns tuple of the form (x, n), where x is one of DAILY_RENTAL,
           WEEKLY_RENTAL or WEEKEND_RENTAL, and n is the number of those units,
           e.g. (DAILY_RENTAL, 3) three days of a daily rental.
        """
        print('\nEnter the rental period:')
        print(DAILY_RENTAL, '- Daily ', WEEKLY_RENTAL, '- Weekly ',
              WEEKEND_RENTAL, '- Weekend\n')
                        
        valid_input = False

        while not valid_input:
            try:
                selection = int(input('Enter: '))
            
                while selection not in (DAILY_RENTAL, WEEKLY_RENTAL,
                                        WEEKEND_RENTAL):
                  
                    print('* Incorrect entry. Please Re-enter *\n')
                    selection = int(input('Enter: '))

                if selection == DAILY_RENTAL:
                  
                    print('How many days do you need the vehicle?', end = '')
                    num_days = self.__getSelection(14, prompt = ' ')

                    if num_days > 6:
                        print("Why don't you consider a weekly rental?\n")
                            
                    return (DAILY_RENTAL, num_days)
                elif selection == WEEKLY_RENTAL:
                    print('How many weeks do you need the vehicle? (1-3): ')
                    num_weeks = self.__getSelection(3, prompt = 'Weeks: ')
                    
                    return (selection, num_weeks)

                elif selection == WEEKEND_RENTAL:
                    return (selection, 1)

            except ValueError:
                print('* Invalid Input - Number Expected *\n') 
