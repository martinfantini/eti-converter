# Copyright (C) 2025 R. Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Optional, Dict, Union

# Data Types
# <ValidValue name="Do_not_check" value="0" description="Do not check"/>
@dataclass(frozen=True)
class ValidValue:
    name: str = field(default_factory=str)
    value: int = field(default_factory=int)
    description: str = field(default_factory=str)

# <DataType name="ValueCheckTypeQuantity" type="int" rootType="int" numericID="25127" package="eti_Cash" size="1" description="" minValue="0" maxValue="1" noValue="0xFF">
@dataclass(frozen=True)
class DataType:
    name: str = field(default_factory=str)
    primitive_type: str = field(default_factory=str)
    root_type: str = field(default_factory=str)
    numeric_id: int = field(default=None)
    package: str = field(default_factory=str)
    primitive_size: Optional[int] = field(default=None)
    description: Optional[str] = field(default=None)
    min_value: Optional[str] = field(default=None)
    max_value: Optional[str] = field(default=None)
    range: Optional[str] = field(default=None)
    precision: Optional[int] = field(default=None)
    no_value: str = field(default=None)
    valid_value_by_name: Dict[str, ValidValue] = field(default_factory=dict)
    is_basic_type: bool = field(default_factory=bool)

# <Member name="MessageHeaderIn" type="MessageHeaderInComp" package="eti_Cash" cardinality="1" description=""/>
# <Member name="UnderlyingStipGrp" type="UnderlyingStipGrpComp" package="eti_Derivatives" minCardinality="0" cardinality="1" counter="NoUnderlyingStips" description=""/>
@dataclass(frozen=True)
class Structures_Member:
    name: str = field(default_factory=str)
    member_type: str = field(default_factory=str)
    package: str = field(default_factory=str)
    min_cardinality: Optional[int] = field(default=None)
    cardinality: int = field(default=1)
    counter: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)

# <Structure name="XetraEnLightUpdateNegotiationRequest" type="Message" numericID="10801" package="eti_Cash" description="">
@dataclass(frozen=True)
class Structures_Structure:
    name: str = field(default_factory=str)
    structure_type: str = field(default_factory=str)
    numeric_id: Optional[int] = field(default=None)
    package: str = field(default_factory=str)
    description: Optional[str] = field(default=None)
    members: Dict[str, Structures_Member] = field(default_factory=dict)

@dataclass(frozen=True)
class ApplicationMessage_Usage(enum.Enum):
    MANDATORY = 'mandatory'
    OPTIONAL = 'optional'
    UNUSED = 'unused'

# ApplicationMessage information
# <ApplicationMessage name="XetraEnLightQuotingStatusRequest" package="eti_Cash" type="XetraEnLightQuotingStatusRequest" numericID="10817" description="" functionalCategory="Selective Request for Quote Service " alias="Xetra EnLight Enter Quoting Status Request" service="Selective Request for Quote Service">
@dataclass(frozen=True)
class ApplicationMessage:
    name: str = field(default_factory=str)
    package: str = field(default_factory=str)
    application_message_type: str = field(default_factory=str)
    numeric_id: int = field(default=None)
    description: Optional[str] = field(default=None)
    functional_category: Optional[str] = field(default=None)
    alias: Optional[str] = field(default=None)
    service: Optional[str] = field(default=None)
    members_or_groups: Dict[str, Union[ApplicationMessage_Member, ApplicationMessage_Group]] = field(default_factory=dict)

# <Member name="MsgType" hidden="true" type="MsgType" package="eti_Cash" numericID="35" usage="unused" offset="0" cardinality="1" description="">
@dataclass(frozen=True)
class ApplicationMessage_Member:
    name: str = field(default_factory=str)
    hidden: bool = field(default_factory=bool)
    member_type: str = field(default_factory=str)
    package: str = field(default_factory=str)
    numeric_id: int = field(default=None)
    usage: ApplicationMessage_Usage = field(default=ApplicationMessage_Usage.OPTIONAL)
    offset: int = field(default=None)
    cardinality: int = field(default=1)
    description: str = field(default_factory=str)
    valid_value_by_name: Dict[str, ValidValue] = field(default_factory=dict)

# <Group name="SecurityStatusEventGrp" type="SecurityStatusEventGrpComp" package="eti_Cash" minCardinality="0" cardinality="2" counter="NoEvents" description="">
@dataclass(frozen=True)
class ApplicationMessage_Group:
    name: str = field(default_factory=str)
    group_type: str = field(default_factory=str)
    package: str = field(default_factory=str)
    min_cardinality: Optional[int] = field(default=None)
    cardinality: int = field(default=1)
    counter: str = field(default_factory=str)
    description: str = field(default_factory=str)
    members: Dict[str,ApplicationMessage_Member] = field(default_factory=dict)

# <Model name="eti_Cash" version="13.1" subVersion="C0002" buildNumber="131.430.2.ga-131004030-47">
@dataclass(frozen=True)
class Schema:
    name: str = field(default_factory=str)
    version: str = field(default_factory=str)
    sub_version: str = field(default_factory=str)
    build_number: str = field(default_factory=str)
    data_types: Dict[str, DataType] = field(default_factory=dict)
    structure: Dict[str, Structures_Structure] = field(default_factory=dict)
    application_messages: Dict[str, ApplicationMessage] = field(default_factory=dict)