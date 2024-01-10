import requests


class BaseWorker:
    def __init__(self, server_url: str):
        self.server_url = server_url
        self.end_points = {"check_login": self.server_url + "/users/check",
                           "users": self.server_url + "/users",
                           "roles": self.server_url + "/roles/",
                           "books": self.server_url + "/books",
                           "books_out": self.server_url + "/books_out"
                           }

    def check_user_login(self, user: "User") -> "Login":
        resp = requests.get(url=self.end_points.get('check_login'), data=user.to_json())
        print(resp.text)
        return Login(user_id=resp.json()['id'], role_id=resp.json()['role_id'])

    def get_users_list(self):
        resp = requests.get(url=self.end_points.get('users'))
        return [User(user_id=user['id'], login=user['login'], role_id=user['role_id'])
                for user in resp.json()]

    def get_roles_list(self):
        resp = requests.get(url=self.end_points.get('roles'))
        return [Role(role_id=role['id'], role_name=role['role_name']) for role in resp.json()]

    def add_new_user(self, user: "User"):
        resp = requests.post(url=self.end_points.get('users'), data=user.to_json())
        return resp.json()

    def delete_user(self, user_id: int):
        resp = requests.delete(url=self.end_points.get('users') + f'/{user_id}')
        return resp.json()

    def get_books_out_list(self):
        resp = requests.get(url=self.end_points.get('books_out'))
        return [Books_out(id=book['id'], id_book=book['id_book'], date_out=book['date_out'], date_in=book['date_in']) for book in resp.json()]


    def get_booksName(self):
        resp = requests.get(url=self.end_points.get('books'))
        return [BooksName(id=book['id'], author=book['author'], name_book=book['name_book'], year_pub=book['year_pub'], genre=book['genre']) for book in resp.json()]

    def add_new_books_out(self, book_out: "Books_out"):
        resp = requests.post(url=self.end_points.get('books_out'), data=book_out.to_json())
        return resp.json()



class BooksName:
    def __init__(self,id: int, author: str, name_book: str,year_pub:int,genre:str):
        self.id = id
        self.author = author
        self.name_book = name_book
        self.year_pub = year_pub
        self.genre = genre


class Books_out:
    def __init__(self, id_book: int, date_out: str = None, date_in: str = None, id: int = None):
        self.id = id
        self.id_book = id_book
        self.date_out = date_out
        self.date_in = date_in

    def to_json(self):
        return f'{{"id_book": "{self.id_book}", "date_out": "{self.date_out}", "date_in": "{self.date_in}"}}'



class Login:
    def __init__(self, user_id: int, role_id: int):
        self.user_id = user_id
        self.role_id = role_id


class User:
    def __init__(self, login: str, user_id: int = None, role_id: int = 0, password: int = None):
        self.user_id = user_id
        self.login = login
        self.role_id = role_id
        self.password = password

    def to_json(self):
        return f'{{"login": "{self.login}", "password": "{self.password}", "role_id": "{self.role_id}"}}'


class Role:
    def __init__(self, role_id: int, role_name: int):
        self.role_id = role_id
        self.role_name = role_name
