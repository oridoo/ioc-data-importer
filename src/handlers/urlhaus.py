from csv import reader
from urllib.request import urlopen
from typing import Iterator


class DataSource(object):
    """
    Data source for urlhaus.
    """

    def __init__(self) -> None:
        self.source_url = "https://urlhaus.abuse.ch/downloads/csv_recent/"
        self.source_name = "urlhaus"
        self.type = "url"

    def generator(self) -> Iterator[str]:
        with urlopen(self.source_url) as f:
            for row in reader(f.read().decode("utf-8").splitlines()):
                if row[0].startswith("#"):
                    continue
                yield row[2]
