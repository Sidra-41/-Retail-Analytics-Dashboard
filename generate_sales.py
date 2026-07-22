import random
import mysql.connector
from datetime import datetime, timedelta
import time

def create_sale():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="$idr@mysql41",
        database="retail_analytics"
)

    cursor = connection.cursor()
    # print("Connected Successfully!")

    cursor.execute("""
    SELECT ProductID,
        CostPrice,
        SellingPrice
    FROM Products
    """)

    products = cursor.fetchall()
    
    selected_product = random.choice(products)
    product_id, unit_cost, unit_price = selected_product
    # print("Selected Product:", product_id)
    # print("Cost Price:", unit_cost)
    # print("Selling Price:", unit_price)

    cursor.execute("""
    SELECT StoreID
    FROM Stores
    """)

    stores = cursor.fetchall()
    selected_store = random.choice(stores)
    store_id = selected_store[0]
    # print("Store ID:", store_id)

    cursor.execute("""
    SELECT CustomerID
    FROM Customers
    """)

    customers = cursor.fetchall()
    selected_customer = random.choice(customers)
    customer_id = selected_customer[0]
    # print("Customer ID:", customer_id)

    cursor.execute("""
    SELECT StockAvailable
    FROM Inventory
    WHERE StoreID = %s
    AND ProductID = %s
    """, (store_id, product_id))

    result = cursor.fetchone()

    if result:
        stock_available = result[0]
        # print("Stock Available:", stock_available)

    else:
        print("Inventory record not found.")
        connection.close()
        return

    quantity = random.randint(1, min(5, stock_available))
    # print("Quantity Sold:", quantity)

    discount = random.choice([0, 0, 0, 5, 10])
    # print("Discount:", discount)

    total_amount = quantity * float(unit_price) * (1 - discount / 100)
    # print("Total Amount:", total_amount)

    payment_method = random.choice([
        "Cash",
        "Credit Card",
        "Debit Card",
        "JazzCash",
        "EasyPaisa"
    ])
    sales_channel = random.choice([
        "In-Store",
        "Online"
    ])

    sale_time = datetime.now() - timedelta(
        minutes=random.randint(0,15)
)

    cursor.execute("""
    INSERT INTO Sales
    (
        SaleDateTime,
        ProductID,
        StoreID,
        CustomerID,
        Quantity,
        PaymentMethod,
        UnitPrice,
        Discount,
        TotalAmount,
        UnitCost,
        SalesChannel
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """,
    (
        sale_time,
        product_id,
        store_id,
        customer_id,
        quantity,
        payment_method,
        unit_price,
        discount,
        total_amount,
        unit_cost,
        sales_channel
    ))

    print(f"Sale created: Product {product_id}, Quantity {quantity}, Amount {total_amount}")

    cursor.execute("""
    UPDATE Inventory
    SET StockAvailable = StockAvailable - %s
    WHERE StoreID = %s
    AND ProductID = %s
    """,
    (
        quantity,
        store_id,
        product_id
    ))

    print("Inventory Updated!")
    connection.commit()

    cursor.close()
    connection.close()

while True:

    print("Starting new sales batch...")

    for i in range(5):
        create_sale()

    print("Waiting 15 minutes for next batch...")

    time.sleep(30)