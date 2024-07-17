# TRTHaber News Crawler

This project is a web scraping tool designed to crawl the TRTHaber news 
website, specifically targeting news articles in the "world" category. 
The tool collects links to news articles, retrieves detailed information about 
each article, and stores the data in a SQLite database.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Modules](#modules)
- [Tests](#tests)
- [Acknowledgements](#acknowledgements)
- [Contact Information](#contact-information)


## Introduction
The TRTHaber News Crawler is a robust web scraping tool designed to 
automatically gather news articles from the TRTHaber website, focusing 
specifically on the "World" category. This project aims to simplify the process
of collecting news data by systematically crawling links, extracting relevant 
information, and storing it in a SQLite database for easy access and analysis.

With the increasing demand for real-time news updates, this crawler provides a 
streamlined solution for aggregating important global news articles, making it 
an invaluable resource for researchers, developers, and news enthusiasts alike.

The crawler is built using Python and leverages popular libraries such as 
BeautifulSoup for HTML parsing and Peewee for database interactions, ensuring 
efficiency and reliability throughout the scraping process.
## Features

- **Link Crawler**: Collects all article links from the "world" category.
- **Article Crawler**: Retrieves detailed information for each article.
- **SQLite Database**: Stores the collected data efficiently.

## Project Structure
my_project/
├── my_project/
│   ├── __init__.py
│   ├── constants.py
│   ├── database.py
│   ├── article_page_parser.py
│   ├── crawl.py
│   ├── main.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_article_page_parser.py
│   ├── test_crawl.py
│   └── ...
├── README.md
├── setup.py
└── requirements.txt

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/zhrwmmdi/News_Crawler.git
    cd NewsCrawler
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Creating Database Tables

At first step, to create the necessary database tables, run:
```bash
python main.py create_tables
```
After running that, the _`trthaber.db`_ file will be created in the project.
### Crawling Links
Next, to crawl links from the TRTHaber "world" category, run:

```bash
python main.py crawl_links
```
### Crawling Articles
To crawl detailed information for each article, run:

```bash
python main.py crawl_articles
```
### Showing Statistics
At any stage, to display statistics about the collected data, run:

```bash
python main.py stats
```
## Configuration
Configuration constants are defined in NewsCrawler/src/constants.py:

```python
# my_project/constants.py

START_DOMAIN = 'https://www.trthaber.com/haber/dunya/'
DEFAULT_DOMAIN = 'https://www.trthaber.com/haber/dunya/{}.sayfa.html'
DATETIME_PATTERN = r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}'
DATABASE_NAME = 'trthaber.db'
```
## Modules
### constants.py
Defines configuration constants used throughout the project.

### database.py
Handles interactions with the SQLite database using the Peewee ORM.

### parse.py
Parses HTML content to extract article data.

### crawl.py
Contains the BaseCrawler, LinkCrawler, and ArticleCrawler
classes for crawling links and articles.

### main.py
Entry point for the project. Contains commands for creating tables, 
crawling links, crawling articles, and showing statistics.

**For more details, see the documentations in the code.**

##Tests
_this part will be added soon._

## Acknowledgements

- **BeautifulSoup** for web scraping.
- **Peewee** for ORM support.
- **Requests** for handling HTTP requests.
- **Flake8** for checking pep8 rules.

## Contact Information

**Author:** Zahra Mohammadi

**Email:** zahra.mmdi2003@gmail.com

