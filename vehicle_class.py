class vehicle:
    def __init__(self, brand, model, ftype):
        self.brand = brand
        self.model = model
        self.ftype = ftype
        self.price_fuel_perltr = 100
        self.tank_size = 30
        self.fuel_level = 0

    def fuel_level_vehicle(self):
        if self.fuel_level == self.tank_size :
            return("vehicle tank is full")
        else :
            return(f'The vehicle tank needs to be filled with addition of {self.tank_size - self.fuel_level} litre.')

    def fuel_price(self):
        return(f'Price of fuel for filling the tank of {self.brand} is {self.price_fuel_perltr*(self.tank_size - self.fuel_level)} rupees')


#constructing object
object1_vehicle = vehicle('Hyundai', 'i20', 'Petrol')
object2_vehicle = vehicle('Ford','Endavour', 'Deisel')

#Accessing attribute values
print(object1_vehicle.brand)
print(object1_vehicle.model)
print(object1_vehicle.ftype)

#calling method
print(object1_vehicle.fuel_level_vehicle())
print(object1_vehicle.fuel_price())
object2_vehicle.fuel_level = 10

print(object2_vehicle.fuel_level_vehicle())
print(object2_vehicle.fuel_price())