CREATE TABLE instruction_record (
    id SERIAL PRIMARY KEY,
    instruction VARCHAR[] NOT NULL UNIQUE,
    result INTEGER
);
