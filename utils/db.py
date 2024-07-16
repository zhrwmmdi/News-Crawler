from crawl import crawl_page_by_url, crawl_all_links
from models import database, Article, Category


def create_tables():
    database.create_tables([Article, Category])


def store_articles():
    articles = Article.select().where(Article.is_completed == False)

    for article in articles:
        data = crawl_page_by_url(article.url)

        if data['category'] not in get_current_categories():
            Category.create(name=data['category'])

        article.title = data['title']
        article.body = data['body']
        article.subtitle = data['subtitle']
        article.category = data['category']
        article.released_time = data['release_time']
        article.update_time = data['update_time']
        article.is_completed = True
        article.save()


def get_current_categories():
    categories = Category.select()
    current_category_names = [c.name for c in categories]
    return current_category_names


def store_all_links():
    crawled_links = crawl_all_links()
    current_urls = Article.select(Article.url)
    current_urls_list = [c.url for c in current_urls]

    for link in crawled_links:
        if link not in current_urls_list:
            Article.create(url=link)


def show_stats():
    articles_count = Article.select().count()
    categories_count = Category.select().count()
    crawled_articles_count = (Article.select()
                              .where(Article.is_completed is True).count())
    print(f'{articles_count} articles\t{categories_count} categories\n'
          f'{crawled_articles_count}/{articles_count} articles crawled')
