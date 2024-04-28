'''l = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":kumar,3:6,7:8},["ineuron","data science"]]

1. try to extract all the list entity
2. try to extract all the dict entiry
3. try to extract all the tuples entity
4. try to extract all the numerical data it may by part of dit key and values
5. try to give summation of all the numerical data
6. try to filter out all the odd values out of all the numerical data which is a part of list
7. try to extract ineuron out of this data
8. try to find out number of occurances of all the data
9. try to find out number of keys in dict element
10. try to filter out all the strings data
11. try to find out alphanumeric data  ## k1 ,k2,k3
12. try to find out multiplication of all the individual collection inside dataset
13. try to unwrap all the collections inside collection and create a flat list'''




import logging
logging.basicConfig(filename="list_tuple_task.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class list_tuple_task:
    def __init__(self,my_list1):
        self.mylist1 = my_list1
        logging.info("we are trying to make a list constructor")

    def all_list(self):
        try:
            logging.info("we are trying to extract all the list entities")
            l1 = []
            for i in self.mylist1:
                if type(i)==list:
                    l1.append(i)
                    logging.info(l1)
        except Exception as e:
            logging.exception(e)

    def all_tuple(self):
        try:
            logging.info("we are trying to extract all the tuple entities")
            l2 = []
            for i in self.mylist1:
                if type(i)==tuple:
                    l2.append(i)
                    logging.info(l2)
        except Exception as e:
            logging.exception(e)

    def all_dict(self):
        try:
            logging.info("we are trying to extract all the dictionary entities")
            l3 = []
            for i in self.mylist1:
                if type(i)==dict:
                    l3.append(i)
                    logging.info(l3)
        except Exception as e:
            logging.exception(e)


    def all_numeric(self):
        l4 = []
        try:
            logging.info("we are trying to extract all the numeric data")
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l4.append(j)

                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int or type(m) == int:
                            l4.append(k)
                            l4.append(m)
            logging.info(l4)
        except  Exception as e:
            logging.exception(e)

    def all_numeri_sum(self):
        l5 = []
        try:
            logging.info("we are trying to extract all the numeric data")
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l5.append(j)

                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int or type(m) == int:
                            l5.append(k)
                            l5.append(m)
            l6 = sum(l5)
            logging.info(l6)
        except  Exception as e:
            logging.exception(e)


    def all_oddnumeric_sum(self):
        l7 = []
        l8 = []
        try:
            logging.info("we are trying to extract all the odd numeric data")
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l7.append(j)

                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int or type(m) == int:
                            l7.append(k)
                            l7.append(m)

            for n in l7:
                if n % 2 != 0:
                    l8.append(n)
            l9 = sum(l8)
            logging.info(l9)
        except  Exception as e:
            logging.exception(e)

    def extract_ineuron(self):
        try:
            logging.info("we are trying to extract all the odd numeric data")
            l10 = []
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if j == 'ineuron':
                            l10.append(j)

                if type(i) == dict:
                    for k, v in i.items():
                        if v == 'ineuron':
                            l10.append(v)

            logging.info(l10)
        except  Exception as e:
            logging.exception(e)


    def all_data_occur(self):
        l11 = []
        try:
            logging.info("we are trying to extract all the data and its occurance")
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l11.append(j)

                if type(i) == dict:
                    for k, v in i.items():
                        l11.append(k)
                        l11.append(v)

            for c in set(l11):
                logging.info(f'{c} : {l11.count(c)}')

        except Exception as e:
            logging.exception(e)

    def all_string(self):
        l12 = []
        try:
            logging.info("we are trying to extract all the string data")
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == str:
                            l12.append(j)

                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == str or type(m) == str:
                            l12.append(k)
                            l12.append(m)

            logging.info(l12)
        except Exception as e:
            logging.exception(e)

    def key(self):
        l13=[]
        try:
            logging.info("we are trying to extract all the keys from dictionary")
            for i in self.mylist1:
                if type(i) == dict:
                    for j in i.keys():
                        l13.append(j)
            logging.info(l13)
        except Exception as e:
            logging.exception(e)

    def alnum(self):
        l14 = []
        try:
            logging.info("We are filtering out all the alphanumeric data")
            l14 = []
            for i in self.mylist1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == str:
                            if j.isalnum():
                                l14.append(j)
            logging.info(l14)
        except Exception as e:
            logging.exception(e)

    def all_num_prod(self):
        l15 = []
        try:
            logging.info("We are filtering out all the alphanumeric data and giving out product of it")
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            l15.append(j)

                if type(i) == dict:
                    for k, m in i.items():
                        if type(k) == int or type(m) == int:
                            l15.append(k)
                            l15.append(m)

            logging.info(l15)
            a = 1
            for i in l15:
                a = a * i
            logging.info(a)
        except Exception as e:
            logging.exception(e)

    def new_list(self):
        newlist=[]
        try:
            logging.info("We are trying to filter out all data and creating a new list")
            for i in self.mylist1:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        newlist.append(j)

                if type(i) == dict:
                    for k, v in i.items():
                        newlist.append(k)
                        newlist.append(v)
            logging.info(newlist)
        except Exception as e:
            logging.exception(e)


my_list1 = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),set([23,4,5,4,4,5,45,45,4,5]),{"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},["ineuron","data science"]]
l = list_tuple_task(my_list1)
l.all_list()
l.all_tuple()
l.all_dict()
l.all_numeric()
l.all_numeri_sum()
l.all_oddnumeric_sum()
l.extract_ineuron()
l.all_data_occur()
l.all_string()
l.key()
l.alnum()
l.all_num_prod()
l.new_list()