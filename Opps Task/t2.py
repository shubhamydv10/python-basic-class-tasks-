#multilevel inheritance
class ineuron:                                      #parent class

    def student(self):
        print("the number of enrolled student")

    def courses(self):
        print('all the  available courses')

    def blog(self):
        print("the numbers of blogs posted online")

class jobs(ineuron):         #child class          ////   #parent class for internship class

    def ineuron_job(self):
        print("the number of student got jobs")

class internship(jobs):                          #child class as by multilevel inheritance it inherit from job class
    pass

i = internship()
i.student()
i.courses()
i.blog()
i.ineuron_job()



