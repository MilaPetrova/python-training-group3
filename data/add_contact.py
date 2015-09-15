__author__ = 'Liudmila'

from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1",
            homephone="homephone1", mobilephone="mobilephone1", workphone=" workphone1", secondaryphone="secondaryphone1",
            email1="email1",email2="email2", email3="email3"),
    Contact(firstname="firstname2", lastname="lastname2",
            homephone="homephone2", mobilephone="mobilephone2", workphone=" workphone2", secondaryphone="secondaryphone2",
            email1="email11",email2="email12", email3="email13")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="",
                    homephone="", mobilephone="", workphone="", secondaryphone="",
                    email1="",email2="", email3="")] + \
           [Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20), address=random_string("address", 50),
            homephone=random_string("home", 15), mobilephone=random_string("mobile", 15),workphone=random_string("work", 15),
            secondaryphone=random_string("phone2", 15),
            email1=random_string("email", 20) + "@" + "gmail.com", email2=random_string("email2", 20) + "@" + "gmail.com", email3=random_string("email3", 20) + "@" + "gmail.com")
    for i in range(2)]