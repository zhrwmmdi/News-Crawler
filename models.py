from datetime import datetime
from peewee import (
    Model, SqliteDatabase, CharField,
    TextField, ForeignKeyField, BooleanField, DateTimeField)

database = SqliteDatabase('Posts.db')


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())

    class Meta:
        """
        the Meta class is a special inner class used to
        provide configuration and metadata about the model
        """
        database = database


class Category(BaseModel):
    name = CharField()


class Article(BaseModel):
    url = CharField()
    title = CharField(null=True)
    body = TextField(null=True)
    subtitle = TextField(null=True)
    category = ForeignKeyField(Category, backref='articles', null=True)
    is_completed = BooleanField(default=False)
