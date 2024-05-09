#single inheritance

class ineuron:                                         #parent class
    def __init__(self,student , course , blog):
        self.student = student
        self.course = course
        self.blog = blog

    def job(self):
        print("no of student got the job")

i = ineuron('shubham','data science','datas')
print(i.student)
print(i.course)
print(i.blog)

class ineuron1(ineuron):                                #child class inheriting values and function from parent class
    pass

i1 = ineuron1('amit','data analytics' , 'analystics')
print(i1)
print(i1.student)
print(i1.course)
print(i1.blog)
i1.job()