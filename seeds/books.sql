TRUNCATE TABLE books;

ALTER SEQUENCE books_id_seq RESTART WITH 1;


INSERT INTO books (title, author, synopsis, rating, notes) VALUES('The Gruffalo', 'Julia Donaldson', NULL, 2.3, NULL);
INSERT INTO books (title, author, synopsis, rating, notes) VALUES('Ada Twist, Scientist', 'Andrea Beaty',  NULL, 2.3, NULL);
INSERT INTO books (title, author, synopsis, rating, notes) VALUES('The Girl Who Drank the Moon', 'Kelly Barnhill',  NULL, 2.3, NULL);
INSERT INTO books (title, author, synopsis, rating, notes) VALUES('Dragons in a Bag', 'Zetta Elliott',  NULL, 2.3, NULL);

