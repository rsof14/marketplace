from abc import abstractmethod, ABC


class Currency(ABC):

    @abstractmethod
    def to_dollars(self):
        pass
