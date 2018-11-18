""" This module provides a VehicleCosts class."""

from vehicleCost import VehicleCost

# symbol constants
DAILY_RENTAL = 1
WEEKLY_RENTAL = 2
WEEKEND_RENTAL = 3

class VehicleCosts:
    """This class provides the methods for maintaining rental costs."""
    
    def __init__(self):
        """Initializes vehicle costs to empty."""

        self.__vehicle_costs = dict()

    
    def getVehicleCost(self, vehicle_type):
        """Returns VehicleCost object for the specified vehicle type."""
        
        return self.__vehicle_costs[vehicle_type]


    def addVehicleCost(self, veh_type, veh_cost):
        """Adds a vehicle cost object to dictionary with keyword veh_type."""

        self.__vehicle_costs[veh_type] = veh_cost


    def calcRentalCost(self, vehicle_type, rental_period,
                       want_insurance, miles_driving):
        """Returns estimate of rental cost for provided parameter values, where
           rental_period of the form (x, n), x is one of DAILY_RENTAL,
           WEEKLY_RENTAL or WEEKEND_RENTAL, and n is the number of those units.

           Returns dictionary with key values: {'base_charges', 'insur_rate',
           'num_free_miles', 'per_mile_charge', 'estimated_mileage_charges'}
        """

        # get vehicle cost
        vehicle_cost = self.getVehicleCost(vehicle_type)
        
        # calc rental charges
        rental_time = rental_period[1]
        
        if rental_period[0] == DAILY_RENTAL:
            rental_rate = vehicle_cost.getDailyRate()
            rental_period_value = DAILY_RENTAL
            rental_period_str = 'daily rental'
            rental_days = rental_time
        elif rental_period[0] == WEEKLY_RENTAL:
            rental_rate = vehicle_cost.getWeeklyRate()
            rental_period_value = WEEKLY_RENTAL
            rental_period_str = 'weekly rental'
            rental_days = rental_time * 7
        elif rental_period[0] == WEEKEND_RENTAL:
            rental_rate = vehicle_cost.getWeekendRate()
            rental_period_value = WEEKEND_RENTAL
            rental_period_str = 'weekend rental'
            rental_days = 2
            
        # get free miles, per mile charge and insurance rate
        num_free_miles = vehicle_cost.getFreeMiles()
        per_mile_charge = vehicle_cost.getPerMileCharge()
        insurance_rate = vehicle_cost.getInsuranceRate()

        # calc rental charge for selected rental period
        if not want_insurance:
            insurance_rate = 0

        # calc base rental charges
        if rental_period[0] == WEEKLY_RENTAL:
            base_rental_charges = rental_days // 7 * rental_rate + \
                                  rental_days * insurance_rate
        elif rental_period[0] == WEEKEND_RENTAL:
            base_rental_charges = rental_days // 2 * rental_rate + \
                                  rental_days * insurance_rate
        else:
            base_rental_charges = rental_days * rental_rate + \
                                  rental_days * insurance_rate
            
        miles_charged = miles_driving - num_free_miles
        
        if miles_charged < 0:
            miles_charged = 0
        
        estimated_mileage_charges = miles_charged * per_mile_charge

        return {'base_charges' : base_rental_charges,
                'insur_rate' : insurance_rate,
                'num_free_miles' : num_free_miles,
                'per_mile_charge' : per_mile_charge,
                'estimated_mileage_charges' : estimated_mileage_charges}





