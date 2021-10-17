class Car:
    def __init__(self,model,color,speed,company):
        self.model = "Black"
        self.color = "Blue"
        self.speed = 160
        self.company = "Company"
    def start():
        print("Started")
    def stop():
        print("Stopped")
    def accelerate():
        print("Accelerating")
    def changegear():
        print("Gear Changed")
audi = Car("Black", "Blue", 160, "Company")
print(audi.color)
Car.start()
Car.stop()
Car.accelerate()
Car.changegear()