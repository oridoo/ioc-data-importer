from abc import ABC

from src.handlers import base_source
from urllib.request import urlopen


class AlienvaultSource(base_source.BaseDataSource, ABC):
    """
    Data source for alienvault.
    """
    def __init__(self) -> None:
        super().__init__()
        self.source_url = "http://reputation.alienvault.com/reputation.data"
        self.source_name = "alienvault"
        self.type = "ip"

    def __iter__(self) -> "AlienvaultSource":
        """
        Returns an iterable for the source.
        :return:
        """
        with urlopen(self.source_url) as f:
            for line in f.read().decode("utf-8").splitlines():
                yield line.split("#")[0]
