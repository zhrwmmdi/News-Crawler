import re
from bs4 import BeautifulSoup

from constants import DATETIME_PATTERN


class ArticlePageParser:
    def __init__(self):
        self.soup = None

    @property
    def title(self):
        title = self.soup.find('h1', attrs={'class': 'news-title'})
        if title:
            return title.text

    @property
    def body(self):
        body_text = ''
        body_tag = self.soup.find('div', attrs={'class': 'news-content'})
        if body_tag:
            p_tags = body_tag.find_all('p')
            for p in p_tags:
                body_text = body_text + p.text
        else:
            body_text = None
        return body_text

    @property
    def subtitle(self):
        subtitle_tag = self.soup.find('h2', attrs={'class': 'news-spot'})
        if subtitle_tag:
            return subtitle_tag.text

    @property
    def category(self):
        category_tag = self.soup.find('span', attrs={'class': 'category-tag'})
        if category_tag:
            return category_tag.text

    @property
    def time(self):
        global times
        creation_tag = self.soup.find('span', attrs={'class': 'created-date'})
        if creation_tag:
            la = creation_tag.find('label')
            if la:
                la.extract()
            times = re.findall(DATETIME_PATTERN, creation_tag.text)
        return times

    def parse(self, html_data):
        self.soup = BeautifulSoup(html_data, 'html.parser')
        article_data = dict(title=self.title, body=self.body, subtitle=self.subtitle,
                            category=self.category, release_time=self.time[0], update_time=self.time[1])

        return article_data

