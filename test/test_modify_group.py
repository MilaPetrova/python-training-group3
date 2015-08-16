__author__ = 'Liudmila'

from model.group import Group

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="test_name2",header="test_header2", footer="test_header3"))
    app.session.logout()
