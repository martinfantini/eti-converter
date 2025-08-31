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
        ir['name'] = schema.name
        ir['version'] = schema.version
        ir['sub_version'] = schema.version
        ir['build_number'] = schema.build_number
        if schema.byte_order == ByteOrder.LITTLE_ENDIAN:
            ir['byte_order'] = 'littleEndian'
        else:
            ir['byte_order'] = 'bigEndian'

        # Data types definition
        ir['types'] = []
        for data_type_definition in schema.dataType.values():
            ir['types'].append(GeneratorBase.make_data_type_definition(data_type_definition))

        # group definition
        ir['groups'] = []
        for group_definition in schema.groupDefinition.values():
            ir['groups'].append(GeneratorBase.make_group_definition(group_definition))

        # messages definition
        ir['messages'] = []
        for message_definition in schema.messageDefinition.values():
            ir['messages'].append(GeneratorBase.make_message_definition(message_definition))

        self._generate_impl(ir)

    @staticmethod
    def make_valid_value(valid_value_definition: ValidValueDefinition) -> dict:
        return {
            'name': valid_value_definition.name,
            'value': valid_value_definition.value,
        }

    @staticmethod
    def make_data_type_definition(data_type_definition: DataTypDefinition) -> dict:
        result_dict = {
            'name': data_type_definition.name,
            'type': data_type_definition.type,
            'numeric_id': data_type_definition.numeric_id,
            'size_bytes': data_type_definition.size_bytes,
            'no_value': data_type_definition.no_value,
        }

        if data_type_definition.precision != None:
            result_dict['precision'] = data_type_definition.precision

        enum_values = []
        for values in data_type_definition.valid_value_definition_by_name.values():
            enum_values.append(GeneratorBase.make_valid_value(values))

        if len(data_type_definition.valid_value_definition_by_name) == 0:
            result_dict['token'] = 'data'
        elif len(data_type_definition.valid_value_definition_by_name) == 1:
            result_dict['token'] = 'const'
            result_dict['enum_values'] = enum_values
        elif len(data_type_definition.valid_value_definition_by_name) > 1:
            result_dict['token'] = 'enum'
            result_dict['enum_values'] = enum_values
        return result_dict

    @staticmethod
    def make_group_definition_members(group_definition_member: GroupDataTypeDefinition) -> dict:
        result_dict = {
            'name': group_definition_member.name,
            'usage': str(group_definition_member.usage),
        }

        if group_definition_member.offset != None:
            result_dict['offset'] = group_definition_member.offset

        if group_definition_member.offsetBase != None:
            result_dict['offsetBase'] = group_definition_member.offsetBase

        if group_definition_member.cardinality != 0:
            result_dict['cardinality'] = group_definition_member.cardinality

        if group_definition_member.dataType != None:
            result_dict['dataType'] = group_definition_member.dataType.name

        return result_dict

    @staticmethod
    def make_group_definition(group_definition: GroupDefinition) -> dict:
        result_dict = {
            'name': group_definition.name,
        }

        if group_definition.counter != None:
            result_dict['counter'] = group_definition.counter
        elif group_definition.cardinality != 0:
            result_dict['cardinality'] = group_definition.cardinality
        else:
            raise Exception(f'Error in group definition "{group_definition.name}", it has no counter and cardinality is 0')

        member_values = []
        for group_definition in group_definition.members.values():
            member_values.append(GeneratorBase.make_group_definition_members(group_definition))
        result_dict['members'] = member_values
        
        return result_dict

    @staticmethod
    def make_message_definition_member(application_message_definition_member: ApplicationMessageMemberDefinition) -> dict:
        return {
            'token': 'field',
            'name': application_message_definition_member.name,
            'offset': application_message_definition_member.offset,
            'cardinality': application_message_definition_member.cardinality,
            'usage': str(application_message_definition_member.usage),
            'dataType': application_message_definition_member.dataType.name,
        }

    @staticmethod
    def make_message_definition_group(application_message_definition_group: ApplicationMessageGroupDefinition) -> dict:
        result_dict = {
            'token': 'group',
            'name': application_message_definition_group.name,
            'group_name': application_message_definition_group.groupType.name,
            'min_cardinality': application_message_definition_group.min_cardinality,
        }

        if application_message_definition_group.counter != None:
            result_dict['counter'] = application_message_definition_group.counter.name
        elif application_message_definition_group.cardinality != 0:
            result_dict['cardinality'] = application_message_definition_group.cardinality
        else:
            raise Exception(f'Error in group definition "{application_message_definition_group.name}", it has no counter and cardinality is 0')

        return result_dict

    @staticmethod
    def make_group_definition(application_definition: ApplicationMessageDefinition) -> dict:
        result_dict = {
            'name': application_definition.name,
            'numeric_id': application_definition.numeric_id,
        }

        members_values = []
        for member_in_message in application_definition.members_or_groups.values():
            if isinstance(member_in_message, ApplicationMessageMemberDefinition):
                members_values.append(GeneratorBase.make_message_definition_member(member_in_message))
            elif isinstance(member_in_message, ApplicationMessageGroupDefinition):
                members_values.append(GeneratorBase.make_message_definition_group(member_in_message))
            else:
                raise Exception(f'Error in member definition "{member_in_message.name}"')

        result_dict['members'] = members_values
        return result_dict
