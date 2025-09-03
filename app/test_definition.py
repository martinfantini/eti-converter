# Copyright (C) 2025 R. Martin Fantini <martin.fantini@gmail.com>
# This file may be distributed under the terms of the GNU GPLv3 license

import unittest
from app.parser import *
from app.schema import *
from app.definition import *
from app.definition_helper import *
from app.helpers import *

class Testing_Definition(unittest.TestCase):

    XML_REF_SHORT = '\
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

    XML_REF_LONG = '\
<Model>\
    <ApplicationMessages>\
        <ApplicationMessage name="BroadcastErrorNotification" package="eti_Cash" type="BroadcastErrorNotification" numericID="10032" description="" functionalCategory="Other" alias="Gap Fill">\
            <Member name="MsgType" hidden="true" type="MsgType" package="eti_Cash" numericID="35" usage="unused" offset="0" cardinality="1" description="">\
                <ValidValue name="ApplicationMessageReport" value="BY" description="Application Message Report"/>\
            </Member>\
            <Group name="MessageHeaderOut" type="MessageHeaderOutComp" package="eti_Cash" cardinality="1" description="">\
                <Member name="BodyLen" type="BodyLen" package="eti_Cash" numericID="9" usage="mandatory" offset="0" cardinality="1" description=""/>\
                <Member name="TemplateID" type="TemplateID" package="eti_Cash" numericID="28500" usage="mandatory" offset="4" cardinality="1" description=""/>\
                <Member name="Pad2" type="Pad2" package="eti_Cash" numericID="39020" usage="unused" offset="6" cardinality="1" description=""/>\
            </Group>\
            <Group name="NotifHeader" type="NotifHeaderComp" package="eti_Cash" cardinality="1" description="">\
                <Member name="SendingTime" type="SendingTime" package="eti_Cash" numericID="52" usage="mandatory" offset="8" cardinality="1" description=""/>\
            </Group>\
            <Member name="ApplIDStatus" type="ApplIDStatus" package="eti_Cash" numericID="28724" usage="mandatory" offset="16" cardinality="1" description="">\
                <ValidValue name="Outbound_conversion_error" value="105" description="Error converting response or broadcast"/>\
            </Member>\
            <Member name="RefApplSubID" type="RefApplSubID" package="eti_Cash" numericID="28728" usage="optional" offset="20" cardinality="1" description=""/>\
            <Member name="VarTextLen" type="VarTextLen" package="eti_Cash" numericID="30354" usage="mandatory" offset="24" cardinality="1" description=""/>\
            <Member name="RefApplID" type="RefApplID" package="eti_Cash" numericID="1355" usage="mandatory" offset="26" cardinality="1" description="">\
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
            </Member>\
            <Member name="SessionStatus" type="SessionStatus" package="eti_Cash" numericID="1409" usage="mandatory" offset="27" cardinality="1" description="">\
                <ValidValue name="Active" value="0" description="Session active"/>\
                <ValidValue name="Logout" value="4" description="Session logout complete"/>\
            </Member>\
            <Member name="VarText" type="VarText" package="eti_Cash" numericID="30355" usage="mandatory" offset="28" cardinality="1" counter="VarTextLen" description=""/>\
            <Member name="NoLegOnbooks" type="NoLegOnbooks" package="eti_Derivatives" numericID="28555" usage="mandatory" offset="43" cardinality="1" description=""/>\
            <Group name="InstrmtLegGrp" type="InstrmtLegGrpComp" package="eti_Derivatives" minCardinality="0" cardinality="144" counter="NoLegOnbooks" description="">\
                <Member name="LegSecurityID" type="LegSecurityID" package="eti_Derivatives" numericID="602" usage="mandatory" offset="72" cardinality="1" description=""/>\
                <Member name="LegPrice" type="LegPrice" package="eti_Derivatives" numericID="566" usage="optional" offset="80" cardinality="1" description=""/>\
            </Group>\
        </ApplicationMessage>\
    </ApplicationMessages>\
    <DataTypes>\
        <DataType name="SessionStatus" type="int" rootType="int" numericID="1409" package="eti_Cash" size="1" description="" minValue="0" maxValue="4" noValue="0xFF">\
            <ValidValue name="Active" value="0" description="Session active"/>\
            <ValidValue name="Logout" value="4" description="Session logout complete"/>\
        </DataType>\
        <DataType name="VarText" type="String" rootType="String" numericID="30355" package="eti_Cash" size="2000" variableSize="true" counter="VarTextLen" description="" range="\\x09,\\x0A,\\x0D,\\x20-\\x7B,\\x7D,\\x7E"/>\
        <DataType name="RefApplID" type="int" rootType="int" numericID="1355" package="eti_Cash" size="1" description="" minValue="0" maxValue="11" noValue="0xFF">\
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
        <DataType name="ApplIDStatus" type="int" rootType="int" numericID="28724" package="eti_Cash" size="4" description="" minValue="0" maxValue="4294967294" noValue="0xFFFFFFFF" nonStrict="true">\
            <ValidValue name="Outbound_conversion_error" value="105" description="Error converting response or broadcast"/>\
        </DataType>\
        <DataType name="RefApplSubID" type="int" rootType="int" numericID="28728" package="eti_Cash" size="4" description="" minValue="0" maxValue="4294967294" noValue="0xFFFFFFFF"/>\
        <DataType name="VarTextLen" type="Counter" rootType="int" numericID="30354" package="eti_Cash" size="2" description="" minValue="0" maxValue="2000" noValue="0xFFFF"/>\
        <DataType name="TemplateID" type="int" rootType="int" numericID="28500" package="eti_Cash" size="2" description="" minValue="0" maxValue="65534" noValue="0xFFFF"/>\
        <DataType name="SendingTime" type="UTCTimestamp" rootType="int" numericID="52" package="eti_Cash" size="8" description="" minValue="0" maxValue="18446744073709551614" noValue="0xFFFFFFFFFFFFFFFF"/>\
        <DataType name="Pad2" type="String" rootType="String" numericID="39020" package="eti_Cash" size="2" description="" range="\\x01-\\x7E" noValue="0x00"/>\
        <DataType name="MsgType" type="String" rootType="String" numericID="35" package="eti_Cash" size="3" description="" range="\\x01-\\x7E" noValue="0x00">\
            <ValidValue name="Heartbeat" value="0" description="Heartbeat"/>\
            <ValidValue name="TestRequest" value="1" description="Test Request"/>\
            <ValidValue name="Reject" value="3" description="Reject"/>\
            <ValidValue name="Logout" value="5" description="Logout"/>\
            <ValidValue name="ExecutionReport" value="8" description="Execution Report"/>\
            <ValidValue name="Logon" value="A" description="Logon"/>\
            <ValidValue name="TradeCaptureReport" value="AE" description="Trade Capture Report"/>\
            <ValidValue name="TradeCaptureReportAck" value="AR" description="Trade Capture Report Ack"/>\
            <ValidValue name="QuoteRequestReject" value="AG" description="Quote Request Reject"/>\
            <ValidValue name="TradeMatchReport" value="DC" description="Trade Match Report"/>\
            <ValidValue name="TradeMatchReportAck" value="DD" description="Trade Match Report Ack"/>\
            <ValidValue name="News" value="B" description="News"/>\
            <ValidValue name="UserRequest" value="BE" description="User Request"/>\
            <ValidValue name="UserResponse" value="BF" description="User Response"/>\
            <ValidValue name="ApplicationMessageRequest" value="BW" description="Application Message Request"/>\
            <ValidValue name="ApplicationMessageRequestAck" value="BX" description="Application Message Request Ack"/>\
            <ValidValue name="ApplicationMessageReport" value="BY" description="Application Message Report"/>\
            <ValidValue name="OrderMassActionReport" value="BZ" description="Order Mass Action Report"/>\
            <ValidValue name="OrderMassActionRequest" value="CA" description="Order Mass Action Request"/>\
            <ValidValue name="UserNotification" value="CB" description="User Notification"/>\
            <ValidValue name="PartyRiskLimitsUpdateReport" value="CR" description="Party Risk Limits Update Report"/>\
            <ValidValue name="PartyRiskLimitsRequest" value="CL" description="Party Risk Limits Request"/>\
            <ValidValue name="PartyRiskLimitsDefinitionRequest" value="CS" description="Party Risk Limits Definition Request"/>\
            <ValidValue name="PartyRiskLimitsDefinitionRequestAck" value="CT" description="Party Risk Limits Definition Request Ack"/>\
            <ValidValue name="PartyRiskLimitsReport" value="CM" description="Party Risk Limits Report"/>\
            <ValidValue name="PartyEntitlementsUpdateReport" value="CZ" description="Party Entitlements Update Report"/>\
            <ValidValue name="NewOrderSingle" value="D" description="New Order Single"/>\
            <ValidValue name="OrderCancelRequest" value="F" description="Order Cancel Request"/>\
            <ValidValue name="OrderCancelReplaceRequest" value="G" description="Order Cancel Replace Request"/>\
            <ValidValue name="QuoteRequest" value="R" description="Quote Request"/>\
            <ValidValue name="MarketDataSnapshotFullRefresh" value="W" description="Market Data Snapshot Full Refresh"/>\
            <ValidValue name="QuoteCancel" value="Z" description="Quote Cancel"/>\
            <ValidValue name="MassQuoteAcknowledgement" value="b" description="Mass Quote Acknowledgement"/>\
            <ValidValue name="TradingSessionStatus" value="h" description="Trading Session Status"/>\
            <ValidValue name="MassQuote" value="i" description="Mass Quote"/>\
            <ValidValue name="Quote" value="S" description="Quote"/>\
            <ValidValue name="QuoteAck" value="CW" description="Quote Acknowledgment"/>\
            <ValidValue name="QuoteStatusRequest" value="a" description="Quote Status Request"/>\
            <ValidValue name="QuoteStatusReport" value="AI" description="Quote Status Report"/>\
            <ValidValue name="QuoteResponse" value="AJ" description="Quote Response"/>\
            <ValidValue name="RequestAcknowledge" value="U1" description="Request Acknowledge"/>\
            <ValidValue name="SessionDetailsListRequest" value="U5" description="Session Details List Request"/>\
            <ValidValue name="SessionDetailsListResponse" value="U6" description="Session Details List Response"/>\
            <ValidValue name="QuoteExecutionReport" value="U8" description="Quote Execution Report"/>\
            <ValidValue name="MMParameterDefinitionRequest" value="U14" description="MMParameter Definition Request"/>\
            <ValidValue name="CrossRequest" value="DS" description="Cross Request"/>\
            <ValidValue name="CrossRequestAck" value="DT" description="Cross Request Ack"/>\
            <ValidValue name="MMParameterRequest" value="U17" description="MMParameter Request"/>\
            <ValidValue name="MMParameterResponse" value="U18" description="MMParameter Response"/>\
            <ValidValue name="SecurityStatusDefinitionRequest" value="U27" description="Security Status Definition Request"/>\
            <ValidValue name="SecurityStatus" value="f" description="Security Status"/>\
            <ValidValue name="PartyDetailsListRequest" value="CF" description="Party Detail List Request"/>\
            <ValidValue name="PartyDetailsListReport" value="CG" description="Party Detail List Request"/>\
            <ValidValue name="TradeEnrichmentListRequest" value="U7" description="Trade Enrichment List Request"/>\
            <ValidValue name="TradeEnrichmentListReport" value="U9" description="Trade Enrichment List Report"/>\
            <ValidValue name="PartyActionReport" value="DI" description="Party Action Report"/>\
            <ValidValue name="MarketDataInstrument" value="U23" description="Market Data Instrument"/>\
            <ValidValue name="NewOrderRequest" value="U32" description="Combination of NewOrderSingle and NewOrderMultileg"/>\
            <ValidValue name="ModifyOrderRequest" value="U33" description="Combination of OrderCancelReplaceRequest and MultilegOrderCancelReplace"/>\
        </DataType>\
        <DataType name="BodyLen" type="int" rootType="int" numericID="9" package="eti_Cash" size="4" description="" minValue="0" maxValue="4294967294" noValue="0xFFFFFFFF"/>\
        <DataType name="NoLegOnbooks" type="Counter" rootType="int" numericID="28555" package="eti_Derivatives" size="1" description="" minValue="0" maxValue="144" noValue="0xFF"/>\
        <DataType name="LegSecurityID" type="int" rootType="int" numericID="602" package="eti_Derivatives" size="8" description="" minValue="-9223372036854775807" maxValue="9223372036854775807" noValue="0x8000000000000000"/>\
        <DataType name="LegPrice" type="PriceType" rootType="floatDecimal" numericID="566" package="eti_Derivatives" size="8" description="" minValue="-92233720368.54775807" maxValue="92233720368.54775807" precision="8" noValue="0x8000000000000000"/>\
    </DataTypes>\
</Model>\
'

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

        parser_result = Parser.from_string(Testing_Definition.XML_REF_SHORT)
        data_types_dict = parser_result.get_data_types()

        result = DefinitionHelper.get_data_type_definition_dict(data_types_dict)

        result_ApplID = result["ApplID"]
        self.assertEqual(result_ApplID.name , "ApplID")
        self.assertEqual(result_ApplID.type , "uint8")
        self.assertEqual(result_ApplID.numeric_id , 1180)
        self.assertEqual(result_ApplID.size_bytes , 1)
        self.assertEqual(result_ApplID.no_value , "0xFF")
        self.assertEqual(result_ApplID.precision , None)
        self.assertEqual(len(result_ApplID.valid_value_definition_by_name) , 11)

    def test_get_group_definition_dict(self):

        parser_result = Parser.from_string(Testing_Definition.XML_REF_LONG)
        data_types_dict = parser_result.get_data_types()
        application_messages_dict = parser_result.get_application_messages(data_types_dict)
        result_dataType_definition = DefinitionHelper.get_data_type_definition_dict(data_types_dict)
        result_group_definition_dict = DefinitionHelper.get_group_definition_dict(application_messages_dict, result_dataType_definition)

        result_group_definition_InstrmtLegGrp = result_group_definition_dict["InstrmtLegGrp"]
        self.assertEqual(result_group_definition_InstrmtLegGrp.name, "InstrmtLegGrp")
        self.assertEqual(result_group_definition_InstrmtLegGrp.counter, 'NoLegOnbooks')
        self.assertEqual(result_group_definition_InstrmtLegGrp.cardinality, '144')
        self.assertEqual(len(result_group_definition_InstrmtLegGrp.members), 2)

        result_group_definition_MessageHeaderOut = result_group_definition_dict["MessageHeaderOut"]
        self.assertEqual(result_group_definition_MessageHeaderOut.name, "MessageHeaderOut")
        self.assertEqual(result_group_definition_MessageHeaderOut.counter, None)
        self.assertEqual(result_group_definition_MessageHeaderOut.cardinality, '1')
        self.assertEqual(len(result_group_definition_MessageHeaderOut.members), 3)

    def test_get_message_definition_dict(self):
        parser_result = Parser.from_string((Testing_Definition.XML_REF_LONG))
        data_types_dict = parser_result.get_data_types()
        application_messages_dict = parser_result.get_application_messages(data_types_dict)
        result_dataType_definition = DefinitionHelper.get_data_type_definition_dict(data_types_dict)
        result_group_definition_dict = DefinitionHelper.get_group_definition_dict(application_messages_dict, result_dataType_definition)
        result_message_definition = DefinitionHelper.get_message_definition_dict(application_messages_dict, result_dataType_definition, result_group_definition_dict)

        self.assertEqual(len(result_message_definition), 1)

        result_message_definition_BroadcastErrorNotification = result_message_definition["BroadcastErrorNotification"]
        self.assertEqual(result_message_definition_BroadcastErrorNotification.numeric_id, '10032')
        self.assertEqual(result_message_definition_BroadcastErrorNotification.name, "BroadcastErrorNotification")
        self.assertEqual(result_message_definition_BroadcastErrorNotification.package, "eti_Cash")
        self.assertEqual(len(result_message_definition_BroadcastErrorNotification.members_or_groups), 11)

    def test_get_definition_eti_Cash(self):
        parser_result = Parser.from_file("resources/eti_Cash.xml")
        schema_result = parser_result.get_schema(ByteOrder.BIG_ENDIAN, None, "BodyLen,TemplateID".split(','))
        schema_definition_result = DefinitionHelper.get_schema_definition(schema_result)
        
        groupDefinition_MessageHeaderIn = schema_definition_result.groupDefinition["MessageHeaderIn"]
        self.assertEqual(groupDefinition_MessageHeaderIn.size_bytes, 16)

        groupDefinition_RequestHeader = schema_definition_result.groupDefinition["RequestHeader"]
        self.assertEqual(groupDefinition_RequestHeader.size_bytes, 8)

        message_definition_RetransmitMEMessageRequest = schema_definition_result.messageDefinition["RetransmitMEMessageRequest"]
        self.assertEqual(message_definition_RetransmitMEMessageRequest.size_bytes, 64)

    def test_get_definition_eti_Derivatives(self):
        parser_result = Parser.from_file("resources/eti_Derivatives.xml")
        schema_result = parser_result.get_schema(ByteOrder.BIG_ENDIAN, None, "BodyLen,TemplateID".split(','))
        schema_definition_result = DefinitionHelper.get_schema_definition(schema_result)
        message_definition_RetransmitMEMessageRequest = schema_definition_result.messageDefinition["RetransmitMEMessageRequest"]
        self.assertEqual(message_definition_RetransmitMEMessageRequest.size_bytes, 64)