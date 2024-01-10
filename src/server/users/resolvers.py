from .models import ImputUser, UserInfo, NewID
from typing import List
import sys

sys.path.append('..')
from server.database.db_manager import base_manager


def check_user(Login: ImputUser) -> UserInfo:
    res = base_manager.execute("SELECT id, role_id "
                               "FROM users "
                               "WHERE login= ? AND password = ?", args=(Login.login.lower(), Login.password),
                               many=False)
    print(res)
    if res['data']:
        return UserInfo(id=res['data'][0], role_id=res['data'][1])
    else:
        return UserInfo(id=0, role_id=0)


def get_all_users():
    res = base_manager.execute("SELECT id, login, role_id FROM users", many=True)
    usr = []
    for user in res['data']:
        usr.append(UserInfo(id=user[0], login=user[1], role_id=user[2]))

    return usr


def get_user(user_id: int):
    res = base_manager.execute("SELECT id, login, role_id FROM users WHERE id = ?", args=(user_id,), many=True)

    usr = []
    for user in res['data']:
        usr.append(UserInfo(id=user[0], login=user[1], role_id=user[2]))
    return usr


def add_new_user(new_user: ImputUser):
    res = base_manager.execute("INSERT INTO users(login, password, role_id)"
                               "VALUES (?, ?, ?)"
                               "RETURNING id ",
                               args=(new_user.login, new_user.password, new_user.role_id,)
                               , many=True)

    return NewID(code=res['code'], id=res['data'][0][0])


def delete_user(user_id: int):
    res = base_manager.execute("DELETE FROM users WHERE id = ?", args=(user_id,))

    return NewID(code=res['code'], id=user_id)


def update_user(user_id: int, new_user_name: ImputUser):
    res = base_manager.execute("UPDATE users SET login = ?, password = ?, role_id = ?"
                               " WHERE id = ?",
                               args=(new_user_name.login, new_user_name.password, new_user_name.role_id, user_id,))

    return NewID(code=res['code'], id=user_id)

