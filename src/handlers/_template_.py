from typing import Iterator


class DataSource(object):
    """
    Data source template.
    """

    def __init__(self) -> None:
        self.source_url: str
        self.source_name: str
        self.source_id: int  # set by database
        self.type: str  # ["url", "ip"]

    def generator(self) -> Iterator[str]:
        """
        A generator that yields the data source items.
        :return:
        """
        yield None
