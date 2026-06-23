import pandas as pd
import sqlite3


def load_excel(file_path):
    df = pd.read_excel(
        file_path,
        header=1
    )

    return df


def create_database():
    conn = sqlite3.connect("data/nifty100.db")

    with open("sql/schema.sql", "r") as f:
        schema = f.read()

    conn.executescript(schema)

    print("Tables Created")

    conn.close()


"""if __name__ == "__main__":
    create_database()"""