CREATE TABLE IF NOT EXISTS shop_data (
    id SERIAL PRIMARY KEY,
    shop_id INTEGER NOT NULL,
    shop_name VARCHAR(255) NOT NULL,
    shop_address VARCHAR(255) NOT NULL,
    shop_phone VARCHAR(255) NOT NULL,
    shop_email VARCHAR(255) NOT NULL
);
