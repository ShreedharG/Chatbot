import mysql.connector

items_dict = {}
def fetch_menu():
    global items_dict

    if not items_dict:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2409",
            database="chatbotDB"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items")
        rows = cursor.fetchall()

        for row in rows:
            serial_no, item, price = row
            items_dict[serial_no] = {"item": item, "price": float(price)}

        cursor.close()
        conn.close()
    return

def insert_order(order_id, item, quantity, price):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2409",
        database="chatbotDB"
    )
    cursor = conn.cursor()

    cursor.execute("INSERT INTO orders (order_ID, Item, Quantity, Price) VALUES (%s, %s, %s, %s)",
                    (order_id, item, quantity, price))
    cursor.execute("INSERT INTO order_status (order_ID) VALUES (%s)", (order_id,))
    conn.commit()

    cursor.close()
    conn.close()
    return

def fetch_order_ids():
    order_ids = []

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2409",
        database="chatbotDB"
    )

    cursor = conn.cursor()  
    cursor.execute("SELECT order_ID FROM orders")
    rows = cursor.fetchall()

    order_ids = [ row[0] for row in rows ]
        
    cursor.close()
    conn.close()
    return order_ids

def fetch_order_status(order_ID):
    conn = mysql.connector.connect(
        host="localhost",
        user = "root",
        password = "2409",
        database = "chatbotDB"
    )

    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT o.*, os.*
        FROM orders o
        JOIN order_status os ON o.order_ID = os.order_ID
        WHERE o.order_ID = %s
    """
    cursor.execute(query, (order_ID,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result