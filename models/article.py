# models/article.py
class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if not title or not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        if not content or not isinstance(content, str):
            raise ValueError("Content must be a non-empty string.")
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value or not isinstance(value, str) or len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters.")
        self._title = value
