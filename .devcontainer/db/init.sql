\connect postgres

CREATE DATABASE data_pipeline;

CREATE TABLE IF NOT EXISTS data_pipeline.public.users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

INSERT INTO data_pipeline.public.users (name, email) VALUES ('John Doe', 'john@email.com');