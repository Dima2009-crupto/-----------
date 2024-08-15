class car:
    type = "car"

    def _init_(self, drivin_forward: float):
        print("Call_init_method")
        self.drivin_forward = drivin_forward

    def drivin_forward(self):
        print(f"{self.type}: я їду вперед...")
        self.drivin_forward += 50.0

    def drivin_backwards(self):
        print(f"{self.type}: я їду назад...")
        self.drivin_backwards -= 25.0


class Truck(car):
    typ = "truck"

    def  drivin_forward(self):
        print(f"{self.type}: я їду вперед...")
        self.drivin_forward += 40.0

    def drivin_backwards(self):
        print(f"{self.type}: я їду назад...")
        self.drivin_backwards -= 20.0

    def air_conditioner(self):
        print(f"{self.type}: я дую прохолодний вітер")
        self.air_conditioner += 5.0


class Passengercar(car):
    type = "passenger_car"

    def color(self):
        print(f"{self.type} color: green")


class door:
    def open(self):
        print("Двері відчинені...")
        
    def closed(self):
        print("Двері зачинені")
        
        
truck = Truck()
passengercar = Passengercar()