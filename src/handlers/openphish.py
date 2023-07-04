from abc import ABC

from src.handlers import base_source
from urllib.request import urlopen


class OpenphishSource(base_source.BaseDataSource, ABC):
    """
    Data source for openphish.
    """
    def __init__(self) -> None:
        super().__init__()
        self.source_url = "https://openphish.com/feed.txt"
        self.source_name = "openphish"
        self.type = "url"

    def __iter__(self) -> "OpenphishSource":
        """
        Returns an iterable for the source.
        :return:
        """
        with urlopen(self.source_url) as f:
            for line in f.read().decode("utf-8").splitlines():
                yield line
