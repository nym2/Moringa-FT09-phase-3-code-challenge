from database.connection import get_db_connection
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    def author(self):
        # Local import to avoid circular import
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (self.author_id,))
        author_data = cursor.fetchone()
        conn.close()
        if author_data:
            return Author(author_data["id"], author_data["name"])
        return None

    def magazine(self):
        # Local import to avoid circular import
        from models.magazine import Magazine
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (self.magazine_id,))
        magazine_data = cursor.fetchone()
        conn.close()
        if magazine_data:
            return Magazine(magazine_data["id"], magazine_data["name"], magazine_data["category"])
        return None
