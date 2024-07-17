"""
database.py

This module defines the DB class which manages the SQLite database operations
of the whole project for Articles and Categories using the Peewee ORM.
"""
from src.utils.models import Article, Category, database


class DB:
    """
    DB class manages the SQLite database operations for the whole project.

    Attributes:
        SqliteDatabase (SqliteDatabase): The database connection object that
        comes from models.py
    """
    SqliteDatabase = database

    @property
    def database(self):
        """
        Gets the database connection.

        Returns:
            SqliteDatabase: The database connection object.
        """
        return self.SqliteDatabase

    def create_tables(self):
        """
        Creates the tables for the Article and Category models.
        """
        self.database.create_tables([Article, Category])

    @staticmethod
    def get_current_categories():
        """
        Retrieves the names of all current categories.

        Returns:
            list: A list of current category names in database, it is used
            later in store_article method to avoid data redundancy in creating
            categories.
        """
        categories = Category.select()
        current_category_names = [c.name for c in categories]
        return current_category_names

    def store_article(self, article, data):
        """
       Stores an article in the database.

       If the category of the article does not exist,
       it creates a new category.

       Args:
           article (Article): The Article object to be stored.
           data (dict): A dictionary containing the article data with keys
           'title', 'body', 'subtitle', 'category',
           'release_time' and 'update_time'.
       """
        if data['category'] not in self.get_current_categories():
            Category.create(name=data['category'])

        article.title = data['title']
        article.body = data['body']
        article.subtitle = data['subtitle']
        article.category = data['category']
        article.released_time = data['release_time']
        article.update_time = data['update_time']
        article.is_completed = True
        article.save()

    @staticmethod
    def store_all_links(crawled_links):
        """
        Stores all the crawled links in the database.

        Only stores the links that are not already in the database.

        Args:
            crawled_links (list): A list of crawled URLs.
        """
        current_urls = Article.select(Article.url)
        current_urls_list = [c.url for c in current_urls]

        for link in crawled_links:
            if link not in current_urls_list:
                Article.create(url=link)

    @staticmethod
    def get_not_crawled_articles():
        """
        Retrieves all articles that have not been crawled.

        Returns:
            list: A list of Article objects that have not been crawled.
        """
        articles = Article.select().where(Article.is_completed == False)
        return articles

    @staticmethod
    def show_stats():
        """
        Prints statistics about the articles and categories in the database.

        Shows the total number of articles, categories,
        and the number of crawled articles.
        """
        articles_count = Article.select().count()
        categories_count = Category.select().count()
        crawled_articles_count = (Article.select()
                                  .where(Article.is_completed == True).count())
        print(f'{articles_count} articles\t{categories_count} categories\n'
              f'{crawled_articles_count}/{articles_count} articles crawled')
