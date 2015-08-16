__author__ = 'Liudmila'


def delete_first_contact(self):
    app.session.login(username="admin", password="secret")
    app.group.del_first_contact()
    app.session.logout()