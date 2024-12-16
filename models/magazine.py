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
        pass

    # Method to return the contributing authors of the magazine
    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
