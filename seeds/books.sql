TRUNCATE TABLE books RESTART IDENTITY;

INSERT INTO books (title, author, synopsis, rating, notes) VALUES('The Gruffalo', 'Julia Donaldson', NULL, 2.3, NULL),
                                                                ('Ada Twist, Scientist', 'Andrea Beaty',  NULL, 4.6, NULL),
                                                                ('The Girl Who Drank the Moon', 'Kelly Barnhill',  NULL, 1.2, NULL),
                                                                ('Dragons in a Bag', 'Zetta Elliott',  NULL, 5.0, NULL);

