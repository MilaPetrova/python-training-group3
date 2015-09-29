__author__ = 'Liudmila'
import random
from model.group import Group
from model.contact import Contact


def test_add_contact_from_homepage_in_group(app, db, check_ui):
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    old_contacts_in_group = db.get_contact_in_group()
    group = random.choice(old_groups)
    contact = random.choice(old_contacts)
    contacts_in_ui_group = app.contact.get_contact_list_in_group(group.name)
    if contact not in contacts_in_ui_group:
        app.contact.select_contact_by_id(contact.id)
        app.contact.replace_in_group(group.name)
    new_contacts_in_group = db.get_contact_in_group()
    old_contacts_in_group.append(contact.id, group.id)
    assert sorted(old_contacts_in_group, key=Group.id_or_max) == sorted(new_contacts_in_group, key=Group.id_or_max)

    if check_ui:
        contacts_in_ui_group = app.contact.get_contact_list_in_group(group.name)
        contacts_in_db_group = []
        for item in new_contacts_in_group:
            if item in contacts_in_ui_group:
                contacts_in_db_group.append(item)
        assert sorted(contacts_in_ui_group, key=Group.id_or_max) == sorted(contacts_in_db_group, key=Group.id_or_max)