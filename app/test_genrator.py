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

    def test_make_group_definition_members(self):
        group_definition_member_name = 'Test_group'
        group_definition_member_usage = UsageDefinition.MANDATORY
        group_definition_member_usage_offset = 11
        group_definition_member_usage_offsetBase = 15
        group_definition_member_usage_cardinality = 20

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

        group_definition_member = GroupDataTypeDefinition(
            name = group_definition_member_name,
            usage = group_definition_member_usage,
            offset = group_definition_member_usage_offset,
            offsetBase = group_definition_member_usage_offsetBase,
            cardinality = group_definition_member_usage_cardinality,
            dataType = data_type_definition
        )

        result = GeneratorBase.make_group_definition_members(group_definition_member)
        self.assertEqual(result['name'], group_definition_member_name)
        self.assertEqual(result['usage'], str(group_definition_member_usage))
        self.assertEqual(result['offset'], group_definition_member_usage_offset)
        self.assertEqual(result['offsetBase'], group_definition_member_usage_offsetBase)
        self.assertEqual(result['cardinality'], group_definition_member_usage_cardinality)
        self.assertEqual(result['dataType'], data_type_definition_name)

    def test_make_group_definition_members_counter(self):
        group_definition_name = "Test"
        group_definition_counter = "Counter"

        # generate a group definition
        data_type_definition = DataTypDefinition(
            name = 'Test',
            type = 'double',
            numeric_id = 123,
            size_bytes = 3,
            no_value = '0xFF',
            precision = 5,
            valid_value_definition_by_name = {}
        )

        group_definition_member = GroupDataTypeDefinition(
            name = 'Test_group',
            usage = UsageDefinition.MANDATORY,
            offset = 11,
            offsetBase = 15,
            cardinality = 20,
            dataType = data_type_definition
        )

        members_definition = {}
        members_definition[group_definition_member.name] = group_definition_member

        group_definition = GroupDefinition(
            name = group_definition_name,
            counter = group_definition_counter,
            members = members_definition
        )

        result = GeneratorBase.make_group_definition(group_definition)

        self.assertEqual(result['name'], group_definition_name)
        self.assertEqual(result['counter'], group_definition_counter)
        self.assertEqual(len(result['members']), 1)

    def test_make_group_definition_members_cardinality(self):
        group_definition_name = "Test"
        group_definition_cardinality = 8

        # generate a group definition
        data_type_definition = DataTypDefinition(
            name = 'Test',
            type = 'double',
            numeric_id = 123,
            size_bytes = 3,
            no_value = '0xFF',
            precision = 5,
            valid_value_definition_by_name = {}
        )

        group_definition_member = GroupDataTypeDefinition(
            name = 'Test_group',
            usage = UsageDefinition.MANDATORY,
            offset = 11,
            offsetBase = 15,
            cardinality = 20,
            dataType = data_type_definition
        )

        members_definition = {}
        members_definition[group_definition_member.name] = group_definition_member

        group_definition = GroupDefinition(
            name = group_definition_name,
            counter = None,
            cardinality = group_definition_cardinality,
            members = members_definition
        )

        result = GeneratorBase.make_group_definition(group_definition)

        self.assertEqual(result['name'], group_definition_name)
        self.assertEqual(result['cardinality'], group_definition_cardinality)
        self.assertEqual(len(result['members']), 1)

    def test_make_message_definition_member(self):

        data_type_definition = DataTypDefinition(
            name = 'Test',
            type = 'double',
            numeric_id = 123,
            size_bytes = 3,
            no_value = '0xFF',
            precision = 5,
            valid_value_definition_by_name = {}
        )

        application_message_definition_member_name = "Test"
        application_message_definition_member_offset = 12
        application_message_definition_member_cardinality = 15
        application_message_definition_member_mandatory = UsageDefinition.MANDATORY

        application_message_definition_member = ApplicationMessageMemberDefinition(
            name = application_message_definition_member_name,
            offset = application_message_definition_member_offset,
            cardinality = application_message_definition_member_cardinality,
            usage = application_message_definition_member_mandatory,
            hidden = True,
            dataType = data_type_definition,
        )

        result = GeneratorBase.make_message_definition_member(application_message_definition_member)

        self.assertEqual(result['token'], 'field')
        self.assertEqual(result['name'], application_message_definition_member_name)
        self.assertEqual(result['offset'], application_message_definition_member_offset)
        self.assertEqual(result['cardinality'], application_message_definition_member_cardinality)
        self.assertEqual(result['usage'], str(application_message_definition_member_mandatory))
        self.assertEqual(result['dataType'], data_type_definition.name)

    def test_make_message_definition_group_counter(self):
        application_message_definition_group_name = "Test"
        application_message_definition_min_cardinality = 8

        # generate a group definition
        data_type_counter = DataTypDefinition(
            name = 'Test',
            type = 'double',
            numeric_id = 123,
            size_bytes = 3,
            no_value = '0xFF',
            precision = 5,
            valid_value_definition_by_name = {}
        )

        # generate a group definition
        data_type_definition = DataTypDefinition(
            name = 'Test',
            type = 'double',
            numeric_id = 123,
            size_bytes = 3,
            no_value = '0xFF',
            precision = 5,
            valid_value_definition_by_name = {}
        )

        group_definition_member = GroupDataTypeDefinition(
            name = 'Test_group',
            usage = UsageDefinition.MANDATORY,
            offset = 11,
            offsetBase = 15,
            cardinality = 20,
            dataType = data_type_definition
        )

        members_definition = {}
        members_definition[group_definition_member.name] = group_definition_member

        group_definition = GroupDefinition(
            name = "Test",
            counter = None,
            cardinality = 8,
            members = members_definition
        )

        application_message_definition_group = ApplicationMessageGroupDefinition(
            name = application_message_definition_group_name,
            counter = data_type_counter,
            min_cardinality = application_message_definition_min_cardinality,
            cardinality = None,
            groupType = group_definition
        )

        result = GeneratorBase.make_message_definition_group(application_message_definition_group)
        self.assertEqual(result['token'], 'group')
        self.assertEqual(result['name'], application_message_definition_group_name)
        self.assertEqual(result['group_name'], group_definition.name)
        self.assertEqual(result['min_cardinality'], application_message_definition_min_cardinality)
        self.assertEqual(result['counter'], data_type_counter.name)

    def test_make_message_definition_group_cardinality(self):
        application_message_definition_group_name = "Test"
        application_message_definition_min_cardinality = 8
        application_message_definition_cardinality = 4

        # generate a group definition
        data_type_definition = DataTypDefinition(
            name = 'Test',
            type = 'double',
            numeric_id = 123,
            size_bytes = 3,
            no_value = '0xFF',
            precision = 5,
            valid_value_definition_by_name = {}
        )

        group_definition_member = GroupDataTypeDefinition(
            name = 'Test_group',
            usage = UsageDefinition.MANDATORY,
            offset = 11,
            offsetBase = 15,
            cardinality = 20,
            dataType = data_type_definition
        )

        members_definition = {}
        members_definition[group_definition_member.name] = group_definition_member

        group_definition = GroupDefinition(
            name = "Test",
            counter = None,
            cardinality = 8,
            members = members_definition
        )

        application_message_definition_group = ApplicationMessageGroupDefinition(
            name = application_message_definition_group_name,
            counter = None,
            min_cardinality = application_message_definition_min_cardinality,
            cardinality = application_message_definition_cardinality,
            groupType = group_definition
        )

        result = GeneratorBase.make_message_definition_group(application_message_definition_group)
        self.assertEqual(result['token'], 'group')
        self.assertEqual(result['name'], application_message_definition_group_name)
        self.assertEqual(result['group_name'], group_definition.name)
        self.assertEqual(result['min_cardinality'], application_message_definition_min_cardinality)
        self.assertEqual(result['cardinality'], application_message_definition_cardinality)

    def test_make_application_definition(self):
        application_definition_name = "Test"
        application_definition_numeric_id = 123

        data_type_definition = DataTypDefinition(
            name = 'Test',
            type = 'double',
            numeric_id = 123,
            size_bytes = 3,
            no_value = '0xFF',
            precision = 5,
            valid_value_definition_by_name = {}
        )

        application_message_definition_member_name = "Test"
        application_message_definition_member_offset = 12
        application_message_definition_member_cardinality = 15
        application_message_definition_member_mandatory = UsageDefinition.MANDATORY

        application_message_definition_member = ApplicationMessageMemberDefinition(
            name = application_message_definition_member_name,
            offset = application_message_definition_member_offset,
            cardinality = application_message_definition_member_cardinality,
            usage = application_message_definition_member_mandatory,
            hidden = True,
            dataType = data_type_definition,
        )

        members_or_groups_dict = {}
        members_or_groups_dict[application_message_definition_member.name] = application_message_definition_member

        application_definition = ApplicationMessageDefinition(
            name = application_definition_name,
            numeric_id = application_definition_numeric_id,
            package = "test",
            members_or_groups = members_or_groups_dict
        )

        result = GeneratorBase.make_application_definition(application_definition)
        self.assertEqual(result['name'], application_definition_name)
        self.assertEqual(result['numeric_id'], application_definition_numeric_id)
        self.assertEqual(len(result['members']), 1)

        result_application_message_definition_member = result['members'][0]
        self.assertEqual(result_application_message_definition_member['token'], 'field')
        self.assertEqual(result_application_message_definition_member['name'], application_message_definition_member_name)
        self.assertEqual(result_application_message_definition_member['offset'], application_message_definition_member_offset)
        self.assertEqual(result_application_message_definition_member['cardinality'], application_message_definition_member_cardinality)
        self.assertEqual(result_application_message_definition_member['usage'], str(application_message_definition_member_mandatory))
        self.assertEqual(result_application_message_definition_member['dataType'], data_type_definition.name)
