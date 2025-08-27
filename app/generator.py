# Copyright (C) 2022 Sergey Kovalevich <inndie@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import Optional
from app.definition import *

# generator: in the case of the groups counter or cardinality

class GeneratorBase(ABC):
    @abstractmethod
    def _generate_impl(self, schema: dict) -> None:
        pass

    def generate(self, schema: SchemaDefinition) -> None:
        ir = {}
        self._generate_impl(ir)
