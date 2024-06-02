from typing import List


CACHE_DIRECTORY = ".shurl-cache"

"""
Ignore domain as training data if listed.
"""
IGNORED_DOMAINS: List[str] = [
    "rutgers.zoom.us",  # require some type of authentication
    "meet.google.com",  # require some type of authentication
    "rutgers.mediaspace.kaltura.com",  # require some type of authentication
    "youtube.com",  # Usually does not have enough information
    "youtu.be",  # Usually does not have enough information
]

"""
Some websites may have been deleted after their shortened URL creation.
"""
ONLY_ACCEPT_OK_RESPONSES: bool = True
