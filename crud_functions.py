import sqlite3

def initiate_db():
    connection = sqlite3.connect("products.db")
    connection1 = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor1 = connection1.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL,
    image_url TEXT
    ) 
    ''')
    cursor1.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INT PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()
    connection1.commit()
    connection1.close()


def get_all_products():
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute("SELECT title, description, price, image_url FROM Products")
    products = cursor.fetchall()
    conn.close()
    return products

def add_test_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    products = [
        ("Протеин", "Белок, строительный материал для твоего организма, который состоит из аминокислот.", 3000, "https://pcdn.goldapple.ru/p/p/19000033923/imgmain.jpg"),
        ("Креатин", "Азотсодержащая карбоновая кислота, которая встречается в организме позвоночных", 2500, "https://cdn1.ozone.ru/s3/multimedia-a/c600/6739414354.jpg"),
        ("Тренболон", "Это андроген и анаболический стероид (AAS) из группы нандролонов, который сам по себе никогда не продавался", 3500, "https://avatars.mds.yandex.net/i?id=9779deb43a8b3c97dfb35e0a492c8d23c491ddcc67df15fd-12209413-images-thumbs&n=13"),
        ("BCAA", "Это биологически активная добавка к пище, содержащая в своем составе аминокислоты: L-лейцин, L-изолейцин, L-валин", 2000, "https://cdn1.ozone.ru/s3/multimedia-z/6020988647.jpg"),
    ]
    cursor.executemany('INSERT INTO Products (title, description, price, image_url) VALUES (?, ?, ?, ?)', products)
    conn.commit()
    conn.close()

def add_users(username, email, age):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)", (username, email, age, 1000))
    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM Users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None