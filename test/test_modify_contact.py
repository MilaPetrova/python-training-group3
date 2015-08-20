__author__ = 'Liudmila'

from model.contact import Contact

def test_modify_contact_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="Mila"))

def test_modify_contact_lastname(app):
    app.contact.modify_first_contact(Contact(lastname="Petrova"))

def test_modify_contact_email(app):
    app.contact.modify_first_contact(Contact(email="mila.petrova@gmail.com"))

def test_modify_contact_nickname(app):
    app.contact.modify_first_contact(Contact(nickname="anonym"))

def test_modify_contact_title(app):
    app.contact.modify_first_contact(Contact(title="QA"))

def test_modify_contact_company(app):
    app.contact.modify_first_contact(Contact(company="Secret"))

def test_modify_contact_address(app):
    app.contact.modify_first_contact(Contact(address="10 Happy St."))

def test_modify_contact_home(app):
    app.contact.modify_first_contact(Contact(home="978-111-1111"))
