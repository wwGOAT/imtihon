import psycopg2 as db
from main import config
import random


class Database:
    def __init__(self):
        self.conn = db.connect(
            database=config.DB_NAME,
            password=config.DB_PASS,
            user=config.DB_USER,
            host=config.DB_HOST
        )
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.conn.commit()
        user_table = """
        CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        chat_id BIGINT NOT NULL,
        full_name VARCHAR(55),
        phone_number VARCHAR(13),
        location_name VARCHAR(55))
        """

        courses = """
        CREATE TABLE IF NOT EXISTS courses (
        course_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            rating FLOAT,
            active_Students INT,
            teacher VARCHAR(45),
            lenguage VARCHAR(30),
            price NUMERIC,
            support_date DATE,
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())"""

        self.cursor.execute(user_table)
        self.cursor.execute(courses)

        self.conn.commit()

    def get_user_by_chat_id(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_user(self, chat_id):
        query = f"SELECT * FROM users WHERE chat_id = {chat_id}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def get_courses(self):
        query = f"SELECT * FROM courses"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
