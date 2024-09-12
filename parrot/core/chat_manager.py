import sqlite3
from datetime import datetime


class ChatManager:
    """Manages chat sessions and message history."""

    def __init__(self, db_path='chat_history.db'):
        self.db_path = db_path
        self._connect()

    def _connect(self):
        """Connect to the SQLite database and create necessary tables."""
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_name TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                model_name TEXT NOT NULL
            )
        """)

        self.conn.commit()

    def create_chat_session(self, chat_name, model_name) -> int:
        """Creates a new chat session and the corresponding message table."""
        timestamp = datetime.now()

        self.cursor.execute("""
            INSERT INTO chats (chat_name, timestamp, model_name)
            VALUES (?, ?, ?)
        """, (chat_name, timestamp, model_name))

        chat_id = self.cursor.lastrowid
        table_name = f"chat_{chat_id}_messages"

        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                sender TEXT NOT NULL,
                message TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (chat_id) REFERENCES chats(id) ON DELETE CASCADE
            )
        """)

        self.conn.commit()

        return chat_id

    def get_chat_sessions(self):
        """Fetches a list of all chat sessions."""
        self.cursor.execute("SELECT id, chat_name, timestamp, model_name FROM chats")
        return self.cursor.fetchall()

    def add_message(self, chat_id, sender, message):
        """Adds a message to the chat session."""
        table_name = f"chat_{chat_id}_messages"
        timestamp = datetime.now()

        self.cursor.execute(f"""
            INSERT INTO {table_name} (chat_id, sender, message, timestamp)
            VALUES (?, ?, ?, ?)
        """, (chat_id, sender, message, timestamp))

        self.conn.commit()

    def edit_message(self, chat_id, message_id, new_message):
        """Edits an existing message in the chat session."""
        table_name = f"chat_{chat_id}_messages"

        self.cursor.execute(f"""
            UPDATE {table_name}
            SET message = ?, timestamp = ?
            WHERE id = ?
        """, (new_message, datetime.now(), message_id))

        self.conn.commit()

    def delete_chat_session(self, chat_id):
        """Deletes the chat session and its associated messages."""
        self.cursor.execute("DELETE FROM chats WHERE id = ?", (chat_id,))

        table_name = f"chat_{chat_id}_messages"
        self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        self.conn.commit()

    def get_messages(self, chat_id):
        """Fetches all messages for a specific chat session."""
        table_name = f"chat_{chat_id}_messages"
        self.cursor.execute(f"SELECT id, sender, message, timestamp FROM {table_name}")
        return self.cursor.fetchall()

    def close(self):
        """Closes the connection to the database."""
        self.conn.close()
