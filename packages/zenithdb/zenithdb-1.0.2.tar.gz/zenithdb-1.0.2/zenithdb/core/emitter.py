from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, List, Any, Optional

@dataclass
class RealtimeEvent:
    operation: str
    timestamp: str
    document: dict
    collection: str
    old_document: Optional[dict] = None

class Emitter(ABC):
    def __init__(self, callback: Callable[[Any], None]):
        self.callback = callback
        self.subs: List[Callable] = []
        if callable(callback):
            self.subs.append(callback)
    
    def subscribe(self, callback: Callable[[Any], None]) -> None:
        if callable(callback):
            self.subs.append(callback)
    
    def unsubscribe(self, callback: Callable[[Any], None]) -> None:
        if callback in self.subs:
            self.subs.remove(callback)
    
    @abstractmethod
    def emit(self, data: Any) -> None:
        pass

class ConsoleEmitter(Emitter):
    def emit(self, data: Any) -> None:
        for sub in self.subs:
            sub(data)

# Usage
#def custom_handler(data):
    #print(f"Received: {data}")

#emitter = ConsoleEmitter(custom_handler)
#emitter.emit("Hello, World!")