import sqlite3
import pandas as pd
import os

# Pobranie katalogu, w którym znajduje się skrypt
current_dir = os.path.dirname(os.path.abspath(__file__))
# Tworzenie dynamicznej ścieżki do pliku bazy danych
db_path = os.path.join(current_dir, "products.db")

csv_path = os.path.join(current_dir, "orders.csv")

conn = sqlite3.connect(db_path)
products = pd.read_sql("select * from products",con=conn)
orders = pd.read_csv(csv_path)
conn.close()

# print(products)

# print(orders)

df = orders.merge(products,on=["product_id"],how="left")
df["order_price"]= df["quantity"]*df["price"]
# df_product = df.groupby("product_id")["order_price"].sum().reset_index()
# df_client= df.groupby("product_id")["customer_id"].nunique().reset_index(name="total_customers")




df_f = df.groupby("product_name").agg(
    total_sales=("order_price", "sum"),
    total_customers=("customer_id", "nunique")
).sort_values(by="total_sales",ascending=False).reset_index()

max_customer = df_f.loc[df_f["total_sales"].idxmax()]

print(df_f.head(3))


csv_path = os.path.join(current_dir, "top_products.csv")

df_f.to_csv(csv_path, index=False)