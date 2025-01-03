__all__ = ("Signal",)

from asyncio import TaskGroup, iscoroutinefunction, to_thread
from typing import Any

from frozenlist import FrozenList


class Signal(FrozenList):
    """Coroutine-based signal implementation.

    To connect a callback to a signal, use any list method.

    Signals are fired using the send() for sync code and aio_send for coroutine,
    which takes named arguments.
    """

    __slots__ = ("_owner",)

    def __init__(self, owner):
        super().__init__()
        self._owner = owner

    def __repr__(self):
        return "<Signal owner={}, frozen={}, {!r}>".format(
            self._owner, self.frozen, list(self)
        )

    def send(self, *args: Any, **kwargs: Any) -> None:
        """
        Sends data to all registered receivers. It will skip async receivers.
        """
        if not self.frozen:
            raise RuntimeError("Cannot send non-frozen signal.")

        for receiver in self:
            if not iscoroutinefunction(receiver):
                receiver(*args, **kwargs)

    async def aio_send(self, *args: Any, **kwargs: Any) -> None:
        """
        Sends data to all registered receivers.
        """
        if not self.frozen:
            raise RuntimeError("Cannot send non-frozen signal.")

        async with TaskGroup() as tg:
            for receiver in self:
                if iscoroutinefunction(receiver):
                    tg.create_task(receiver(*args, **kwargs))
                else:
                    tg.create_task(to_thread(receiver, *args, **kwargs))
