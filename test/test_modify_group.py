__author__ = 'Liudmila'

from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="test_name2", header="test_name2", footer="test_footer2"))
    app.session.logout()
