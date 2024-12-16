from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category="General"):  # Provide default value for category
        self.id = id
        self.name = name
        self.category = category

    def __repr__(self):
        return f'<Magazine {self.name}>'

    # Getter for 'id'
    @property
    def id(self):
        return self._id

    # Setter for 'id'
    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    # Getter for 'name'
    @property
    def name(self):
        return self._name

    # Setter for 'name'
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    # Getter for 'category'
    @property
    def category(self):
        return self._category

    # Setter for 'category'
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    # Method to return the articles of the magazine
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        articles_data = cursor.fetchall()
        conn.close()
        
        articles = []
        for article in articles_data:
            from models.article import Article
            articles.append(Article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]))
        
        return articles

    # Method to return the contributing authors of the magazine
    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.id, authors.name
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        authors_data = cursor.fetchall()
        conn.close()
        
        authors = []
        for author in authors_data:
            from models.author import Author
            authors.append(Author(author["id"], author["name"]))
        
        return authors

    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT title FROM articles WHERE magazine_id = ?', (self.id,))
        titles_data = cursor.fetchall()
        conn.close()
        
        titles = [title["title"] for title in titles_data]
        return titles if titles else None

    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT authors.id, authors.name
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING COUNT(articles.id) > 2
        ''', (self.id,))
        authors_data = cursor.fetchall()
        conn.close()
        
        authors = []
        for author in authors_data:
            from models.author import Author
            authors.append(Author(author["id"], author["name"]))
        
        return authors if authors else None
