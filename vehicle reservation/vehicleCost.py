"""This module provide a VehicleCost class."""

class VehicleCost:
    """This class provides the methods for maintaining rental costs."""   
    
    def __init__(self, daily_rate, weekly_rate, weekend_rate,
                 free_miles, per_mile_chrg, insur_rate):
        """Initialzes rental rates, num free miles /mileage chrg/insur rate."""

        self.__daily_rate = daily_rate
        self.__weekly_rate = weekly_rate
        self.__weekend_rate = weekend_rate
        self.__free_miles = free_miles
        self.__per_mile_chrg = per_mile_chrg
        self.__insur_rate = insur_rate


    def getDailyRate(self):
        """Returns daily rental rate of vehicle."""
        
        return float(self.__daily_rate)


    def getWeeklyRate(self):
        """Returns weekly rental rate of vehicle."""
        
        return float(self.__weekly_rate)

    
    def getWeekendRate(self):
        """Returns weekend rental rate of vehicle."""
        
        return float(self.__weekend_rate)


    def getFreeMiles(self):
        """Returns number of free miles for vehicle rental."""
        
        return int(self.__free_miles)


    def getPerMileCharge(self):
        """Returns per mile charge for vehicle rental."""
        
        return float(self.__per_mile_chrg)


    def getInsuranceRate(self):
        """Returns daily insurance rate for vehicle."""
        
        return float(self.__insur_rate)

    def getCosts(self):
        """Returns a list containing all costs for vehicle."""

        return [self.__daily_rate, self.__weekly_rate,
                self.__weekend_rate, self.__free_miles,
                self.__per_mile_chrg, self.__insur_rate]

