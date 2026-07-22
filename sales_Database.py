
from faker import Faker
import random
import mysql.connector
from datetime import datetime

fake = Faker()

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="$idr@mysql41",
    database="retail_analytics"
)

cursor = connection.cursor()
print("Connected Successfully!")

products = [
    ("Apple AirPods Pro","Electronics",180,250),
    ("Samsung Galaxy Buds","Electronics",120,170),
    ("Rice 5kg","Grocery",18,25),
    ("Cooking Oil","Grocery",7,10),
    ("Coffee Maker","Home",45,65),
    ("T-Shirt","Clothing",8,20),
    ("Running Shoes","Sports",35,60),
    ("Shampoo","Beauty",3,7),
    ("Laptop","Electronics",650,850),
    ("Wireless Mouse","Electronics",10,18)
]

for p in products:
    cursor.execute("""
    INSERT INTO Products
    (ProductName,Category,CostPrice,SellingPrice)
    VALUES (%s,%s,%s,%s)
    """, p)

connection.commit()

print("Products Inserted")

stores = [
    ("Karachi Mall","Karachi","South"),
    ("Lucky One","Karachi","South"),
    ("Packages Mall","Lahore","Punjab"),
    ("Centaurus","Islamabad","North"),
    ("Hyderabad Mall","Hyderabad","Sindh")
]

for s in stores:
    cursor.execute("""
    INSERT INTO Stores
    (StoreName,City,Region)
    VALUES(%s,%s,%s)
    """, s)

connection.commit()

print("Stores Inserted")

genders = ["Male","Female"]
age_groups = ["18-25","26-35","36-50","50+"]

for i in range(500):

    cursor.execute("""
    INSERT INTO Customers
    (Gender,AgeGroup)
    VALUES(%s,%s)
    """,(random.choice(genders),
         random.choice(age_groups)))

connection.commit()

print("Customers Inserted")

payment_methods = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "JazzCash",
    "EasyPaisa"
]

number_of_sales = random.randint(3, 5)

for _ in range(number_of_sales):

    product_id = random.randint(1, 10)
    store_id = random.randint(1, 5)
    customer_id = random.randint(1, 500)

    quantity = random.randint(1, 5)

    payment = random.choice(payment_methods)

    sale_time = datetime.now()

    cursor.execute("""
        INSERT INTO Sales
        (SaleDateTime, ProductID, StoreID, CustomerID, Quantity, PaymentMethod)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        sale_time,
        product_id,
        store_id,
        customer_id,
        quantity,
        payment
    ))

connection.commit()

print(f"{number_of_sales} sales inserted successfully!")

cursor.close()
connection.close()

for store_id in range(1, 6):      # 5 stores
    for product_id in range(1, 11):   # 10 products

        stock = random.randint(50, 300)

        cursor.execute("""
            INSERT INTO Inventory
            (StoreID, ProductID, StockAvailable)
            VALUES (%s, %s, %s)
        """, (store_id, product_id, stock))

connection.commit()

print("Inventory Created Successfully!")

cursor.close()
connection.close()

cursor.execute("""
    SELECT *
    FROM Sales limit 5
""")

sales = cursor.fetchall()

for row in sales:
    print(row)