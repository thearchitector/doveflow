from abc import ABC, abstractmethod
from typing import Any, final
from uuid import uuid4

from gevent.greenlet import Greenlet


class Processor(ABC, Greenlet):
    """
    A general model for an abstract Doveflow processor, based on a single greenlet.
    Processors are identified by their UUID, which is used for context management
    during redis (de)serialization.
    """

    def __init__(self, name: str, *args: Any, **kwargs: Any):
        self.name = name
        self.uuid = uuid4()

        super().__init__(self._run, *args, **kwargs)

    @final
    def _run(self, *args, **kwargs):
        return self.execute(*args, **kwargs)

    @abstractmethod
    def execute(self, *args: Any, **kwargs: Any):
        return
