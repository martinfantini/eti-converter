# Copyright (C) 2025 Roberto Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

from typing import Required
from typing import Dict, Union
from app.schema import *
from app.definition import *
from app.helpers import *

class DefinitionHelper:

    """ define primiteive data type set """
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
        PrimitiveDefinition('float', '8', None): 'double',
        PrimitiveDefinition('floatDecimal', '8', '-922337203685.4775807'): 'double',
        PrimitiveDefinition('floatDecimal4', '8', None): 'double',
        PrimitiveDefinition('floatDecimal6', '8', None): 'double',
        PrimitiveDefinition('floatDecimal7', '8', None): 'double',
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

        type_definition = DefinitionHelper.PRIMITIVE_TYPE_BY_DEFINITION[PrimitiveDefinition(parsed_value.primitive_type, parsed_value.primitive_size, parsed_value.min_value)]
        if  type_definition == None:
            raise Exception(f'Undefined type: root type: "{parsed_value.root_type}", primitive size: "{parsed_value.primitive_type}" and min value: "{parsed_value.min_value}"')

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
