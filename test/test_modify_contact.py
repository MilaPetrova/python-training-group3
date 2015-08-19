__author__ = 'Liudmila'

from model.contact import Contact

def test_modify_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="Mila"))
    app.session.logout()

def test_modify_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(lastname="Petrova"))
    app.session.logout()

def test_modify_contact_email(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(email="mila.petrova@gmail.com"))
    app.session.logout()


def test_modify_contact_nickname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(nickname="anonym"))
    app.session.logout()


def test_modify_contact_title(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(title="QA"))
    app.session.logout()

def test_modify_contact_company(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(company="Secret"))
    app.session.logout()

def test_modify_contact_address(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(address="10 Happy St."))
    app.session.logout()

def test_modify_contact_home(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(home="978-111-1111"))
    app.session.logout()