TRUNCATE TABLE books;

ALTER SEQUENCE books_id_seq RESTART WITH 1;


INSERT INTO books (title, author) VALUES('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES('Dragons in a Bag', 'Zetta Elliott');

