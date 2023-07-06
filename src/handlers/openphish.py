from urllib.request import urlopen
from typing import Iterator


class DataSource(object):
    """
    Data source for openphish.
    """

    def __init__(self) -> None:
        self.source_url = "https://openphish.com/feed.txt"
        self.source_name = "openphish"
        self.type = "url"

    def generator(self) -> Iterator[str]:
        with urlopen(self.source_url) as f:
            for line in f.read().decode("utf-8").splitlines():
                yield line
