import sys
from utils.db import create_tables, store_all_links, show_stats, store_articles

if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_tables()
    elif sys.argv[1] == 'crawl_links':
        store_all_links()
    elif sys.argv[1] == 'status':
        show_stats()
    elif sys.argv[1] == 'crawl_articles':
        store_articles()
