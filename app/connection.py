import sqlite3


class Connection():
    # Initialise connection
    def __init__(self):
        self.connection = sqlite3.connect("db.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

    # Add new task
    def add_task(self, user_id: int, name: str, category: str):
        self.cursor.execute("""
            INSERT INTO tasks
            (user_id, name, category)
            VALUES (?, ?, ?);
        """, (user_id, name, category))

        self.connection.commit()

    # Closes the connection
    def close(self):
        self.connection.close()
