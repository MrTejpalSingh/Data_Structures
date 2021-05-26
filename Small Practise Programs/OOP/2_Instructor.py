class Instructor:
    def __init__(self):
        self.__experience = 8
        self.__instructor_name = "Tejpal"
        self.__technology_skill = ['JAVA','C++','Python']
        self.__avg_feedback = 6

    def check_elegibilty(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        else:
            return False

    def allocate_course(self,technology):
        if technology in self.__technology_skill:
            if self.check_elegibilty():
                return True
            else:
                return False
        else:
            return False

In1 = Instructor()
print(In1.allocate_course('JAVA'))

