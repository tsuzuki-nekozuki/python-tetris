from abc import ABC, abstractmethod


class BaseScene(ABC):

    @abstractmethod
    def update(self, dt: float):
        pass

    @abstractmethod
    def render(self) -> any:
        pass

    @abstractmethod
    def handle_input(self, key: int):
        pass
