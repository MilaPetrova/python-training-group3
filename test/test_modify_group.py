__author__ = 'Liudmila'

from model.group import Group
import random

def test_modify_group_name(app, db, json_group_for_modify, check_ui):
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
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

