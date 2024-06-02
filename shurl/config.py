from typing import List

"""
Ignore domain as training data if listed.
"""

IGNORED_DOMAINS: List[str] = [
    "zoom.us",
    "meet.google.com",
    "rutgers.mediaspace.kaltura.com",
]

"""
Some websites may have been deleted after their shortened URL creation.
"""
ONLY_ACCEPT_OK_RESPONSES: bool = True
