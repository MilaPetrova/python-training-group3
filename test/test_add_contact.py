# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols)for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="",
                    homephone="", mobilephone="", workphone="", secondaryphone="",
                    email1="",email2="", email3="")] + \
           [Contact(firstname=random_string("firstname", 20), lastname=random_string("lastname", 20), address=random_string("address", 50),
            homephone=random_string("home", 15), mobilephone=random_string("mobile", 15),workphone=random_string("work", 15),
            secondaryphone=random_string("phone2", 15),
            email1=random_string("email", 20) + "@" + "gmail.com", email2=random_string("email2", 20) + "@" + "gmail.com", email3=random_string("email3", 20) + "@" + "gmail.com")
    for i in range(5)]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x)for x in testdata])


def test_add_contact(app, contact):
    pass
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Alisa", lastname="Petrova", nickname="Lesi", company="Roga i kopita", title="QA",address="10 Happy St., Boston, MA",
                      homephone="9781111111", mobilephone="9781112222", workphone="9781113333", secondaryphone="9781114444",
                      email1="alisa.petrova@gmail.com",email2="alisa.petrova@mail.ru", email3="alisa.petrova@yandex.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


