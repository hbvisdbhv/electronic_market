import sqlite3

con = sqlite3.connect('products.db')
cursor = con.cursor()


#Таблиця "products":
# cursor.execute('''
# CREATE TABLE products (
#     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     category TEXT NOT NULL,
#     price REAL NOT NULL
# )''')
cursor.execute('''
CREATE TABLE customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE 
)''')
cursor.execute('''
CREATE TABLE orders(
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL, 
    quantity INTEGER NOT NULL,
    order_date DATE NOT NULL, 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)''')
