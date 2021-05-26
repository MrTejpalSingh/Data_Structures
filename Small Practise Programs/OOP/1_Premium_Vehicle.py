class Vehicle:
    def __init__(self):
        pass

    def set_vehicle_type(self,type):
        self.__vehicle_type = type
    def set_vehicle_premium_amount(self,amount):
        self.__vehicle_premium_amount = amount
    def set_vehicle_id(self,id):
        self.__vehicle_id = id
    def set_vehicle_cost(self,cost):
        self.__vehicle_cost = cost


    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def get_vehicle_premium_amount(self):
        return self.__vehicle_premium_amount

    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.set_vehicle_premium_amount((self.get_vehicle_cost()*2)/100)
        elif self.__vehicle_cost == "Four Wheeler":
            self.set_vehicle_premium_amount((self.get_vehicle_cost()*6)/100)
    def show_details(self):
        print( 'Vehicle Type:'+ self.get_vehicle_type()+'  ,Vehicle id:'+ str(self.get_vehicle_id())+'  ,Vehicle Cost:'+ str(self.get_vehicle_cost())+'  ,Vehicle Premium Amount:'+ str(self.get_vehicle_premium_amount()) )

v1 = Vehicle()
v1.set_vehicle_cost(50000)
v1.set_vehicle_id(1001)
v1.set_vehicle_type("Two Wheeler")
v1.calculate_premium()
v1.show_details()

v1 = Vehicle()
v1.set_vehicle_cost(80000)
v1.set_vehicle_id(1002)
v1.set_vehicle_type("Four Wheeler")
v1.calculate_premium()
v1.show_details()