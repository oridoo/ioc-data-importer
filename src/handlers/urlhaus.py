from abc import ABC

from src.handlers import base_source
from urllib.request import urlopen
from csv import reader


class UrlhausSource(base_source.BaseDataSource, ABC):
    """
    Data source for urlhaus.
    """
    def __init__(self) -> None:
        super().__init__()
        self.source_url = "https://urlhaus.abuse.ch/downloads/csv_recent/"
        self.source_name = "urlhaus"
        self.type = "url"

    def __iter__(self) -> "UrlhausSource":
        """
        Returns an iterable for the source.
        :return:
        """
        with urlopen(self.source_url) as f:
            for row in reader(f.read().decode("utf-8").splitlines()):
                if row[0].startswith("#"):
                    continue
                yield row[2]
