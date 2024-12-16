# models/author.py
class Author:
    def __init__(self, id, name):
        if not name or not isinstance(name, str):
            raise ValueError("Name must be a non-empty string.")
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Name must be a non-empty string.")
        self._name = value
