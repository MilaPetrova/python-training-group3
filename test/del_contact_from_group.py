__author__ = 'Liudmila'

import random
from model.group import Group
from model.contact import Contact

def test_delete_contact_from_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_groups = db.get_group_list()
    old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    contacts_in_ui_group = app.contact.get_contact_list_in_group(group.name)
    selected_contact = random.choice(contacts_in_ui_group)
    app.contact.delete_contact_by_id(selected_contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(selected_contact)
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(new_contacts, key=Group.id_or_max)

    if check_ui:
        new_contacts_in_ui_group = app.contact.get_contact_list_in_group(group.name)
        contacts_in_db_group = []
        for item in new_contacts:
            if item in contacts_in_ui_group:
                contacts_in_db_group.append(item)
        assert sorted(new_contacts_in_ui_group, key=Group.id_or_max) == sorted(contacts_in_db_group, key=Group.id_or_max)
