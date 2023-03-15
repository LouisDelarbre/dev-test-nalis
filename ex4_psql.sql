

CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  price DECIMAL,
  creation_date DATETIME
);

CREATE TABLE categories (
  id INTEGER PRIMARY KEY,
  name TEXT,
  flag_private BOOLEAN
);

CREATE TABLE product_categories (
  product_id INTEGER,
  category_id INTEGER,
  FOREIGN KEY (product_id) REFERENCES products (id),
  FOREIGN KEY (category_id) REFERENCES categories (id)
);

SELECT prod.name AS product_name, COUNT(*) AS category_count
FROM products AS prod
JOIN product_categories AS pc ON prod.id = pc.product_id
JOIN categories AS c ON c.id = pc.category_id
WHERE c.flag_private = FALSE
GROUP BY prod.id
HAVING COUNT(*) > 5;