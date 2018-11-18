class Battery():
    def __init__(self,battery_size = 60):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print ('This battery has'+ " " + str(self.battery_size) + '-kw of battery',end='')
        
    def get_range(self):
        if self.battery_size == 60:
            range = 100
        elif self.battery_size == 85:
            range = 150
        message =  'The car can go approximately'+" " + str(range)
        message += 'Miles on full charge'
        print(message,end='')
        
    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
        else:
            print('Battery is already upgraded',end='')
