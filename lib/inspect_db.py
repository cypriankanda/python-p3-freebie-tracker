import sqlite3
import os

def print_table_contents(db_path, table_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        print(f"\nTable '{table_name}':")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error reading table {table_name}: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    db_path = os.path.abspath("freebies.db")
    print(f"Using DB file at: {db_path}")

    tables = ["companies", "devs", "freebies"]

    for table in tables:
        print_table_contents(db_path, table)
