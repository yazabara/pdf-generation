import logging
import uuid
from abc import ABCMeta, abstractmethod


class DocComponent(metaclass=ABCMeta):
    """
    Abstract document component
    """

    def __init__(self) -> None:
        super().__init__()
        self.id = uuid.uuid4()
        self.logger = logging.getLogger("Component." + self.component_type())
        self.logger.info('Component {} with id {} created '.format(self.component_type(), self.id))

    @abstractmethod
    def component_type(self):
        """
        Method return component type
        :return: component type
        """
        pass
