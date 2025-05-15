import sqlite3
import pandas as pd
from pathlib import Path

# Paths
db_path = Path(__file__).resolve().parent.parent / 'data' / 'store.db'
output_dir = Path(__file__).resolve().parent.parent / 'data'
output_dir.mkdir(exist_ok=True)

# Connect
conn = sqlite3.connect(db_path)

# Orders per country
df = pd.read_sql_query("""
    SELECT c.country, COUNT(o.id) AS num_orders
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    GROUP BY c.country
""", conn)
df.to_csv(output_dir / 'orders_by_country.csv', index=False)

# Revenue per product
df = pd.read_sql_query("""
    SELECT p.name AS product, SUM(oi.quantity * oi.price) AS revenue
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
    GROUP BY p.id
""", conn)
df.to_csv(output_dir / 'revenue_per_product.csv', index=False)

# Monthly sales
df = pd.read_sql_query("""
    SELECT SUBSTR(order_date, 1, 7) AS month, SUM(total) AS revenue
    FROM orders
    GROUP BY month
    ORDER BY month
""", conn)
df.to_csv(output_dir / 'monthly_sales.csv', index=False)

# Top customers
df = pd.read_sql_query("""
    SELECT c.name, c.country, SUM(o.total) AS total_spent
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    GROUP BY c.id
    ORDER BY total_spent DESC
    LIMIT 10
""", conn)
df.to_csv(output_dir / 'top_customers.csv', index=False)

# Average order value per country
df = pd.read_sql_query("""
    SELECT c.country, AVG(o.total) AS avg_order_value
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    GROUP BY c.country
""", conn)
df.to_csv(output_dir / 'avg_order_value_by_country.csv', index=False)

# Most sold products (by quantity)
df = pd.read_sql_query("""
    SELECT p.name AS product, SUM(oi.quantity) AS total_quantity
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
    GROUP BY p.id
    ORDER BY total_quantity DESC
""", conn)
df.to_csv(output_dir / 'most_sold_products.csv', index=False)

# Revenue by category
df = pd.read_sql_query("""
    SELECT p.category, SUM(oi.quantity * oi.price) AS revenue
    FROM order_items oi
    JOIN products p ON oi.product_id = p.id
    GROUP BY p.category
""", conn)
df.to_csv(output_dir / 'revenue_by_category.csv', index=False)

# Daily order count
df = pd.read_sql_query("""
    SELECT order_date, COUNT(*) AS num_orders
    FROM orders
    GROUP BY order_date
    ORDER BY order_date
""", conn)
df.to_csv(output_dir / 'daily_order_count.csv', index=False)

# Customer age distribution
df = pd.read_sql_query("""
    SELECT age, COUNT(*) AS count
    FROM customers
    GROUP BY age
    ORDER BY age
""", conn)
df.to_csv(output_dir / 'customer_age_distribution.csv', index=False)

conn.close()
print("All analysis exported to data/ folder.")
