# Copyright (C) 2025 R. Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

import unittest
from app.parser import *
from app.schema import *
from app.definition import *
from app.definition_helper import *
from app.helpers import *

class Testing_Definition(unittest.TestCase):

    # <ValidValue name="Trade" value="1" description="Trade"/>
    def test_get_valid_value_definition(self):
        valid_value = ValidValue(
            name="Trade",
            value=1,
            description="Trade")
        result = DefinitionHelper.get_valid_value_definition(valid_value)
        self.assertEqual(result.name, "Trade")
        self.assertEqual(result.value, 1)

    def test_get_data_type_definition(self):
        xml_ref = '\
<Model>\
    <DataTypes>\
        <DataType name="AlphaNumeric" type="String" rootType="String" package="eti_Cash" description="" range="A-Z,0-9,\x20" noValue="0x00"/>\
        <DataType name="floatDecimal7" type="floatDecimal" rootType="floatDecimal" package="eti_Cash" size="8" description="" minValue="-922337203685.4775807" maxValue="922337203685.4775807" precision="7" noValue="0x8000000000000000"/>\
        <DataType name="ApplID" type="int" rootType="int" numericID="1180" package="eti_Cash" size="1" description="" minValue="0" maxValue="11" noValue="0xFF">\
            <ValidValue name="Trade" value="1" description="Trade"/>\
            <ValidValue name="News" value="2" description="News"/>\
            <ValidValue name="Service_availability" value="3" description="Service Availability"/>\
            <ValidValue name="Session_data" value="4" description="Session Data"/>\
            <ValidValue name="Listener_data" value="5" description="Listener Data"/>\
            <ValidValue name="RiskControl" value="6" description="Risk Control"/>\
            <ValidValue name="TES_Maintenance" value="7" description="TES Maintenance"/>\
            <ValidValue name="TES_Trade" value="8" description="TES Trade"/>\
            <ValidValue name="SRQS_Maintenance" value="9" description="SRQS Maintenance"/>\
            <ValidValue name="Service_Availability_Market" value="10" description="Service Availability Market"/>\
            <ValidValue name="Specialist_Data" value="11" description="Specialist Data"/>\
        </DataType>\
    </DataTypes>\
</Model>\
'

        parser_result = Parser.from_string(xml_ref)
        data_types_dict = parser_result.get_data_types()

        result = UniqueKeysDict()
        for data_type in data_types_dict.values():
            result_data_definition = DefinitionHelper.get_data_type_definition(data_type)
            result[result_data_definition.name] = result_data_definition

        result_ApplID = result["ApplID"]
        self.assertEqual(result_ApplID.name , "ApplID")
        self.assertEqual(result_ApplID.type , "uint8")
        self.assertEqual(result_ApplID.numeric_id , "1180")
        self.assertEqual(result_ApplID.size_bytes , "1")
        self.assertEqual(result_ApplID.no_value , "0xFF")
        self.assertEqual(result_ApplID.precision , None)
        self.assertEqual(len(result_ApplID.valid_value_definition_by_name) , 11)
