__author__ = 'Liudmila'

from model.group import Group
import random

def test_modify_group_name(app, db, json_group_for_modify):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    new_data = json_group_for_modify
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, new_data)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups = new_groups
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(header="test"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="new_header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)

#def test_modify_group_footer(app):
    #if app.group.count() == 0:
        #app.group.create(Group(footer="test"))
    #old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(footer="new_footer"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
