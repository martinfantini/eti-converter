    # Copyright (C) 2025 R. Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

import unittest
from app.parser import *
from app.schema import *
from app.definition import *
from app.definition_helper import *
from app.helpers import *
from app.generator import *

class Testing_Generation(unittest.TestCase):

    def test_make_valid_value(self):
        valid_value_name = 'test'
        valid_value_value = 152

        valid_value_definition = ValidValueDefinition(
            name = valid_value_name,
            value= valid_value_value
        )

        result = GeneratorBase.make_valid_value(valid_value_definition)

        self.assertEqual(result['name'], valid_value_name)
        self.assertEqual(result['value'], valid_value_value)

    def test_make_data_type_definition_const(self):
        data_type_definition_name = 'Test'
        data_type_definition_type = 'double'
        data_type_definition_numeric_id = 123
        data_type_definition_size_bytes = 3
        data_type_definition_no_value = '0xFF'
        data_type_definition_precision = 5

        valid_value_name = 'test'
        valid_value_value = 152

        valid_value_definition = ValidValueDefinition(
            name = valid_value_name,
            value= valid_value_value
        )

        valid_value_definition_by_name_values = {}
        valid_value_definition_by_name_values[valid_value_definition.name] = valid_value_definition

        data_type_definition = DataTypDefinition(
            name = data_type_definition_name,
            type = data_type_definition_type,
            numeric_id = data_type_definition_numeric_id,
            size_bytes = data_type_definition_size_bytes,
            no_value = data_type_definition_no_value,
            precision = data_type_definition_precision,
            valid_value_definition_by_name = valid_value_definition_by_name_values
        )

        result = GeneratorBase.make_data_type_definition(data_type_definition)
        self.assertEqual(result['name'], data_type_definition_name)
        self.assertEqual(result['type'], data_type_definition_type)
        self.assertEqual(result['numeric_id'], data_type_definition_numeric_id)
        self.assertEqual(result['size_bytes'], data_type_definition_size_bytes)
        self.assertEqual(result['no_value'], data_type_definition_no_value)
        self.assertEqual(result['precision'], data_type_definition_precision)
        self.assertEqual(result['token'], 'const')
        enum_value_in_dict = result['enum_values']
        self.assertEqual(len(enum_value_in_dict), 1)
        enum_value_in_dict_first = enum_value_in_dict[0]
        self.assertEqual(enum_value_in_dict_first['name'], valid_value_name)
        self.assertEqual(enum_value_in_dict_first['value'], valid_value_value)

    def test_make_data_type_definition_data(self):
        data_type_definition_name = 'Test'
        data_type_definition_type = 'double'
        data_type_definition_numeric_id = 123
        data_type_definition_size_bytes = 3
        data_type_definition_no_value = '0xFF'
        data_type_definition_precision = 5

        valid_value_definition_by_name_values = {}

        data_type_definition = DataTypDefinition(
            name = data_type_definition_name,
            type = data_type_definition_type,
            numeric_id = data_type_definition_numeric_id,
            size_bytes = data_type_definition_size_bytes,
            no_value = data_type_definition_no_value,
            precision = data_type_definition_precision,
            valid_value_definition_by_name = valid_value_definition_by_name_values
        )

        result = GeneratorBase.make_data_type_definition(data_type_definition)
        self.assertEqual(result['name'], data_type_definition_name)
        self.assertEqual(result['type'], data_type_definition_type)
        self.assertEqual(result['numeric_id'], data_type_definition_numeric_id)
        self.assertEqual(result['size_bytes'], data_type_definition_size_bytes)
        self.assertEqual(result['no_value'], data_type_definition_no_value)
        self.assertEqual(result['precision'], data_type_definition_precision)
        self.assertEqual(result['token'], 'data')

    def test_make_data_type_definition_enum(self):
        data_type_definition_name = 'Test'
        data_type_definition_type = 'double'
        data_type_definition_numeric_id = 123
        data_type_definition_size_bytes = 3
        data_type_definition_no_value = '0xFF'
        data_type_definition_precision = 5

        valid_value_name = 'test'
        valid_value_value = 152

        valid_value_definition = ValidValueDefinition(
            name = valid_value_name,
            value= valid_value_value
        )

        valid_value_definition_by_name_values = {}
        valid_value_definition_by_name_values[valid_value_definition.name] = valid_value_definition

        valid_value_name_1 = 'test_1'
        valid_value_value_1 = 153

        valid_value_definition_1 = ValidValueDefinition(
            name = valid_value_name_1,
            value= valid_value_value_1
        )

        valid_value_definition_by_name_values[valid_value_definition_1.name] = valid_value_definition_1

        data_type_definition = DataTypDefinition(
            name = data_type_definition_name,
            type = data_type_definition_type,
            numeric_id = data_type_definition_numeric_id,
            size_bytes = data_type_definition_size_bytes,
            no_value = data_type_definition_no_value,
            precision = data_type_definition_precision,
            valid_value_definition_by_name = valid_value_definition_by_name_values
        )

        result = GeneratorBase.make_data_type_definition(data_type_definition)
        self.assertEqual(result['name'], data_type_definition_name)
        self.assertEqual(result['type'], data_type_definition_type)
        self.assertEqual(result['numeric_id'], data_type_definition_numeric_id)
        self.assertEqual(result['size_bytes'], data_type_definition_size_bytes)
        self.assertEqual(result['no_value'], data_type_definition_no_value)
        self.assertEqual(result['precision'], data_type_definition_precision)
        self.assertEqual(result['token'], 'enum')
        enum_value_in_dict = result['enum_values']
        self.assertEqual(len(enum_value_in_dict), 2)
        enum_value_in_dict_first = enum_value_in_dict[0]
        self.assertEqual(enum_value_in_dict_first['name'], valid_value_name)
        self.assertEqual(enum_value_in_dict_first['value'], valid_value_value)
        enum_value_in_dict_second = enum_value_in_dict[1]
        self.assertEqual(enum_value_in_dict_second['name'], valid_value_name_1)
        self.assertEqual(enum_value_in_dict_second['value'], valid_value_value_1)
