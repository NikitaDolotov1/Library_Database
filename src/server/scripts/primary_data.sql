INSERT INTO roles(id, role_name)
VALUES(1, 'Admin'), (2, 'Librarian');

INSERT INTO users(id, login, password, role_id)
VALUES(1,'adm',123,1), (2,'ivan',123,1);

INSERT INTO authors(id, FIO)
VALUES(1, 'Puschkin'), (2, 'Tolstoy');

INSERT INTO genres(id, name_genre)
VALUES(1, 'Roman'), (2, 'Drama');

INSERT INTO books(id, author, name_book, year_pub, genre, author_id, genre_id)
VALUES(1, 'Puschkin', 'Book1', 1869, 'Roman', 1, 1), (2, 'Tolstoy', 'Book2', 1888, 'Drama', 2, 2 );

INSERT INTO books_out(id, id_book, date_out, date_in)
VALUES(1, 1, '11.11.2023', '06.01.2024'), (2,2, '11.11.2023', '06.01.2024');

INSERT INTO profile(id, name)
VALUES(1, 'Ivan'), (2, 'Alex');

INSERT INTO Deleted_profile(id, profile_id, date_deleted, details)
VALUES(1, 1, '11.11.2023', 'Spam'), (2, 2, '11.11.2023', 'Spam');

INSERT INTO coments(id, profile_id, date, coment)
VALUES(1,1, '11.11.2023', 'Good books'), (2,2, '11.11.2023', 'Good books');

INSERT INTO Deleted_coments(id, coment_id, date_deleted, details)
VALUES(1, 1, '11.11.2023', 'Spam'), (2, 2, '11.11.2023', 'Spam');
