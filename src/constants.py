"""
constants.py

This module defines constants used throughout the application.
"""

# The starting domain for the news articles
START_DOMAIN = 'https://www.trthaber.com/haber/dunya/'

# The default domain pattern for paginated news articles
DEFAULT_DOMAIN = 'https://www.trthaber.com/haber/dunya/{}.sayfa.html'

# The regex pattern to match datetime strings in the format 'dd.mm.yyyy hh:mm'
DATETIME_PATTERN = r'\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}'

# The name of the SQLite database file
DATABASE_NAME = 'trthaber.db'
