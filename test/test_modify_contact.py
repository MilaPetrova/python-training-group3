__author__ = 'Liudmila'

from model.contact import Contact

def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify(Contact(firstname="Mila", lastname="Petrova", email="mila.petrova@gmail.com", nickname="anonym", title="QA", company="Secret", address="10 Happy St., Boston, MA", home="978-111-1111"))
    app.session.logout()
