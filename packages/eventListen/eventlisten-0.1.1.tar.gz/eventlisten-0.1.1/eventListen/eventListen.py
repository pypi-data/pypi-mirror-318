from typing import Callable
from copy import copy

from proto import proto

with proto("Events") as Events:
    @Events
    def new(self) -> None:
        self.obj = {}
        self.events = []
        self.priority = None
        return
    
    @Events
    def observe(self, callback: Callable[[], None]) -> Callable[[], None]:
        self.events.append({"name": callback.__name__, "callback": callback})
        return callback

    @Events
    def trigger(self, event: str, *args, **kwargs) -> None:
        for e in self.events:
            if e["name"] == event:
                e["callback"](*args, **kwargs)
        if self.priority:
            o = self.obj[self.priority]
            if event in o:
                o[event](*args, **kwargs)
        else:
            for obj in copy(self.obj):
                if not obj in self.obj: return
                o = self.obj[obj]
                if event in o:
                    o[event](*args, **kwargs)
        return 

    @Events
    def group(self, obj: object, events: dict) -> None:
        self.obj[obj] = events
        return

    @Events
    def stopObserving(self, obj: object) -> None:
        del self.obj[obj]
        return
    
    @Events
    def setPriority(self, obj: object) -> None:
        self.priority = obj if self.priority != obj else None
        return
