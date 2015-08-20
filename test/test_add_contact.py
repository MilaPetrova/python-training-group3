# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Alisa", lastname="Petrova", email="alisa.petrova@gmail.com", nickname="Lesi", title="QA", company="Roga i kopita", address="10 Happy St., Boston, MA", home="978-111-1111"))


