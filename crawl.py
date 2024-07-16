import requests
from bs4 import BeautifulSoup
import re


def crawl_page_by_url(url):
    response = requests.get(url)
    body_text = ''
    global title_text
    global subtitle_text
    global category_text
    global created_time_text
    global updated_time_text

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.find('h1', attrs={'class': 'news-title'})
        if title:
            title_text = title.text

        body_tag = soup.find('div', attrs={'class': 'news-content'})
        if body_tag:
            p_tags = body_tag.find_all('p')
            for p in p_tags:
                body_text = body_text + p.text
        else:
            body_text = None

        subtitle_tag = soup.find('h2', attrs={'class': 'news-spot'})
        if subtitle_tag:
            subtitle_text = subtitle_tag.text

        category_tag = soup.find('span', attrs={'class': 'category-tag'})
        if category_tag:
            category_text = category_tag.text

        creation_tag = soup.find('span',attrs={'class': 'created-date'})
        if creation_tag:
            creation_tag.find('label').extract()
            matches = re.findall(r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}', creation_tag.text)
            created_time_text = matches[0]
            updated_time_text = matches[1]

    return {'title': title_text, 'body': body_text, 'subtitle': subtitle_text, 'category': category_text, 'release_time': created_time_text, 'update_time': updated_time_text}

# TODO: obejct oriented and class making


def crawl_all_links(page_count = 10):
    link_tags = list()

    for i in range(page_count):
        response = requests.get(
            f'https://www.trthaber.com/haber/dunya/{i}.sayfa.html'
        )
        soup = BeautifulSoup(response.text, 'html.parser')
        ll = soup.find_all('a')
        link_tags.extend(ll)

    link_hrefs = [tag.get('href') for tag in link_tags]

    valid_links = validate_links(link_hrefs)
    return set(valid_links)


def validate_links(link_hrefs):
    valid_links = list()
    for link in link_hrefs:
        if (link.endswith('html') and
                link.startswith('https://www.trthaber.com/haber/dunya/')):
            valid_links.append(link)
    return valid_links
