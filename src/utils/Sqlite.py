"""
Sqlite.py
This module provides a singleton implementation
of an SQLite database connection.
"""
from peewee import SqliteDatabase


class Sqlite:
    """
   A singleton class to manage a single instance
   of an SQLite database connection.

   This class ensures that only one instance of the SQLite database connection
   exists throughout the application. It uses the singleton design pattern to
   provide a single shared instance.

   Attributes:
       _instance (SqliteDatabase):
            The singleton instance of the SQLite database connection.
   """
    _instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        """
        Creates a new instance of the Sqlite class if one does not exist.

        This method overrides the default behavior of object creation to ensure
        that only one instance of the Sqlite class is created.

        :param args: Variable length argument list.
        :param kwargs: Arbitrary keyword arguments.

        Returns:
            Sqlite: The singleton instance of the Sqlite class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        """
        Initializes the Sqlite class with the given database name.

        This method initializes the singleton instance with an SQLite
        database connection.

        :param name: The name of the SQLite database.
        """
        self._instance = SqliteDatabase(name)

    @property
    def instance(self):
        """
        Gets the singleton instance of the SQLite database connection.

        This property provides access to SQLite database connection instance.

        :return:
            The singleton instance of the SQLite database connection.
        """
        return self._instance
