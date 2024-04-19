from db import Database

def create_table():
    user = """
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(50),
    phone_number VARCHAR(13) NOT NULL,
    username VARCHAR(50) NOT NULL,
    password VARCHAR NOT NULL,
    create_date  TIMESTAMP  DEFAULT now())"""

    data = {
        "users": user
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], 'create')}")


if __name__ == "__main__":
    create_table()