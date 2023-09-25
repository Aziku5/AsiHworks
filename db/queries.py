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
        CREATE TABLE IF NOT EXISTS product (
            productId INTEGER PRIMARY KEY AUTOINCREMENT,
            price FLOAT,
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
    db.commit()


def get_product():
    product = cursor.execute(
        '''
        SELECT * FROM product 
        '''
    )
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_tables()

