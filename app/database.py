import sqlite3


class Database():
    def __init__(self):
        self.connection = sqlite3.connect("db.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        if self.is_first_launch():
            self.create_tables()
        
    def create_tables(self):
        # Create "accounts" table
        self.cursor.execute("""
                CREATE TABLE accounts(
                    id INTEGER PRIMARY KEY,
                    username VARCHAR(255),
                    password BLOB
                );
        """)

        self.connection.commit()

        # create "tasks" table
        self.cursor.execute("""
                CREATE TABLE tasks(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    name VARCHAR(255),
                    category VARCHAR(255)
                );
        """)

        self.connection.commit()


        # Create "sessions" table
        self.cursor.execute("""
                CREATE TABLE sessions(
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    token TEXT,
                    expires_at DATETIME
                );
        """)

        self.connection.commit()

    def is_first_launch(self) -> bool:
        self.cursor.execute("""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name=?;
        """, ("accounts",))

        result = self.cursor.fetchone()

        return result is None