class Student:
    def __init__(self):
        self.__student_id = None
        self.__marks = None
        self.__age = None
        self.__course_id = None
        self.__fees = None

    def set_student_id(self,id):
        self.__student_id = id
    def get_student_id(self):
        return self.__student_id

    def set_marks(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks

    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return self.__age

    def set_course_id(self,course_id):
        self.__course_id = course_id
    def get_course_id(self):
        return self.__course_id

    def set_fees(self,fees):
        self.__fees = fees
    def get_fees(self):
        return self.__fees

    def validate_marks(self):
        if 0 <= self.get_marks() <= 100:
            return True
        else:
            return False

    def validate_age(self):
        if self.get_age() > 20:
            return True
        else:
            return False


    def check_qualification(self):
        if self.validate_age():
            if self.validate_marks():
                if self.get_marks() >= 65:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def choose_course(self, course_id):
        if self.check_qualification():
            if course_id == 1001:
                if self.get_marks() > 85:
                    self.set_fees( 25575.0 - ( 25575.0 * 25 )/100 )
                    return True
                return True
            elif course_id == 1002:
                if self.get_marks() > 85:
                    self.set_fees( 15500.0 - ( 15500.0 * 25 )/100 )
                    return True
                return True
            else:
                return False
        else:
            return False

s1 = Student()
s1.set_student_id(1004)
s1.set_age(21)
s1.set_marks(100)
print(s1.check_qualification())
print(s1.choose_course(1001))