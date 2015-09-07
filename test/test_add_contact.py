# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Alisa", lastname="Petrova",
                      nickname="Lesi", company="Roga i kopita", title="QA",address="10 Happy St., Boston, MA",
                      homephone="9781111111", mobilephone="9781112222", workphone="9781113333", secondaryphone="9781114444",
                      email1="alisa.petrova@gmail.com",email2="alisa.petrova@mail.ru", email3="alisa.petrova@yandex.ru")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
    #old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="", lastname="", email="", nickname="", title="", company="", address="", home="", mobile="", work="", fax="")
    #app.contact.create(contact)
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)
    #old_contacts.append(contact)
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)