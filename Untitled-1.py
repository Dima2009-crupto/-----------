class Car:
    type = "car"

    def __init__(self,distance: float):
        print("Call_init_method")
        self.distance = distance,

    def drivin_forward(self):
        print(f"{self.type}: я їду вперед...")
        self.distance +=30    

    def drivin_backwards(self):
        print(f"{self.type}: я їду назад...")
        self.distance -=25


class Truck(Car):
    type = "truck"

    def drivin_forward(self):
        print(f"{self.type}: я їду вперед...")
        self.distance +=40.0

    def drivin_backwards(self):
        print(f"{self.type}: я їду назад...")
        self.distance -=25   
         
    def air_conditioner(self):
        print(f"{self.type}: я дую прохолодний вітер")
        self.temp +=5.0


class Passengercar(Car):
    type = "passenger_car"

    def color(self):
        print(f"{self.type} color: green")
        
    
class Door:
    def open(self):
        print("Двері відчинені...")
        
    def closed(self):
        print("Двері зачинені")
        
        
truck = Truck(40)
passenger_car = Passengercar(40)
        
print(truck.type)
print(passenger_car.type)
print(truck.air_conditioner())
print(truck.drivin_forward())