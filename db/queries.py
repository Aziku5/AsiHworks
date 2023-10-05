import sqlite3
from pathlib import Path


def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).parent.parent / "db.sqlite3")
    cursor = db.cursor()


def create_tables():
    cursor.execute(
        """
        DROP TABLE IF EXISTS product
        """
    )
    cursor.execute(
        """
       DROP TABLE IF EXISTS category
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            price FLOATprice FLOAT,
            categoryId INTEGER,
            FOREIGN KEY (categoryId) REFERENCES category (id)
            
        )
        """
    )
    db.commit()


def populate_tables():
    cursor.execute(
        """
         INSERT INTO product (name, price)
        VALUES  ('Лист', 25.0),
                ('Кисть', 19.0),
                ('Картина', 26.0)
        """
    )
    cursor.execute(
        """
        INSERT INTO product (name, price, categoryId)
        VALUES ('А4', 25.0, 1),
                ('А3', 25, 1),
                ('KИСТЬ', 19.0, 2),
                ('KИСТЬ2', 19.0, 2),
                ('КАРТИНА', 26.0, 3),
                ('КАРТИНА2', 26.0, 3)
        """
    )
    db.commit()


def get_product():
    cursor.execute(
        """
          SELECT p.name, c.name FROM product p JOIN category c ON p.categoryId = c.id
          """
    )
    return cursor.fetchall()


def get_product_by_category(category_id):
    cursor.execute(
        """
        SELECT * FROM product WHERE categoryId = :c_id
        """,
        {"c_id": category_id},
    )
    return cursor.fetchall()


def select_sub():
    cursor.execute('''SELECT ID FROM subscrebu''')
    users = cursor.fetchall()
    users_id = [user for user in users]
    return users_id
    return [user for user in cursor.fetchall()]



if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()
