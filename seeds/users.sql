TRUNCATE TABLE users;

ALTER SEQUENCE users_id_seq RESTART WITH 1;

INSERT INTO users (username, password) VALUES('test', 'test');
INSERT INTO users (username, password) VALUES('test2', 'test2');