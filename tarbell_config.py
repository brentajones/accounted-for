# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "accounted-for"

# Descriptive title of project
TITLE = "Accounted For"

# Google spreadsheet key
SPREADSHEET_KEY = "0AgR1tOj24iNkdFJjanRZeXgyT2NIMHlwYmJMNThQS2c"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "brentajones-prod/accounted-for",
    "staging": "brentajones-stg/accounted-for",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'accounted-for',
    'title': 'Accounted For'
}