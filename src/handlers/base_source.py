from abc import abstractmethod, ABCMeta


class BaseDataSource(metaclass=ABCMeta):
    """
    Base class for all data sources.
    """
    def __init__(self) -> None:
        super().__init__()
        self.source_url: str
        self.source_name: str
        self.source_id: int
        self.type: str  # ["url", "ip"]

    @abstractmethod
    def __iter__(self) -> "BaseDataSource":
        """
        Returns an iterator for the source.
        :return:
        """
        return self
