__author__ = 'Liudmila'

from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Mila")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_contact_lastname(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(lastname="test"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(lastname="Petrova"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_email(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="email"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(email="mila.petrova@gmail.com"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

#def test_modify_contact_nickname(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(nickname="test"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(nickname="anonym"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

#def test_modify_contact_title(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(title="test"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(title="QA"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)


#def test_modify_contact_company(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(company="test"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(company="Secret"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

#def test_modify_contact_address(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(address="test"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(address="10 Happy St."))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

#def test_modify_contact_home(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(home="test"))
    #old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(home="978-111-1111"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
