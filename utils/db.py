from crawl import crawl_page_by_url, crawl_all_links
from models import database, Article, Category


def create_tables():
    database.create_tables([Article, Category])


def store_articles():
    articles = Article.select().where(Article.is_completed is False)
    for article in articles:
        data = crawl_page_by_url(article.url)
        article.title = data['title']
        article.body = data['body']
        article.subtitle = data['subtitle']
        article.is_completed = True
        article.save()


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
    crawled_articles_count = (Article.select()
                              .where(Article.is_completed is True).count())
    print(f'{articles_count} articles\t{categories_count} categories\n'
          f'{crawled_articles_count}/{articles_count} articles crawled')
