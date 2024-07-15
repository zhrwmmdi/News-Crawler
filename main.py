import sys

from crawl import get_all_links
from models import Article, Category
from utils.db import create_tables


def store_all_links():
    links = get_all_links('sample')
    category = Category.create(name='world')
    for link in links:
        article = Article.create(url=link, category=category)
        print(article.id)


if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_tables()
    elif sys.argv[1] == 'run':
        store_all_links()
