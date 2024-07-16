import requests
from bs4 import BeautifulSoup


def crawl_page_by_url(url):
    response = requests.get(url)
    body_text = ''
    title_text = None
    subtitle_text = None
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
            print(subtitle_text)

    return {'title': title_text, 'body': body_text, 'subtitle': subtitle_text}

# TODO: obejct oriented and class making


def crawl_all_links(topic, page_count=10):
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

if __name__ == '__main__':
    urls = [
        'https://www.trthaber.com/haber/dunya/penguen-ve-yumurta-galaksileri-ic-ice-goruntulendi-868254.html',
        'https://www.trthaber.com/haber/dunya/italya-g7-ticaret-bakanlari-toplantisina-turkiyeyi-de-davet-etti-868260.html',
    ]
    for u in urls:
        crawl_page_by_url(u)