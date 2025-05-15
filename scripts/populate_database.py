import sqlite3
import random
from datetime import datetime, timedelta
from pathlib import Path

# Path to the SQLite database file
db_path = Path(__file__).resolve().parent.parent / 'data' / 'store.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Base data for simulation
countries = ["USA", "Germany", "Spain", "France", "Italy", "UK"]
product_names = [
    "Laptop", "Smartphone", "Headphones", "Monitor", "Keyboard",
    "Mouse", "Webcam", "Microphone", "Tablet", "Charger",
    "USB Drive", "Hard Drive", "Graphics Card", "Power Supply",
    "RAM", "Motherboard", "Cooling Fan", "Speaker", "Router", "Projector"
]
categories = ["Electronics", "Accessories", "Peripherals", "Networking"]

# Insert customers
for i in range(1, 101):  # 100 customers
    name = f"Customer {i}"
    country = random.choice(countries)
    age = random.randint(18, 70)
    cursor.execute("INSERT INTO customers (id, name, country, age) VALUES (?, ?, ?, ?)",
                   (i, name, country, age))

# Insert products
for i, name in enumerate(product_names, start=1):
    category = random.choice(categories)
    cursor.execute("INSERT INTO products (id, name, category) VALUES (?, ?, ?)",
                   (i, name, category))

# Insert orders and order items
order_id = 1
item_id = 1
for customer_id in range(1, 101):  # Each customer places between 1 and 5 orders
    for _ in range(random.randint(1, 5)):
        order_date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))
        order_total = 0.0
        cursor.execute("INSERT INTO orders (id, customer_id, order_date, total) VALUES (?, ?, ?, ?)",
                       (order_id, customer_id, order_date.strftime('%Y-%m-%d'), 0.0))

        # Each order contains 1 to 4 products
        for _ in range(random.randint(1, 4)):
            product_id = random.randint(1, len(product_names))
            quantity = random.randint(1, 5)
            price = round(random.uniform(10, 300), 2)
            subtotal = quantity * price
            order_total += subtotal
            cursor.execute(
                "INSERT INTO order_items (id, order_id, product_id, quantity, price) VALUES (?, ?, ?, ?, ?)",
                (item_id, order_id, product_id, quantity, price))
            item_id += 1

        # Update order total
        cursor.execute("UPDATE orders SET total = ? WHERE id = ?", (round(order_total, 2), order_id))
        order_id += 1

# Commit changes and close connection
conn.commit()
conn.close()

print("Database populated with fake data at:", db_path)
