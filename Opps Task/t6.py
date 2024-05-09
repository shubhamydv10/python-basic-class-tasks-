#polymorphisim =  a different form of different instances by behaving differently for each variable or class

class ineuron:

    def students(self):
        print("the number of available student")

class udemy:
    def students(self):
        print("the enrolled students")

def bridge(a):            #function work as a bridge between two class by which we can call any function from both of class
    a.students()

i = ineuron()
j = udemy()
i.students()
j.students()
bridge(i)
bridge(j)