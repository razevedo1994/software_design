class Book:
    def __init__(self, title: str, last: str, first: str):
        self._title = title
        self._last = last
        self._first = first

    @property
    def title(self):
        return self._title

    @property
    def last(self):
        return self._last

    @property
    def first(self):
        return self._first

    def __str__(self):
        return f"{{TITLE: '{self._title}', LAST: '{self._last}', FIRST: '{self._first}'}}"
