"""
main.py

This script serves as the entry point for the web scrawling application.
It provides commands to create database tables, crawl links, show statistics,
and crawl articles.

First run 'python main.py create_tables' to create the Sqlite database.

Then run 'python main.py crawl_links' to get all news page URLs and
store in database.

At last run 'python main.py crawl_articles' to get all data of each news URLs
and update the database.

At any time you can run 'python main.py stats' to get the statistics of data.
"""
import sys

from crawl import LinkCrawler, ArticleCrawler
from utils.database import DB

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: python main.py ["
              "create_tables|crawl_links|stats|crawl_articles]")
        sys.exit(1)
    else:
        db = DB()

        if sys.argv[1] == 'create_tables':
            db.create_tables()
            print("Tables created successfully.")
        elif sys.argv[1] == 'crawl_links':
            crawler = LinkCrawler()
            crawler.start()
            print("Link crawling completed.")
        elif sys.argv[1] == 'stats':
            db.show_stats()
        elif sys.argv[1] == 'crawl_articles':
            crawler = ArticleCrawler()
            crawler.start()
            print("Article crawling completed.")
        else:
            print(f"Unknown command: {sys.argv[1]}")
            print("Usage: python main.py ["
                  "create_tables|crawl_links|stats|crawl_articles]")
            sys.exit(1)
