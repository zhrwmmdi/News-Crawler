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


def get_all_links(topic):
    response = requests.get('https://www.trthaber.com/haber/dunya/')
    html_doc = response.text
    soup = BeautifulSoup(html_doc,'html.parser')
    link_tags = soup.find_all('a')

    links = list()
    for tag in link_tags:
        links.append(tag.get('href'))

    valid_links = list()
    for link in links:
        if link.endswith('html') and link.startswith('https://www.trthaber.com/haber/dunya/'):
            valid_links.append(link)

    return valid_links


if __name__ == '__main__':
    # links = [
    #     'https://www.trthaber.com/haber/dunya/kuzey-koreden-sinirin-kuzeyine-pyongyang-karsiti-brosurler-gonderen-guney-koreye-tepki-868496.html',
    #     'https://www.trthaber.com/haber/dunya/avrupa-birligi-icin-kader-haftasi-basliyor-868489.html',
    #     'https://www.trthaber.com/haber/dunya/israilin-gazzeye-gece-boyu-duzenledigi-saldirilarda-cok-sayida-filistinli-oldu-868481.html',
    # ]

    # for link in links:
    #     crawl_page_by_url(link)

    get_all_links('sam[le')