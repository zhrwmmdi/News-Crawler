"""
crawl.py

This module is an abstract factory design pattern module that defines the
BaseCrawler, LinkCrawler, and ArticleCrawler classes for web scraping using the
Peewee ORM for database interactions. These classes are designed to crawl links
and articles from specified domains and store result data in database.
"""
from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from parse import ArticlePageParser
from utils.database import DB
from constants import START_DOMAIN, DEFAULT_DOMAIN


class BaseCrawler(ABC):
    """
    BaseCrawler serves as an abstract base class for all crawlers.

    Methods:
        get_page(url, i=None): Static method to fetch a web page by URL.
        start(): Abstract method to start the crawling process.
    """

    @staticmethod
    def get_page(url, i=None):
        """
        Fetches a web page by URL.

        Args:
            url (str): The URL of the web page to fetch.
            i (int, optional): An optional index for pagination.
            Defaults to None.

        Returns:
            response: The HTTP response object or None if an error occurs.
        """
        try:
            response = requests.get(url)
        except requests.HTTPError:
            print('HttpError happened in get method.')
            return None
        return response

    @abstractmethod
    def start(self):
        """
        Starts the crawling process. Must be implemented by subclasses.
        """
        pass


class LinkCrawler(BaseCrawler):
    """
   LinkCrawler crawls all links from the DEFAULT DOMAIN to get a list of news
   URLs.

   Methods:
       validate_links(link_hrefs): Static method to validate links and exclude
       not required links.
       crawl_all_links(page_count=10): Class method to crawl all links across
       pages.
       start(): Starts the link crawling process.
   """

    @staticmethod
    def validate_links(link_hrefs):
        """
       Validates and filters links that end with 'html' and start with the
       START DOMAIN to exclude not required links.

       Args:
           link_hrefs (list): A list of link hrefs.

       Returns:
           list: A list of valid links.
       """
        valid_links = list()
        for link in link_hrefs:
            if (link.endswith('html') and
                    link.startswith(START_DOMAIN)):
                valid_links.append(link)
        return valid_links

    @classmethod
    def crawl_all_links(cls, page_count=10):
        """
        Crawls all links across the specified number of pages.

        Args:
            page_count (int): The number of pages to crawl. Defaults to 10.

        Returns:
            set: A set of unique valid links without duplicated data.
        """
        link_tags = list()

        for i in range(page_count):
            response = super().get_page(DEFAULT_DOMAIN.format(i))
            soup = BeautifulSoup(response.text, 'html.parser')
            ll = soup.find_all('a')
            link_tags.extend(ll)

        link_hrefs = [tag.get('href') for tag in link_tags]

        valid_links = cls.validate_links(link_hrefs)
        return set(valid_links)

    def start(self):
        """
        Starts the link crawling process and stores the crawled links in
        the database.
        """
        crawled_links = self.crawl_all_links()
        db = DB()
        db.store_all_links(list(crawled_links))


class ArticleCrawler(BaseCrawler):
    """
    ArticleCrawler crawls each news articles from the collected links.

    Methods:
        crawl_page_by_url(url): Crawls a single article page by URL.
        start(): Starts the article crawling process.
    """
    def crawl_page_by_url(self, url):
        """
        Crawls a single article page by URL.

        Args:
            url (str): The URL of the article page to crawl.

        Returns:
            dict: The parsed article data.
        """
        global article_data
        response = self.get_page(url)

        if response.status_code == 200:
            parser = ArticlePageParser()
            article_data = parser.parse(response.text)

        return article_data

    def start(self):
        """
        Starts the article crawling process and stores the crawled
        articles in the database.
        """
        db = DB()

        not_crawled_articles = db.get_not_crawled_articles()
        for artcl in not_crawled_articles:
            data = self.crawl_page_by_url(artcl.url)
            db.store_article(artcl, data)
