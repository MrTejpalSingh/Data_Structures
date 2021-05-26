#lex_auth_0127426245709905921377

class Car:
    def __init__(self,model,year,registration_number):
        self.__model=model
        self.__year=year
        self.__registration_number=registration_number

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_registration_number(self):
        return self.__registration_number

    def __str__(self):
        return(self.__model+" "+self.__registration_number+" "+(str)(self.__year))

class Service:
    def __init__(self,car_list):
        self.__car_list = car_list

    def find_cars_by_year(self,year):
        lst_of_models = []
        for i in car_list:
            if i.get_year() == year:
                lst_of_models.append(i.get_model())
        return lst_of_models

    def add_cars(self,new_car_list):
        asc_years = []
        for i in new_car_list:
            asc_years.append(i.get_year())
        asc_years.sort()
        print(asc_years)
        for i in range(len(asc_years)):
            for j in new_car_list:
                if asc_years[i] == j.get_year():
                    car_list.append(new_car_list[i])
        for i in car_list:
            print("Car: ",i.get_model(),", year: ",i.get_year())

    def remove_cars_from_karnataka(self):
        i = 0
        while i <= len(car_list) - 1:
            rn = car_list[i].get_registration_number()
            if "KA" == rn[:2]:
                car_list.remove(car_list[i])
            else:
                i += 1
        return car_list

#Implement Service class here

car1=Car("WagonR",2010,"KA09 3056")
car2=Car("Beat", 2011, "MH10 6776")
car3=Car("Ritz", 2013,"KA12 9098")
car4=Car("Polo",2013,"GJ01 7854")
car5=Car("Amaze",2014,"KL07 4332")
#Add different values to the list and test the program
car_list=[car1, car2, car3, car4,car5]
#new car list
car6=Car("A",2015,"KA09 3056")
car7=Car("B", 2018, "MH10 6776")
car8=Car("C", 2011,"KA12 9098")
new_car_list=[car6, car7, car8]
#Create object of Service class, invoke the methods and test your
s = Service(car_list)
print(s.find_cars_by_year(2013))
s.add_cars(new_car_list)
# print(s.remove_cars_from_karnataka())