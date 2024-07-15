import requests
from bs4 import BeautifulSoup

from models import Article, Category


def crawl_page_by_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find('h1', attrs={'class': 'news-title'})
        if title:
            print(title.text)


def get_all_links(topic):
    link_tags = list()

    for i in range(10):
        response = requests.get(f'https://www.trthaber.com/haber/dunya/{i}.sayfa.html')
        html_doc = response.text
        soup = BeautifulSoup(html_doc,'html.parser')
        ll = soup.find_all('a')
        link_tags.extend(ll)

    link_hrefs = list()
    for tag in link_tags:
        link_hrefs.append(tag.get('href'))

    valid_links = list()
    for link in link_hrefs:
        if link.endswith('html') and link.startswith('https://www.trthaber.com/haber/dunya/'):
            valid_links.append(link)

    return valid_links
