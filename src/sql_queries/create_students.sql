CREATE TABLE IF NOT EXISTS public.students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    subject VARCHAR(50) NOT NULL,
    marks INT NOT NULL
);