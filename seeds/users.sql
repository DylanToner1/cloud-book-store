TRUNCATE TABLE users RESTART IDENTITY;

-- passwords: test, test2
INSERT INTO users (username, password) VALUES('test', '$2b$12$AvvLEFFUG/00XzBB6Xz54Onm9cTnqJQ7TIf5Xm4JqDErb7TaAyXJi'),
                                            ('test2', '$2b$12$z4ddsyuIeQpdlHZ3fjAkM.GmR8oHF6GI77YbfQJdI4g7gjX9jVGIC');