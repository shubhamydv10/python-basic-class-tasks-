#incaptulation = you are not suppose to allow a user to modify the class of variable in the run time which is protected.

class ineuron:

    def __init__(self):
        self.student1 = "data science"

    def students(self):
        print(self.student1)

i = ineuron()
i.students()
i.student1 = "data analytics"          # assigning the data in run time
i.students()     #data is changed as it is a private variable



class ineuron1:

    def __init__(self):
        self.__student1 = "data science"

    def students(self):
        print(self.__student1)

    def student_change(self):                    #function to change value when the variable is private
        self.__student1 =  "big data by me"

    def change_val(self,new_value):      #function to take input new values from user
        self.__student1 = new_value




i1 = ineuron1()
i1.students()
i1.__student1 = "big data"          #value is not changed as the variable is protected , so we need to add a new function to change value in run time
i1.students()
i1.student_change()           # now by calling the change function  first the value can be changed in the run time
i1.students()
i1.change_val("shubham")        #we can make a function to input value by myself
i1.students()
