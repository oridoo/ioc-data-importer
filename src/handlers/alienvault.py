from urllib.request import urlopen
from typing import Iterator


class DataSource(object):
    """
    Data source for alienvault.
    """

    def __init__(self) -> None:
        self.source_url = "http://reputation.alienvault.com/reputation.data"
        self.source_name = "alienvault"
        self.type = "ip"

    def generator(self) -> Iterator[str]:
        with urlopen(self.source_url) as f:
            for line in f.read().decode("utf-8").splitlines():
                yield line.split("#")[0]
