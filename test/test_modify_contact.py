__author__ = 'Liudmila'

from model.contact import Contact

def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="Mila"))

def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    app.contact.modify_first_contact(Contact(lastname="Petrova"))

def test_modify_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="email"))
    app.contact.modify_first_contact(Contact(email="mila.petrova@gmail.com"))

def test_modify_contact_nickname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(nickname="test"))
    app.contact.modify_first_contact(Contact(nickname="anonym"))

def test_modify_contact_title(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(title="test"))
    app.contact.modify_first_contact(Contact(title="QA"))

def test_modify_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(company="test"))
    app.contact.modify_first_contact(Contact(company="Secret"))

def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="test"))
    app.contact.modify_first_contact(Contact(address="10 Happy St."))

def test_modify_contact_home(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(home="test"))
    app.contact.modify_first_contact(Contact(home="978-111-1111"))
