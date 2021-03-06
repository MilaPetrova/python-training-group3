__author__ = 'Liudmila'
import re
from model.contact import Contact


def test_all_contacts_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_likes_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_likes_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_info_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page, key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_likes_on_home_page(contact):
     return "\n".join(filter(lambda x: x != "",
                      map(lambda x: clear(x),
                          filter(lambda x: x is not None,
                                 [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_likes_on_home_page(contact):
     return "\n".join(filter(lambda x: x != "",
                      map(lambda x: clear(x),
                          filter(lambda x: x is not None,
                                 [contact.email1, contact.email2, contact.email3]))))