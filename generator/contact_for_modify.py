__author__ = 'Liudmila'

from model.contact import Contact
import random
import string
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contact_for_modify.json"
for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="",
                    homephone="", mobilephone="", workphone="", secondaryphone="",
                    email1="",email2="", email3="")] + \
           [Contact(firstname=random_string("newfirstname", 20), lastname=random_string("newlastname", 20),
            address=random_string("newaddress", 50),
            homephone=random_string("newhome", 15), mobilephone=random_string("newmobile", 15),workphone=random_string("newwork", 15),
            secondaryphone=random_string("newphone2", 15),
            email1=random_string("newemail", 20) + "@" + "gmail.com", email2=random_string("newemail2", 20) + "@" + "gmail.com",
            email3=random_string("newemail3", 20) + "@" + "gmail.com")
    for i in range(1)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))