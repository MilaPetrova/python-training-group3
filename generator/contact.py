__author__ = 'Liudmila'

from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="",
                    homephone="", mobilephone="", workphone="", secondaryphone="",
                    email1="",email2="", email3="")] + \
           [Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20), address=random_string("address", 50),
            homephone=random_string("home", 15), mobilephone=random_string("mobile", 15),workphone=random_string("work", 15),
            secondaryphone=random_string("phone2", 15),
            email1=random_string("email", 20) + "@" + "gmail.com", email2=random_string("email2", 20) + "@" + "gmail.com", email3=random_string("email3", 20) + "@" + "gmail.com")
    for i in range(4)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))