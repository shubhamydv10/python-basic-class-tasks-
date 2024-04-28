""" questions
 l = [3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
 1 . Try to reverse a list
 2. try to access 234 out of this list
 3 . try to access 456
 4 . Try to extract only a list collection form list l
 5 . Try to extract "sudh"
 6 . Try to list all the key in dict element available in list
 7 . Try to extract all the value element form dict available in list """

import logging
logging.basicConfig(filename="list_task.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class list_task:
    def __init__(self,my_list):
        self.mylist = my_list
        logging.info("We are creating a list constructor")

    def rev(self):
      try:
          logging.info("we are trying to reverse list")
          l1 = self.mylist[::-1]
          logging.info("the reversed list is : ")
          logging.info(l1)
          return l1
      except Exception as e:
          logging.exception(e)

    def access234(self):
        try:
            logging.info("we will access 234 from lists")
            l2 = self.mylist[7][0]
            logging.info(l2)
            return l2
        except Exception as e:
            logging.exception(e)

    def onlylist(self):
        try:
            logging.info("we are trying to extract on list from l")
            l3=[]
            for i in self.mylist:
                if type(i)==list:
                    l3.append(i)
                    logging.info(l3)

        except Exception as e:
            logging.exception(e)


    def extract_sudh(self):
        try:
            logging.info("we are trying to extract 'sudh' from'' l")
            l4=[]
            for i in self.mylist:
                if type(i)==dict:
                    for k,v in i.items():
                        if k == "sudh" or v == "sudh":
                           l4.append(v)
                           logging.info(l4)

        except Exception as e:
            logging.exception(e)

    def only_keys(self):
        try:
            logging.info("we are trying to extract only keys from l")
            l5=[]
            for i in self.mylist:
                if type(i)==dict:
                    for j in i.keys():
                        l5.append(j)
                        logging.info(l5)

        except Exception as e:
            logging.exception(e)

    def only_val(self):
        try:
            logging.info("we are trying to extract only val from l")
            l6=[]
            for i in self.mylist:
                if type(i)==dict:
                    for j in i.values():
                        l6.append(j)
                        logging.info(l6)

        except Exception as e:
            logging.exception(e)


logging.shutdown()


my_list =[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
l = list_task(my_list)
l.rev()
l.access234()
l.onlylist()
l.extract_sudh()
l.only_keys()
l.only_val()