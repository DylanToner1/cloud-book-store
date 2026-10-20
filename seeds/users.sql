TRUNCATE TABLE users;

ALTER SEQUENCE users_id_seq RESTART WITH 1;

-- passwords: test, test2
INSERT INTO users (username, password) VALUES('test', '$2b$12$AvvLEFFUG/00XzBB6Xz54Onm9cTnqJQ7TIf5Xm4JqDErb7TaAyXJi');
INSERT INTO users (username, password) VALUES('test2', '$2b$12$z4ddsyuIeQpdlHZ3fjAkM.GmR8oHF6GI77YbfQJdI4g7gjX9jVGIC');