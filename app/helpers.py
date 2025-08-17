from __future__ import annotations

from collections import UserDict
from dataclasses import dataclass, field
from typing import Optional, Dict, Union

# Helper class to define unique type in the dictionary
class UniqueKeysDict(UserDict):
    def __setitem__(self, key, value):
        if key in self.data:
            raise Exception(f'duplicate key "{key}"')
        self.data[key] = value
        
# Helper class to define the data types read from the xml
@dataclass(frozen=True)
class PrimitiveDefinition:
    root_type: str = field(default_factory=str)
    primitive_size: Optional[int] = field(default=None)
    min_value: Optional[str] = field(default=None)

    def __eq__(self, another: PrimitiveDefinition):
        return (
            hasattr(another, 'root_type') and
            hasattr(another, 'primitive_size') and
            hasattr(another, 'min_value') and 
            self.root_type == another.root_type and
            self.primitive_size == another.primitive_size and
            self.min_value == another.min_value
        )

    def __hash__(self):
        return hash(self.root_type) and hash(self.primitive_size) and hash(self.min_value)