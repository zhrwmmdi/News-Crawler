from peewee import SqliteDatabase


class Sqlite:
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self._instance = SqliteDatabase(name)

    @property
    def instance(self):
        return self._instance
