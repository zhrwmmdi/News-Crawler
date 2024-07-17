"""
parse.py

This module defines the ArticlePageParser class which is used to parse HTML
content of news articles to extract relevant information such as title, body,
subtitle, category and timestamps using BeautifulSoup.
"""
import re
from bs4 import BeautifulSoup

from constants import DATETIME_PATTERN


class ArticlePageParser:
    """
    ArticlePageParser is responsible for parsing the HTML content
    of a news article.

    Attributes:
        soup (BeautifulSoup): A BeautifulSoup object representing
        the parsed HTML content.

    Methods:
        parse(html_data): Parses the given HTML content and
        extracts article data.
    """
    def __init__(self):
        self.soup = None

    @property
    def title(self):
        """
        Extracts the title of the article.

        Returns:
            str: The title of the article or None if not found.
        """
        title = self.soup.find('h1', attrs={'class': 'news-title'})
        if title:
            return title.text

    @property
    def body(self):
        """
        Extracts the body content of the article.

        Returns:
            str: The body content of the article or None if not found.
        """
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
        """
        Extracts the subtitle of the article.

        Returns:
            str: The subtitle of the article or None if not found.
        """
        subtitle_tag = self.soup.find('h2', attrs={'class': 'news-spot'})
        if subtitle_tag:
            return subtitle_tag.text

    @property
    def category(self):
        """
        Extracts the category of the article.

        Returns:
            str: The category of the article or None if not found.
        """
        category_tag = self.soup.find('span', attrs={'class': 'category-tag'})
        if category_tag:
            return category_tag.text

    @property
    def time(self):
        """
       Extracts the creation and update times of the article.

       Returns:
           list: A list containing the creation time and update time,
           or an empty list if not found.
       """
        global times
        creation_tag = self.soup.find('span', attrs={'class': 'created-date'})
        if creation_tag:
            la = creation_tag.find('label')
            if la:
                la.extract()
            times = re.findall(DATETIME_PATTERN, creation_tag.text)
        return times

    def parse(self, html_data):
        """
        Parses the given HTML content to extract article data.

        Args:
            html_data (str): The HTML content of the article.

        Returns:
            dict: A dictionary containing the extracted article data.
        """
        self.soup = BeautifulSoup(html_data, 'html.parser')
        article_data = dict(title=self.title,
                            body=self.body,
                            subtitle=self.subtitle,
                            category=self.category,
                            release_time=self.time[0],
                            update_time=self.time[1]
                            )

        return article_data
