from datetime import datetime
from peewee import (
    Model, CharField,
    TextField, ForeignKeyField, BooleanField, DateTimeField, SqliteDatabase)

from constants import DATABASE_NAME

database = SqliteDatabase(DATABASE_NAME)


class BaseModel(Model):
    crawled_time = DateTimeField(default=datetime.now())

    class Meta:
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
    released_time = DateTimeField(null=True)
    update_time = DateTimeField(null=True)
