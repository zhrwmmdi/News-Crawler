import sys

from crawl import LinkCrawler, ArticleCrawler
from utils.database import DB

if __name__ == '__main__':
    db = DB()

    if sys.argv[1] == 'create_tables':
        db.create_tables()
    elif sys.argv[1] == 'crawl_links':
        crawler = LinkCrawler()
        crawler.start()
    elif sys.argv[1] == 'status':
        db.show_stats()
    elif sys.argv[1] == 'crawl_articles':
        crawler = ArticleCrawler()
        crawler.start()
