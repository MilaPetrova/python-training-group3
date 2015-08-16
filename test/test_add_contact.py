# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Alisa", lastname="Petrova", email="alisa.petrova@gmail.com", nickname="Lesi", title="QA", company="Roga i kopita", address="10 Happy St., Boston, MA", home="978-111-1111"))
    app.session.logout()

