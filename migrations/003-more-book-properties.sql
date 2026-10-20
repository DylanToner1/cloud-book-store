ALTER TABLE books
    ADD synopsis TEXT,
    ADD rating NUMERIC(2,1) CONSTRAINT books_rating_check CHECK(rating BETWEEN 0 AND 5),
    ADD notes TEXT;