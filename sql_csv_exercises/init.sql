CREATE TABLE products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    price INTEGER NOT NULL
);

INSERT INTO products (product_id, product_name, price) VALUES
('P001', 'Laptop', 4000),
('P002', 'Monitor', 1200),
('P003', 'Klawiatura', 300);
