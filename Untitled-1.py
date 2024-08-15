class Car:
    type = "car"

    def _init_(self, drivin_forward: int):
        print("Call_init_method")
        self.drivin_forward = drivin_forward

    def drivin_forward(self):
        print(f"{self.type}: я їду вперед...")
        self.drivin_forward += 30

    def drivin_backwards(self):
        print(f"{self.type}: я їду назад...")
        self.drivin_backwards -= 25


class Truck(Car):
    type = "truck"

    def  drivin_forward(self):
        print(f"{self.type}: я їду вперед...")
        self.drivin_forward += 40

    def drivin_backwards(self):
        print(f"{self.type}: я їду назад...")
        self.drivin_backwards -= 20

    def air_conditioner(self):
        print(f"{self.type}: я дую прохолодний вітер")
        self.air_conditioner += 5


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