from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from parse import ArticlePageParser
from utils.database import DB
from constants import START_DOMAIN, DEFAULT_DOMAIN


class BaseCrawler(ABC):

    @staticmethod
    def get_page(url, i=None):
        try:
            response = requests.get(url)
        except requests.HTTPError:
            print('HttpError happened in get method.')
            return None
        return response

    @abstractmethod
    def start(self):
        pass


class LinkCrawler(BaseCrawler):

    @staticmethod
    def validate_links(link_hrefs):
        valid_links = list()
        for link in link_hrefs:
            if (link.endswith('html') and
                    link.startswith(START_DOMAIN)):
                valid_links.append(link)
        return valid_links

    @classmethod
    def crawl_all_links(cls, page_count=10):
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
        crawled_links = self.crawl_all_links()
        db = DB()
        db.store_all_links(crawled_links)


class ArticleCrawler(BaseCrawler):
    def crawl_page_by_url(self, url):
        global article_data
        response = self.get_page(url)

        if response.status_code == 200:
            parser = ArticlePageParser()
            article_data = parser.parse(response.text)

        return article_data

    def start(self):
        db = DB()

        not_crawled_articles = db.get_not_crawled_articles()
        for artcl in not_crawled_articles:
            data = self.crawl_page_by_url(artcl.url)
            db.store_article(artcl, data)
