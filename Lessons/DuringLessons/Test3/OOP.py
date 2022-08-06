class Animal:
    def __init__(self,weight,height,age):
        self.weight = weight
        self.height = height
        self.age = age
    def walk(self,distance):
        self.weight-=distance*0.00034
    
class Dog(Animal):
    def __init__(self, weight, height, age, type):
        super().__init__(weight, height, age)
        self.type = type
    
    def run(self,distance):
        self.weight-=distance-0.005
        
class CarShop:
    ## cars = {
    ##  "Toyota Camry 2016":{"count":15, "price":6000}  
    ## }
    def __init__(self,name,area,cars:dict,location,totalIncome,totalOutcome) -> None:
        self.name = name
        self.area = area
        self.cars = cars
        self.location = location
        self.totalIncome = totalIncome
        self.totalOutcome = totalOutcome
        
    def sellCar(self,cartype):
        self.cars[cartype]["count"]-=1
        self.totalIncome-=self.cars[cartype]["price"]
    
    def getCar(self,car:dict):
        if car.keys()[0] in self.cars:
            self.cars[car.keys(0)]["count"]+=car[car.keys(0)]["count"]
        else:
            self.cars[car.keys(0)] = {}
            self.cars[car.keys(0)]["count"]+=car[car.keys(0)]["count"] 
            
        self.totalOutcome+=car[car.keys(0)]["price"]*car[car.keys(0)]["count"]
        