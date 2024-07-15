import sys

from crawl import crawl_all_links, crawl_page_by_url
from models import Article, Category
from utils.db import create_tables


def store_all_links():
    crawled_links = crawl_all_links('sample')
    category = Category.create(name='world')

    current_urls = Article.select(Article.url)
    current_urls_list = [c.url for c in current_urls]

    for link in crawled_links:
        if link not in current_urls_list:
            article = Article.create(url=link, category=category)
            print(article.id)


def show_stats():
    articles_count = Article.select().count()
    categories_count = Category.select().count()
    print(f'{articles_count} articles\t{categories_count} categories')


def store_articles():
    articles = Article.select().where(Article.is_completed == False)
    for article in articles:
        data = crawl_page_by_url(article.url)
        article.title = data['title']
        article.body = data['body']
        article.is_completed = True
        article.save()


if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_tables()
    elif sys.argv[1] == 'crawl_links':
        store_all_links()
    elif sys.argv[1] == 'status':
        show_stats()
    elif sys.argv[1] == 'crawl_articles':
        store_articles()
