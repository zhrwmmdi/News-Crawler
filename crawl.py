import requests
from bs4 import BeautifulSoup


def crawl_page_by_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        html_doc = response.text
        soup = BeautifulSoup(html_doc,'html.parser')
        title = soup.find('h1', attrs={'class': 'news-title'})
        if title:
            print(title.text)


def get_all_links(topic, page_count=10):
    link_tags = list()

    for i in range(page_count):
        response = requests.get(f'https://www.trthaber.com/haber/dunya/{i}.sayfa.html')
        soup = BeautifulSoup(response.text, 'html.parser')
        ll = soup.find_all('a')
        link_tags.extend(ll)

    link_hrefs = [tag.get('href') for tag in link_tags]

    valid_links = validate_links(link_hrefs)
    return valid_links


def validate_links(link_hrefs):
    valid_links = list()
    for link in link_hrefs:
        if link.endswith('html') and link.startswith('https://www.trthaber.com/haber/dunya/'):
            valid_links.append(link)
    return valid_links

