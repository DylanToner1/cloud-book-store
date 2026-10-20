TRUNCATE TABLE films RESTART IDENTITY;

INSERT INTO films (title, release_date) VALUES('title1', '2026-10-20'),
                                                ('title2', '2026-9-20'),
                                                ('title3', '2026-8-20'),
                                                ('title4', '2026-7-20');