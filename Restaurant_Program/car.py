class Car(object):
    def __init__(self,model,manifacturer,year):
        self.model = model
        self.manifacturer = manifacturer
        self.year = year
        self.odometer = 0
        
    def get_descriptive(self):
         long_desc = self.model + "" + self.manifacturer + "" + str(self.year)
         return long_desc.title()
        
    def read_odometer(self):
         print ('This car has'+ str(self.odometer)+ 'Miles on it.')
         
    def update_odometer(self,milage):
         if milage >= self.odometer:
             self.odometer = milage
         else:
             print('You cannot role back odometer with lesser value')
             
    def increment_odometer(self,miles):
         self.odometer += miles   
