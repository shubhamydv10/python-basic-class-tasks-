#multiple inheritance
class ineuron:                                      #parent class

    def student(self):
        print("the number of enrolled student")

    def courses(self):
        print('all the  available courses')

    def blog(self):
        print("the numbers of blogs posted online")

class jobs(ineuron):

    def ineuron_job(self):
        print("the number of student got jobs")

class internship:
    def internship_ineuron(self):
        print("The students who all got internship by ineuron")

class achivers(jobs ,ineuron, internship):                 #multilevel inheritance
    pass

a = achivers()

a.student()
a.ineuron_job()
a.internship_ineuron()
a.courses()
a.blog()

