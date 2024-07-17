"""
models.py

This module defines the database models using the Peewee ORM.
"""
from datetime import datetime
from peewee import (
    Model, CharField,
    TextField, ForeignKeyField, BooleanField, DateTimeField, SqliteDatabase)

from constants import DATABASE_NAME

# Initialize the database connection
database = SqliteDatabase(DATABASE_NAME)


class BaseModel(Model):
    """
    BaseModel serves as an abstract base class for all database models.

    Attributes:
        crawled_time (DateTimeField): The timestamp when the record was
        created, defaults to the current datetime
    """
    crawled_time = DateTimeField(default=datetime.now())

    class Meta:
        """
        Metaclass to specify the database for the model.
        """
        database = database


class Category(BaseModel):
    """
    Category model represents a category of articles.

    Attributes:
        name (CharField): The name of the category.
    """
    name = CharField()


class Article(BaseModel):
    """
    Article model represents a news article with various attributes and a
    relationship to a category.

    Attributes:
        url (CharField): The URL of the article page.
        title (CharField): The title of the news, nullable.
        body (TextField): The body content of the news, it's nullable because
        it is filled later in crawling.
        subtitle (TextField): The subtitle of the news, it's nullable because
        it is filled later in crawling.
        category (ForeignKeyField): The foreign key to the category model,
        it's nullable because it is filled later in crawling.
        is_completed (BooleanField): Indicates if crawling this news object is
        completed, defaults to False.
        released_time (DateTimeField): The release timestamp of the news,
        it's nullable because it is filled later in crawling.
        update_time (DateTimeField): The last update timestamp of the news,
        it's nullable because it is filled later in crawling.
    """
    url = CharField()
    title = CharField(null=True)
    body = TextField(null=True)
    subtitle = TextField(null=True)
    category = ForeignKeyField(Category, backref='articles', null=True)
    is_completed = BooleanField(default=False)
    released_time = DateTimeField(null=True)
    update_time = DateTimeField(null=True)
