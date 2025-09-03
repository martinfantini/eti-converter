# Copyright (C) 2025 R. Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Optional, Dict, Union
from app.schema import ByteOrder

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

@dataclass(frozen=True)
class UsageDefinition(enum.Enum):
    MANDATORY = 'mandatory'
    OPTIONAL = 'optional'
    UNUSED = 'unused'

    def __eq__(self, other)-> bool:
        return self.__class__ is other.__class__ and other.value == self.value

@dataclass(frozen=True)
class ApplicationMessageDefinition:
    name: str = field(default_factory=str)
    numeric_id: int = field(default=None)
    package: str = field(default_factory=str)
    size: int = field(default=0)
    members_or_groups: Dict[str, Union[ApplicationMessageMemberDefinition, ApplicationMessageGroupDefinition]] = field(default_factory=dict)

# <Member name="MsgType" hidden="true" type="MsgType" package="eti_Cash" numericID="35" usage="unused" offset="0" cardinality="1" description="">
@dataclass(frozen=True)
class ApplicationMessageMemberDefinition:
    name: str = field(default_factory=str)
    offset: int = field(default=None)
    cardinality: int = field(default=1)
    usage: UsageDefinition = field(default=UsageDefinition.OPTIONAL)
    hidden: bool = field(default_factory=bool)
    size: int = field(default=0)
    dataType: DataTypDefinition = field(default=None)

# <Group name="SecurityStatusEventGrp" type="SecurityStatusEventGrpComp" package="eti_Cash" minCardinality="0" cardinality="2" counter="NoEvents" description="">  
@dataclass(frozen=True)
class ApplicationMessageGroupDefinition:
    name: str = field(default_factory=str)
    counter: DataTypDefinition = field(default=None)
    min_cardinality: Optional[int] = field(default=None)
    cardinality: int = field(default=1)
    size: int = field(default=0)
    groupType: GroupDefinition = field(default=None)

@dataclass(frozen=True)
class GroupDataTypeDefinition:
    name: str = field(default_factory=str)
    usage: UsageDefinition = field(default=UsageDefinition.OPTIONAL)
    offset: int = field(default=None)
    offsetBase: int = field(default=None)
    cardinality: int = field(default=1)
    dataType: DataTypDefinition = field(default=None)

@dataclass(frozen=True)
class GroupDefinition:
    name: str = field(default_factory=str)
    counter: str = field(default_factory=str)
    cardinality: int = field(default=0)
    size: int = field(default=0)
    members: Dict[str, GroupDataTypeDefinition] = field(default_factory=dict)

@dataclass(frozen=True)
class SchemaDefinition:
    dataType: Dict[str, DataTypDefinition] = field(default_factory=dict)
    groupDefinition: Dict[str, GroupDefinition] = field(default_factory=dict)
    messageDefinition: Dict[str, ApplicationMessageDefinition] = field(default_factory=dict)
    version: str = field(default_factory=str)
    sub_version: str = field(default_factory=str)
    build_number: str = field(default_factory=str)
    byte_order: ByteOrder = field(default=ByteOrder.LITTLE_ENDIAN)
    name: str = field(default_factory=str)
    initial_message_fields: list[str] = field(default_factory=list)
