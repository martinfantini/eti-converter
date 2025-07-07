# Copyright (C) 2025 R. Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from __future__ import annotations
import xml.etree.ElementTree as ET
from typing import Optional, Dict, Union, Tuple
from collections import UserDict
from schema import *
from xml_helper import *

class UniqueKeysDict(UserDict):
    def __setitem__(self, key, value):
        if key in self.data:
            raise Exception(f'duplicate key "{key}"')
        self.data[key] = value

class Parser:

    def __init__(self, root: ET.Element) -> None:
        self.root = root

    @staticmethod
    def from_file(path: str) -> Parser:
        root = load_xml_from_file(path)
        return Parser(root)

    @staticmethod
    def from_string(string_xml: str) -> Parser:
        root = load_xml_from_string(string_xml)
        return Parser(root)

    def parse_valid_value_from_node(self, node: ET.Element) -> ValidValue:
        return ValidValue(
            name = attr(node, 'name'),
            value = attr(node, 'value'),
            description = attr(node, 'description', None),
        )

    def parse_data_type_from_node(self, node: ET.Element) -> DataType:
        name_str = attr(node, 'name')
        primitive_type_str = attr(node, 'type')
        root_type_str = attr(node, 'rootType')
        numeric_id_int = attr(node, 'numericID', None)
        package_str = attr(node, 'package')
        primitive_size_int = attr(node, 'size', None)
        description_str = attr(node, 'description', None)
        min_value_str = attr(node, 'minValue', None)
        max_value_str = attr(node, 'maxValue', None)
        no_value_str = attr(node, 'noValue', None)
        range_str = attr(node, 'range', None)
        precision_int = attr(node, 'precision', None)

        """ define primiteive data type set """
        PRIMITIVE_DATA_TYPE_LIST = [ "AlphaNumeric", "Counter", "CurrencyType", "Freetext", "ISIN", "LocalMktDate", "LocalMonthYearCod", "PriceType", "Qty", "SeqNum", "String", "UTCTimestamp", "char", "data", "float", "floatDecimal", "floatDecimal4", "floatDecimal6", "floatDecimal7", "int" ]
        is_basic_type_bool = False
        if name_str in PRIMITIVE_DATA_TYPE_LIST:
            is_basic_type_bool = True

        valid_value_by_name_dict = UniqueKeysDict()
        for child in node:
            if child.tag == 'ValidValue':
                valid_value = self.parse_valid_value_from_node(child)
                valid_value_by_name_dict[valid_value.name] = valid_value
            else:
                raise Exception(f'unexpected tag "{child.tag}" inside enum "{name_str}"')

        return DataType(
            name = name_str,
            primitive_type = primitive_type_str,
            root_type = root_type_str,
            numeric_id = numeric_id_int,
            package = package_str,
            primitive_size = primitive_size_int,
            description = description_str,
            min_value = min_value_str,
            max_value = max_value_str,
            no_value = no_value_str,
            precision = precision_int,
            range = range_str,
            valid_value_by_name = valid_value_by_name_dict,
            is_basic_type = is_basic_type_bool
        )

    def parse_structure_member_from_node(self, node: ET.Element, members: Dict[str, Structures_Member]) -> Structures_Member:
        name_str = attr(node, 'name')
        member_type_str = attr(node, 'type')
        package_str = attr(node, 'package')
        min_cardinality_int = attr(node, 'minCardinality', None)
        cardinality_int = attr(node, 'cardinality')
        counter_str = attr(node, 'counter', None)
        if counter_str != None:
            if members[counter_str] == None:
                raise Exception(f'unexpected count "{counter_str}" inside member "{name_str}"')
        description_str = attr(node, 'description', None)

        return Structures_Member(
            name = name_str,
            member_type = member_type_str,
            package = package_str,
            min_cardinality = min_cardinality_int,
            cardinality = cardinality_int,
            counter = counter_str,
            description = description_str
        )

    def parse_structure_structure_from_node(self, node: ET.Element) -> Structures_Structure:
        name_str = attr(node, 'name')
        structure_type = attr(node, 'type')
        numeric_id_int = attr(node, 'numericID', None)
        package_str = attr(node, 'package')
        description_str = attr(node, 'description', None)
        members_dict = UniqueKeysDict()

        for child in node:
            if child.tag == 'Member':
                member_value = self.parse_structure_member_from_node(child, members_dict)
                members_dict[member_value.name] = member_value
            else:
                raise Exception(f'unexpected tag "{child.tag}" inside structure "{name_str}"')

        return Structures_Structure(
            name = name_str,
            structure_type = structure_type,
            numeric_id = numeric_id_int,
            package = package_str,
            description = description_str,
            members = members_dict
        )

    def get_data_type_ref(self, data_type_name: str, data_types: Dict[str, DataType]) -> DataType:
        return data_types[data_type_name]
    
    def get_valid_value_ref_in_data_type(self, data_type: DataType, valid_value_name: str) -> ValidValue:
        found_valid_value = data_type.valid_value_by_name[valid_value_name]
        if found_valid_value == None:
            raise Exception(f'valid value name  "{valid_value_name}" in data type  "{data_type.name}" is not valid')
        return found_valid_value

    def is_valid_data_type_ref(self, data_type_name: str, data_types: Dict[str, DataType]) -> bool:
        return data_types[data_type_name] != None

    def parse_application_message_member_from_node(self, node: ET.Element, data_types: Dict[str, DataType]) -> ApplicationMessage_Member:
        name_str = attr(node, 'name')
        hidden_bool = attr(node, 'hidden', False)
        member_type_str = attr(node, 'type')
        if member_type_str != None and not self.is_valid_data_type_ref(member_type_str, data_types):
            raise Exception(f'member "{name_str}" has a type "{member_type_str}" is not valid')
        data_type_ref = self.get_data_type_ref(member_type_str, data_types)
        
        package_str = attr(node, 'package')
        numeric_id_int = attr(node, 'numericID')
        usage_enum = attr(node, 'usage', ApplicationMessage_Usage.MANDATORY, cast=ApplicationMessage_Usage)
        offset_int = attr(node, 'offset')
        cardinality_int = attr(node, 'cardinality')
        description_str = attr(node, 'description', None)
        valid_value_dict = UniqueKeysDict()

        for child in node:
            if child.tag == 'ValidValue':
                valid_value = self.parse_valid_value_from_node(child)
                found_valid_value = self.get_valid_value_ref_in_data_type(data_type_ref, valid_value.name)
                if valid_value.name != found_valid_value.name or valid_value.value != found_valid_value.value:
                    raise Exception(f'valid values "{valid_value.name}" has a valid "{valid_value.value}" value')
                valid_value_dict[valid_value.name] = valid_value
            else:
                raise Exception(f'unexpected tag "{child.tag}" inside member "{name_str}"')

        return ApplicationMessage_Member(
            name = name_str,
            hidden = hidden_bool,
            member_type = member_type_str,
            package = package_str,
            numeric_id = numeric_id_int,
            usage = usage_enum,
            offset = offset_int,
            cardinality = cardinality_int,
            description = description_str,
            valid_value_by_name=valid_value_dict
        )

    def parse_application_message_group_from_node(self, node: ET.Element, fields: Dict[str, Union[ApplicationMessage_Member, ApplicationMessage_Group]], data_types: Dict[str, DataType] ) -> ApplicationMessage_Group:
        name_str = attr(node, 'name')
        group_type_str = attr(node, 'type')
        package_str = attr(node, 'package')
        min_cardinality_int = attr(node, 'minCardinality', None)
        cardinality_int = attr(node, 'cardinality', None)
        description_str = attr(node, 'description', None)
        counter_str = attr(node, 'counter', None)
        if counter_str != None and not counter_str in fields:
            raise Exception(f'unexpected field name "{counter_str}" in group "{name_str}"')

        members_dict = UniqueKeysDict()
        for child in node:
            if child.tag == 'Member':
                member_value = self.parse_application_message_member_from_node(child, data_types)
                members_dict[member_value.name] = member_value
            else:
                raise Exception(f'unexpected tag "{child.tag}" inside "{name_str}" group')

        return ApplicationMessage_Group(
            name = name_str,
            group_type = group_type_str,
            package = package_str,
            min_cardinality = min_cardinality_int,
            cardinality = cardinality_int,
            counter = counter_str,
            description = description_str,
            members = members_dict
        )

    def parse_application_message_from_node(self, node: ET.Element, data_types: Dict[str, DataType]) -> ApplicationMessage:
        name_str = attr(node, 'name')
        package_str = attr(node, 'package')
        application_message_type_str = attr(node, 'type')
        numeric_id_int = attr(node, 'numericID')
        description_str = attr(node, 'description', None)
        functional_category_str = attr(node, 'functionalCategory')
        alias_str = attr(node, 'alias')
        service_str = attr(node, 'service', None)
        members_or_groups_dict = UniqueKeysDict()

        for child in node:
            if child.tag == 'Member':
                member_value = self.parse_application_message_member_from_node(child, data_types)
                members_or_groups_dict[member_value.name] = member_value
            elif child.tag == 'Group':
                group_value = self.parse_application_message_group_from_node(child, members_or_groups_dict, data_types)
                members_or_groups_dict[group_value.name] = group_value
            else:
                raise Exception(f'unexpected tag "{child.tag}" inside "{name_str}" application message')
        
        return ApplicationMessage(
            name = name_str,
            package = package_str,
            application_message_type = application_message_type_str,
            numeric_id = numeric_id_int,
            description = description_str,
            functional_category = functional_category_str,
            alias = alias_str,
            service = service_str,
            members_or_groups = members_or_groups_dict
        )

    def get_data_types(self) -> Dict[str, DataType]:
        data_types_by_name = UniqueKeysDict() 
        data_types_by_id = UniqueKeysDict()
        for child_data_type in self.root.findall("DataTypes/DataType"):
            data_type_obj = self.parse_data_type_from_node(child_data_type)
            data_types_by_name[data_type_obj.name] = data_type_obj
            data_types_by_id[data_type_obj.name] = data_type_obj
        return data_types_by_name

    def get_structures(self) -> Dict[str, Structures_Structure]:
        structure_by_name = UniqueKeysDict()
        for structure_node in self.root.findall("Structures/Structure"):
            structure_obj = self.parse_structure_structure_from_node(structure_node)
            structure_by_name[structure_obj.name] = structure_obj
        return structure_by_name

    def get_application_messages(self, data_types: Dict[str, DataType]) -> Dict[str, ApplicationMessage]:
        message_by_name = UniqueKeysDict()
        message_by_id = UniqueKeysDict()
        for child_application_message in self.root.findall("ApplicationMessages/ApplicationMessage"):
            message = self.parse_application_message_from_node(child_application_message, data_types)
            message_by_name[message.name] = message
            message_by_id[message.numeric_id] = message
        return message_by_name

    def get_schema(self) -> Schema:
        if self.root.tag != "Model":
            raise Exception(f'not found Model tag at the beggining')
        model_node  = self.root
        name_str = attr(model_node, 'name')
        version_str = attr(model_node, 'version')
        sub_version_str = attr(model_node, 'subVersion')
        build_number_str = attr(model_node, 'buildNumber')

        data_types_dic = self.get_data_types()
        structures_dict = self.get_structures()
        application_messages_dict = self.get_application_messages(data_types_dic)

        return Schema(
            name = name_str,
            version = version_str,
            sub_version = sub_version_str,
            build_number = build_number_str,
            data_types = data_types_dic,
            structure = structures_dict,
            application_messages = application_messages_dict
        )
