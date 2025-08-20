# Copyright (C) 2025 R. Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Optional, Dict, Union

@dataclass(frozen=True)
class ValidValueDefinition:
    name: str = field(default_factory=str)
    value: int = field(default_factory=int)

@dataclass(frozen=True)
class DataTypDefinition:
    name: str = field(default_factory=str)
    type: str = field(default_factory=str)
    numeric_id: Optional[int] = field(default=None)
    size_bytes: Optional[int] = field(default=None)
    no_value: Optional[str] = field(default=None)
    precision: Optional[int] = field(default=None)
    valid_value_definition_by_name: Dict[str, ValidValueDefinition] = field(default_factory=dict)
