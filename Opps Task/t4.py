#Method overriding

class ineuron:

    def courses(self):
        print("this will return all the course available ")

    def student(self):
        print("this will inform the number of student enrolled in the course")

    def blogs(self):
        print("this will inform about the blogs posted about ineuron")


class jobs(ineuron):

    def student(self):                    #Method overriding by using same function name

        print("THIS WILL RETURN THE NUMBER OF STUDENT GOT THE JOBS")

i = jobs()
i.student()