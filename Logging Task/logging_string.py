''' my_str = "this is My First Python programming class and i am learNING python string and its function"
1 . Try to extract data from index one to index 300 with a jump of 3
2. Try to reverse a string without using reverse function
3. Try to split a string after conversion of entire string in uppercase
4. try to convert the whole string into lower case
5 . Try to capitalize the whole string
6 . Write a difference between isalnum() and isalpha()
8 . Give an example of strip , lstrip and rstrip
9.  Replace a string charecter by another charector by taking your own example
"shubham"
10 . Try  to give a defination of string center function with and example '''




import logging
logging.basicConfig(filename="string_task.log",level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

class strings_task:
    def __init__(self,my_str,name1):
        logging.info("we are making a string constructor")
        self.mystring = my_str
        self.name = name1

    def jump(self):
        try:
            logging.info("we are jumping 3 values in a string")
            j = self.mystring[0:300:3]
            logging.info("The string after 3 jump is %s" ,j )
            return j
        except Exception as e:
            logging.exception(e)

    def reverse(self):
        try:
            logging.info("We are trying to reverse the string without using reverse function")
            r = self.mystring[::-1]
            logging.info("The reversed string is %s" ,r)
            return r
        except Exception as e:
            logging.exception(e)

    def split_upper(self):
        try:
            logging.info("we are trying to covert string in uppercase")
            u = self.mystring.upper().split()
            logging.info("we are trying to split the string after converting it into upper")
            logging.info(u)
            return u
        except Exception as e:
            logging.exception(e)

    def lowercase(self):
        try:
            logging.info("We are converting the string into lowercase")
            l = self.mystring.lower()
            logging.info(l)
            return l
        except Exception as e:
            logging.exception(e)

    def cptlz(self):
        try:
            logging.info("We are trying to capitalize string ")
            c = self.mystring.capitalize()
            logging.info(c)
            return c
        except Exception as e:
            logging.exception(e)

    def stp(self):
        try:
            logging.info("We are try to perform strip operation")
            n = self.name.strip()
            logging.info(n)
            return n
        except Exception as e:
            logging.exception(e)

    def lstp(self):
        try:
            logging.info("We are try to perform left strip operation")
            n = self.name.lstrip()
            logging.info(n)
            return n
        except Exception as e:
            logging.exception(e)

    def rstp(self):
        try:
            logging.info("We are try to perform right strip operation")
            n = self.name.rstrip()
            logging.info(n)
            return n
        except Exception as e:
            logging.exception(e)

    def replace_char(self):
        try:
            logging.info("We are doing replacement inside string")
            re = self.name.replace("u","z")
            logging.info("the u in shubham is replaced by z")
            logging.info(re)
            return re
        except Exception as e:
            logging.exception(e)

    def cntr(self):
        try:
            logging.info("Trying tu use center function in string")
            c = self.name.center(100 , 'Q')
            logging.info(c)
            return c
        except Exception as e:
            logging.exception(e)




my_str = "this is My First Python programming class and i am learNING python string and its function"
name1 = "           shubham             "
s = strings_task(my_str,name1)
s.jump()
s.reverse()
s.split_upper()
s.lowercase()
s.cptlz()
s.stp()
s.lstp()
s.rstp()
s.replace_char()
s.cntr()
