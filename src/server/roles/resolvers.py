from .models import ImputRole, Roles, NewID
from typing import List
import sys
sys.path.append('..')
from server.database.db_manager import base_manager

def get_all_roles():

    res = base_manager.execute("SELECT * FROM roles", many=True)
    roles = []
    for role in res['data']:
        roles.append(Roles(id=role[0], role_name=role[1]))

    return roles


def get_role(role_id: int):
    res = base_manager.execute("SELECT * FROM roles WHERE id = ?", args=(role_id,), many=True)

    roles = []
    for role in res['data']:
        roles.append(Roles(id=role[0], role_name=role[1]))

    return roles


def add_new_role(new_role: ImputRole):
    res = base_manager.execute("INSERT INTO roles(role_name)"
                               "VALUES (?)"
                               "RETURNING id ",
                               args=(new_role.role_name,)
                               , many=True)

    return NewID(code=res['code'], id=res['data'][0][0])


def delete_roles(role_id: int):
    res = base_manager.execute("DELETE FROM roles WHERE id = ?", args=(role_id,))

    return NewID(code=res['code'], id=role_id)
