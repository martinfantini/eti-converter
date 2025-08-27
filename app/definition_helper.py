# Copyright (C) 2025 Roberto Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from typing import Required
from typing import Dict, Union
from app.schema import *
from app.definition import *
from app.helpers import *

class DefinitionHelper:

    """ define primitive data type set """
    PRIMITIVE_DATA_TYPE_LIST = [ 
                                "AlphaNumeric",
                                "Counter",
                                "CurrencyType",
                                "Freetext",
                                "ISIN",
                                "LocalMktDate", 
                                "LocalMonthYearCod",
                                "PriceType",
                                "Qty",
                                "SeqNum",
                                "String",
                                "UTCTimestamp",
                                "char",
                                "data",
                                "float",
                                "floatDecimal",
                                "floatDecimal4",
                                "floatDecimal6",
                                "floatDecimal7",
                                "int"
                            ]

    """ define special cases for searching none with the other types """
    PRIMITIVE_TYPE_SEARCH_WITH_NONE = [
                                    "AlphaNumeric",
                                    "String",
                                    "floatDecimal",
                                    "floatDecimal4",
                                    "floatDecimal6",
                                    "floatDecimal7",
                                    "float"
                            ]

    """ define primiteive data type conversion """
    PRIMITIVE_TYPE_BY_DEFINITION = UniqueKeysDict({
        PrimitiveDefinition('AlphaNumeric', None, None): 'char',
        PrimitiveDefinition('Counter', '1', '0'): 'uint8',
        PrimitiveDefinition('Counter', '1', None): 'int8',
        PrimitiveDefinition('Counter', '2', '0'): 'uint16',
        PrimitiveDefinition('Counter', '2', None): 'int16',
        PrimitiveDefinition('Counter', '4', '0'): 'uint32',
        PrimitiveDefinition('Counter', '4', None): 'int32',
        PrimitiveDefinition('Counter', '8', '0'): 'uint64',
        PrimitiveDefinition('Counter', '8', None): 'int64',
        PrimitiveDefinition('CurrencyType', None, None): 'char',
        PrimitiveDefinition('Freetext', None, None): 'char',
        PrimitiveDefinition('ISIN', None, None): 'char',
        PrimitiveDefinition('LocalMktDate', '4', '0'): 'uint32',
        PrimitiveDefinition('LocalMonthYearCod', '4', '0'): 'uint32',
        PrimitiveDefinition('PriceType', '8', '0'): 'double',
        PrimitiveDefinition('Qty', '8', '0'): 'double',
        PrimitiveDefinition('SeqNum', '8', '0'): 'uint64',
        PrimitiveDefinition('String', None, None): 'string',
        PrimitiveDefinition('UTCTimestamp', '8', '0'): 'uint64',
        PrimitiveDefinition('char', None, None): 'char',
        PrimitiveDefinition('data', None, None): 'char',
        PrimitiveDefinition('float', None, None): 'double',
        PrimitiveDefinition('floatDecimal', None, None): 'double',
        PrimitiveDefinition('floatDecimal4', None, None): 'double',
        PrimitiveDefinition('floatDecimal6', None, None): 'double',
        PrimitiveDefinition('floatDecimal7', None, None): 'double',
        PrimitiveDefinition('int', '1', '0'): 'uint8',
        PrimitiveDefinition('int', '1', None): 'int8',
        PrimitiveDefinition('int', '2', '0'): 'uint16',
        PrimitiveDefinition('int', '2', None): 'int16',
        PrimitiveDefinition('int', '4', '0'): 'uint32',
        PrimitiveDefinition('int', '4', None): 'int32',
        PrimitiveDefinition('int', '8', '0'): 'uint64',
        PrimitiveDefinition('int', '8', None): 'int64',
    })

    @staticmethod
    def get_valid_value_definition(parsed_value: ValidValue) -> ValidValueDefinition:
        return ValidValueDefinition(
            name = parsed_value.name,
            value = parsed_value.value)

    @staticmethod
    def get_data_type_definition(parsed_value: DataType) -> DataTypDefinition:
        name_definition = parsed_value.name
        numeric_id_definition = parsed_value.numeric_id
        size_bytes_definition = parsed_value.primitive_size
        no_value_definition = parsed_value.no_value

        if not parsed_value.root_type in DefinitionHelper.PRIMITIVE_DATA_TYPE_LIST:
            raise Exception(f'Undefined root type "{parsed_value.root_type}"')

        # Special search cases: This will be a search with none value
        if parsed_value.root_type in DefinitionHelper.PRIMITIVE_TYPE_SEARCH_WITH_NONE:
            type_definition = DefinitionHelper.PRIMITIVE_TYPE_BY_DEFINITION.get(PrimitiveDefinition(parsed_value.root_type, None, None))
        else:
            type_definition = DefinitionHelper.PRIMITIVE_TYPE_BY_DEFINITION.get(PrimitiveDefinition(parsed_value.root_type, parsed_value.primitive_size, parsed_value.min_value))

        if  type_definition == None:
            type_definition = DefinitionHelper.PRIMITIVE_TYPE_BY_DEFINITION.get(PrimitiveDefinition(parsed_value.root_type, parsed_value.primitive_size,None))
            if  type_definition == None:
                raise Exception(f'Undefined type: "{parsed_value.name}" root type: "{parsed_value.root_type}", primitive size: "{parsed_value.primitive_size}" and min value: "{parsed_value.min_value}"')

        precision_definition = parsed_value.precision

        if type_definition == 'double' and precision_definition == None:
            raise Exception(f'Error in definition "{parsed_value.name}" of double without precision')

        valid_value_definition_by_name_dict = UniqueKeysDict()
        for parsed_valid_value in parsed_value.valid_value_by_name.values():
            result = DefinitionHelper.get_valid_value_definition(parsed_valid_value)
            valid_value_definition_by_name_dict[result.name] = result

        return DataTypDefinition(
            name = name_definition,
            type = type_definition,
            numeric_id = numeric_id_definition,
            size_bytes = size_bytes_definition,
            no_value = no_value_definition,
            precision = precision_definition,
            valid_value_definition_by_name = valid_value_definition_by_name_dict
        )

    @staticmethod
    def get_data_type_definition_dict(data_types: Dict[str, DataType]) -> Dict[str, DataTypDefinition]:
        dataTypeDefinition_dict = UniqueKeysDict()
        for data_type in data_types.values():
            result = DefinitionHelper.get_data_type_definition(data_type)
            dataTypeDefinition_dict[result.name] = result
        return dataTypeDefinition_dict

    @staticmethod
    def convert_usage(usage_application: ApplicationMessage_Usage) -> UsageDefinition:
        usage_result = UsageDefinition.OPTIONAL
        if usage_application == ApplicationMessage_Usage.OPTIONAL:
            usage_result = UsageDefinition.OPTIONAL
        elif usage_application == ApplicationMessage_Usage.MANDATORY:
            usage_result = UsageDefinition.MANDATORY
        elif usage_application == ApplicationMessage_Usage.OPTIONAL:
            usage_result = UsageDefinition.OPTIONAL
        return usage_result

    @staticmethod
    def get_group_data_type_definition(parsed_application_member: ApplicationMessage_Member, dataType_definition: Dict[str, DataTypDefinition]) -> GroupDataTypeDefinition:
        usage_result = DefinitionHelper.convert_usage(parsed_application_member.usage)
        result_data_type_definition = dataType_definition[parsed_application_member.name]
        if result_data_type_definition == None:
            raise Exception(f'Error in definition "{parsed_application_member.name}" is not defined in data type dictionary')

        return GroupDataTypeDefinition(
            name = parsed_application_member.name,
            usage = usage_result,
            offset = parsed_application_member.offset,
            offsetBase = parsed_application_member.offset_base,
            cardinality = parsed_application_member.cardinality,
            dataType = result_data_type_definition
        )

    @staticmethod
    def get_group_definition(parsed_group: ApplicationMessage_Group, dataType_definition: Dict[str, DataTypDefinition]) -> GroupDefinition:
        members_dict = UniqueKeysDict()
        for member in parsed_group.members.values():
            result_member =  DefinitionHelper.get_group_data_type_definition(member, dataType_definition)
            members_dict[result_member.name] = result_member

        return GroupDefinition(
            name = parsed_group.name,
            counter = parsed_group.counter,
            cardinality = parsed_group.cardinality,
            members = members_dict,
        )

    @staticmethod
    def get_group_definition_dict(parsed_application_messages: Dict[str, ApplicationMessage], dataType_definition: Dict[str, DataTypDefinition]) -> Dict[str, GroupDefinition]:
        groupDefinition_dict = UniqueKeysDict()
        for parsed_application_message in parsed_application_messages.values():
            for parsed_application_message_members in parsed_application_message.members_or_groups.values():
                if isinstance(parsed_application_message_members, ApplicationMessage_Group):
                    result = DefinitionHelper.get_group_definition(parsed_application_message_members, dataType_definition)
                    if groupDefinition_dict.get(result.name) == None:
                        groupDefinition_dict[result.name] = result
        return groupDefinition_dict

    @staticmethod
    def get_application_message_member_definition(parsed_member: ApplicationMessage_Member, dataType_definition: Dict[str, DataTypDefinition]) -> ApplicationMessageMemberDefinition:
        usage_result = DefinitionHelper.convert_usage(parsed_member.usage)
        result_data_type_definition = dataType_definition[parsed_member.name]
        if result_data_type_definition == None:
            raise Exception(f'Error in definition "{parsed_member.name}" is not defined in data type dictionary')

        return ApplicationMessageMemberDefinition(
            name = parsed_member.name,
            offset = parsed_member.offset,
            cardinality = parsed_member.cardinality,
            hidden = parsed_member.hidden,
            dataType = result_data_type_definition,
            usage = usage_result,
        )

    @staticmethod
    def get_application_message_group_definition(parsed_group: ApplicationMessage_Group, dataType_definition: Dict[str, DataTypDefinition], groupType_definition: Dict[str, GroupDefinition]) -> ApplicationMessageGroupDefinition:
        if not parsed_group.counter and parsed_group.cardinality == 0:
            raise Exception(f'Error in definition "{parsed_group.name}" has empty counter and not cardinality')

        counter_data_type = None
        if parsed_group.counter:
            counter_data_type = dataType_definition[parsed_group.counter]
            if counter_data_type == None:
                raise Exception(f'Error in definition "{parsed_group.counter}" is not defined in data type dictionary')

        group_definition = groupType_definition[parsed_group.name]
        if group_definition == None:
            raise Exception(f'Error in definition "{parsed_group.name}" is not defined in group type dictionary')

        return ApplicationMessageGroupDefinition(
            name = parsed_group.name,
            counter = counter_data_type,
            min_cardinality = parsed_group.min_cardinality,
            cardinality = parsed_group.cardinality,
            groupType = group_definition
        )

    @staticmethod
    def get_message_definition(parsed_message: ApplicationMessage, dataType_definition: Dict[str, DataTypDefinition], groupType_definition: Dict[str, GroupDefinition]) -> ApplicationMessageDefinition:
        members_or_groups_dict = UniqueKeysDict()
        for parsed_application_message_members in parsed_message.members_or_groups.values():
            if isinstance(parsed_application_message_members, ApplicationMessage_Member):
                result =  DefinitionHelper.get_application_message_member_definition(parsed_application_message_members, dataType_definition)
                members_or_groups_dict[result.name] = result
            elif isinstance(parsed_application_message_members, ApplicationMessage_Group):
                result =  DefinitionHelper.get_application_message_group_definition(parsed_application_message_members, dataType_definition, groupType_definition)
                members_or_groups_dict[result.name] = result
            else:
                raise Exception(f'Error in internal type "{parsed_application_message_members.name}" is not a group or member')

        return ApplicationMessageDefinition(
            name = parsed_message.name,
            numeric_id = parsed_message.numeric_id,
            package = parsed_message.package,
            members_or_groups = members_or_groups_dict,
        )

    @staticmethod
    def get_message_definition_dict(parsed_application_messages: Dict[str, ApplicationMessage], dataType_definition: Dict[str, DataTypDefinition], groupType_definition: Dict[str, GroupDefinition]) -> Dict[str, ApplicationMessageDefinition]:
        messageDefinition_dict = UniqueKeysDict()
        for parsed_application_message in parsed_application_messages.values():
            result = DefinitionHelper.get_message_definition(parsed_application_message, dataType_definition, groupType_definition)
            messageDefinition_dict[result.name] = result
        return messageDefinition_dict

    @staticmethod
    def get_schema_definition(parsed_schema: Schema) -> SchemaDefinition:
        dataTypDict = DefinitionHelper.get_data_type_definition_dict(parsed_schema.data_types)
        groupDefinitionDict = DefinitionHelper.get_group_definition_dict(parsed_schema.application_messages, dataTypDict)
        messageDefinitionDict = DefinitionHelper.get_message_definition_dict(parsed_schema.application_messages, dataTypDict, groupDefinitionDict)
        return SchemaDefinition(
            dataType = dataTypDict,
            groupDefinition = groupDefinitionDict,
            messageDefinition = messageDefinitionDict,
            version = parsed_schema.version,
            sub_version = parsed_schema.sub_version,
            build_number = parsed_schema.build_number,
            byte_order = parsed_schema.byte_order,
        )
