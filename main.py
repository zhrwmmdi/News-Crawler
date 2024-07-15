import sys
from utils.db import create_tables


def run():
    pass


if __name__ == '__main__':
    if sys.argv[1] == 'create_tables':
        create_tables()
    elif sys.argv[1] == 'run':
        run()
