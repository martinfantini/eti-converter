import unittest
from parser import Parser
from schema import *

class Testing_Parser(unittest.TestCase):

    def test_DataType(self):
        xml_ref = '\
<Model>\
    <DataTypes>\
        <DataType name="AlphaNumeric" type="String" rootType="String" package="eti_Cash" description="" range="A-Z,0-9,\x20" noValue="0x00"/> \
        <DataType name="floatDecimal7" type="floatDecimal" rootType="floatDecimal" package="eti_Cash" size="8" description="" minValue="-922337203685.4775807" maxValue="922337203685.4775807" precision="7" noValue="0x8000000000000000"/> \
    </DataTypes>\
</Model>\
'

        parser_result = Parser.from_string(xml_ref)
        data_types_dict = parser_result.get_data_types()

        # Test AlphaNumeric case
        data_type_AlphaNumeric = data_types_dict["AlphaNumeric"]
        self.assertEqual(data_type_AlphaNumeric.name, "AlphaNumeric")
        self.assertEqual(data_type_AlphaNumeric.primitive_type, "String")
        self.assertEqual(data_type_AlphaNumeric.root_type, "String")
        self.assertEqual(data_type_AlphaNumeric.package, "eti_Cash")
        self.assertEqual(data_type_AlphaNumeric.numeric_id, None)
        self.assertEqual(data_type_AlphaNumeric.primitive_size, None)
        self.assertEqual(data_type_AlphaNumeric.description, '')
        self.assertEqual(data_type_AlphaNumeric.min_value, None)
        self.assertEqual(data_type_AlphaNumeric.max_value, None)
        self.assertEqual(data_type_AlphaNumeric.precision, None)
        self.assertEqual(data_type_AlphaNumeric.range, "A-Z,0-9,\x20")
        self.assertEqual(data_type_AlphaNumeric.no_value, "0x00")

        # Test floatDecimal7 case
        data_type_floatDecimal7 = data_types_dict["floatDecimal7"]
        self.assertEqual(data_type_floatDecimal7.name, "floatDecimal7")
        self.assertEqual(data_type_floatDecimal7.primitive_type, "floatDecimal")
        self.assertEqual(data_type_floatDecimal7.root_type, "floatDecimal")
        self.assertEqual(data_type_floatDecimal7.package, "eti_Cash")
        self.assertEqual(data_type_floatDecimal7.numeric_id, None)
        self.assertEqual(data_type_floatDecimal7.primitive_size, '8')
        self.assertEqual(data_type_floatDecimal7.description, '')
        self.assertEqual(data_type_floatDecimal7.min_value, "-922337203685.4775807")
        self.assertEqual(data_type_floatDecimal7.max_value, "922337203685.4775807")
        self.assertEqual(data_type_floatDecimal7.precision, '7')
        self.assertEqual(data_type_floatDecimal7.no_value, "0x8000000000000000")

    def test_DataType_with_ValidValue(self):
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

        # Test ApplID
        data_type_ApplID = data_types_dict["ApplID"]
        self.assertEqual(data_type_ApplID.name, "ApplID")
        self.assertEqual(data_type_ApplID.primitive_type, "int")
        self.assertEqual(data_type_ApplID.root_type, "int")
        self.assertEqual(data_type_ApplID.package, "eti_Cash")
        self.assertEqual(data_type_ApplID.numeric_id, '1180')
        self.assertEqual(data_type_ApplID.primitive_size, '1')
        self.assertEqual(data_type_ApplID.description, '')
        self.assertEqual(data_type_ApplID.min_value, '0')
        self.assertEqual(data_type_ApplID.max_value, '11')
        self.assertEqual(data_type_ApplID.precision, None)
        self.assertEqual(data_type_ApplID.range, None)
        self.assertEqual(data_type_ApplID.no_value, "0xFF")

        valid_value = data_type_ApplID.valid_value_by_name
        first_valid_value = list(valid_value.values())[0]

        self.assertEqual(first_valid_value.name , "Trade")
        self.assertEqual(first_valid_value.value , '1')
        self.assertEqual(first_valid_value.description , "Trade")

        find_by_name = valid_value["News"]

        self.assertEqual(find_by_name.name , "News")
        self.assertEqual(find_by_name.value , '2')
        self.assertEqual(find_by_name.description , "News")

    def test_Structure(self):
        xml_ref = '\
<Model>\
    <Structures>\
        <Structure name="XetraEnLightStatusBroadcast" type="Message" numericID="10814" package="eti_Cash" description="">\
            <Member name="MessageHeaderOut" type="MessageHeaderOutComp" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="RBCHeader" type="RBCHeaderComp" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="TradeDate" type="TradeDate" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="TradSesEvent" type="TradSesEvent" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="Pad3" type="Pad3" package="eti_Cash" cardinality="1" description=""/>\
        </Structure>\
        <Structure name="BroadcastErrorNotification" type="Message" numericID="10032" package="eti_Cash" description="">\
            <Member name="MessageHeaderOut" type="MessageHeaderOutComp" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="NotifHeader" type="NotifHeaderComp" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="ApplIDStatus" type="ApplIDStatus" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="RefApplSubID" type="RefApplSubID" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="VarTextLen" type="VarTextLen" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="RefApplID" type="RefApplID" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="SessionStatus" type="SessionStatus" package="eti_Cash" cardinality="1" description=""/>\
            <Member name="VarText" type="VarText" package="eti_Cash" cardinality="1" counter="VarTextLen" description=""/>\
        </Structure>\
    </Structures>\
</Model>\
'

        parser_result = Parser.from_string(xml_ref)
        structures_dict = parser_result.get_structures()

        structure_XetraEnLightStatusBroadcast = structures_dict["XetraEnLightStatusBroadcast"]
        self.assertEqual(structure_XetraEnLightStatusBroadcast.name, "XetraEnLightStatusBroadcast")
        self.assertEqual(structure_XetraEnLightStatusBroadcast.structure_type, "Message")
        self.assertEqual(structure_XetraEnLightStatusBroadcast.numeric_id, '10814')
        self.assertEqual(structure_XetraEnLightStatusBroadcast.package, "eti_Cash")
        self.assertEqual(structure_XetraEnLightStatusBroadcast.description, "")

        structure_members = structure_XetraEnLightStatusBroadcast.members
        structure_member_MHO = structure_members['MessageHeaderOut']
        
        self.assertEqual(structure_member_MHO.name, "MessageHeaderOut")
        self.assertEqual(structure_member_MHO.member_type, "MessageHeaderOutComp")
        self.assertEqual(structure_member_MHO.package, "eti_Cash")
        self.assertEqual(structure_member_MHO.min_cardinality, None)
        self.assertEqual(structure_member_MHO.cardinality, '1')
        self.assertEqual(structure_member_MHO.counter, None)
        self.assertEqual(structure_member_MHO.description, "")

        structure_BEN = structures_dict["BroadcastErrorNotification"]
        self.assertEqual(structure_BEN.name, "BroadcastErrorNotification")
        self.assertEqual(structure_BEN.structure_type, "Message")
        self.assertEqual(structure_BEN.numeric_id, '10032')
        self.assertEqual(structure_BEN.package, "eti_Cash")
        self.assertEqual(structure_BEN.description, "")

        last_valid_value = list(structure_BEN.members.values())[7]
        self.assertEqual(last_valid_value.name, "VarText")
        self.assertEqual(last_valid_value.member_type, "VarText")
        self.assertEqual(last_valid_value.package, "eti_Cash")
        self.assertEqual(last_valid_value.min_cardinality, None)
        self.assertEqual(last_valid_value.cardinality, '1')
        self.assertEqual(last_valid_value.counter, "VarTextLen")
        self.assertEqual(structure_member_MHO.description, "")

    def test_application_message(self):
        xml_ref = '\
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
    </DataTypes>\
</Model>\
'

        parser_result = Parser.from_string(xml_ref)
        data_types_dict = parser_result.get_data_types()
        application_messages_dict = parser_result.get_application_messages(data_types_dict)

        application_messages_BEN = application_messages_dict["BroadcastErrorNotification"]
        self.assertEqual(application_messages_BEN.name, "BroadcastErrorNotification")
        self.assertEqual(application_messages_BEN.package, "eti_Cash")
        self.assertEqual(application_messages_BEN.application_message_type, "BroadcastErrorNotification")
        self.assertEqual(application_messages_BEN.numeric_id, '10032')
        self.assertEqual(application_messages_BEN.description, "")
        self.assertEqual(application_messages_BEN.functional_category, "Other")
        self.assertEqual(application_messages_BEN.alias, "Gap Fill")
        self.assertEqual(application_messages_BEN.service, None)

        members_or_groups_dict = application_messages_BEN.members_or_groups
        group_MHO = members_or_groups_dict["MessageHeaderOut"]
        
        self.assertEqual(group_MHO.name, "MessageHeaderOut")
        self.assertEqual(group_MHO.group_type, "MessageHeaderOutComp")
        self.assertEqual(group_MHO.package, "eti_Cash")
        self.assertEqual(group_MHO.min_cardinality, None)
        self.assertEqual(group_MHO.cardinality, '1')
        self.assertEqual(group_MHO.description, "")
        self.assertEqual(len(group_MHO.members), 3)

        group_MHO_member_BL = group_MHO.members["BodyLen"]
        self.assertEqual(group_MHO_member_BL.name, "BodyLen")
        self.assertEqual(group_MHO_member_BL.member_type, "BodyLen")
        self.assertEqual(group_MHO_member_BL.package, "eti_Cash")
        self.assertEqual(group_MHO_member_BL.numeric_id, '9')
        self.assertEqual(group_MHO_member_BL.usage, ApplicationMessage_Usage.MANDATORY)
        self.assertEqual(group_MHO_member_BL.offset, '0')
        self.assertEqual(group_MHO_member_BL.cardinality, '1')
        self.assertEqual(group_MHO_member_BL.description, "")

        group_MHO_member_Pad2 = group_MHO.members["Pad2"]
        self.assertEqual(group_MHO_member_Pad2.name, "Pad2")
        self.assertEqual(group_MHO_member_Pad2.member_type, "Pad2")
        self.assertEqual(group_MHO_member_Pad2.package, "eti_Cash")
        self.assertEqual(group_MHO_member_Pad2.numeric_id, '39020')
        self.assertEqual(group_MHO_member_Pad2.usage, ApplicationMessage_Usage.UNUSED)
        self.assertEqual(group_MHO_member_Pad2.offset, '6')
        self.assertEqual(group_MHO_member_Pad2.cardinality, '1')
        self.assertEqual(group_MHO_member_Pad2.description, "")

    def test_schema(self):
        parser_result = Parser.from_file("../resources/eti_Cash.xml")
        schema_result = parser_result.get_schema()

        self.assertEqual(schema_result.name, "eti_Cash")
        self.assertEqual(schema_result.version, "13.1")
        self.assertEqual(schema_result.sub_version, "C0002")
        self.assertEqual(schema_result.build_number, "131.430.2.ga-131004030-47")

        # Test data types
        data_type_ApplID = schema_result.data_types["ApplID"]
        self.assertEqual(data_type_ApplID.name, "ApplID")
        self.assertEqual(data_type_ApplID.primitive_type, "int")
        self.assertEqual(data_type_ApplID.root_type, "int")
        self.assertEqual(data_type_ApplID.package, "eti_Cash")
        self.assertEqual(data_type_ApplID.numeric_id, '1180')
        self.assertEqual(data_type_ApplID.primitive_size, '1')
        self.assertEqual(data_type_ApplID.description, '')
        self.assertEqual(data_type_ApplID.min_value, '0')
        self.assertEqual(data_type_ApplID.max_value, '11')
        self.assertEqual(data_type_ApplID.precision, None)
        self.assertEqual(data_type_ApplID.range, None)
        self.assertEqual(data_type_ApplID.no_value, "0xFF")

        valid_value = data_type_ApplID.valid_value_by_name
        first_valid_value = list(valid_value.values())[0]

        self.assertEqual(first_valid_value.name , "Trade")
        self.assertEqual(first_valid_value.value , '1')
        self.assertEqual(first_valid_value.description , "Trade")

        find_by_name = valid_value["News"]

        self.assertEqual(find_by_name.name , "News")
        self.assertEqual(find_by_name.value , '2')
        self.assertEqual(find_by_name.description , "News")

        # Test structures
        structure_XetraEnLightStatusBroadcast = schema_result.structure["XetraEnLightStatusBroadcast"]
        self.assertEqual(structure_XetraEnLightStatusBroadcast.name, "XetraEnLightStatusBroadcast")
        self.assertEqual(structure_XetraEnLightStatusBroadcast.structure_type, "Message")
        self.assertEqual(structure_XetraEnLightStatusBroadcast.numeric_id, '10814')
        self.assertEqual(structure_XetraEnLightStatusBroadcast.package, "eti_Cash")
        self.assertEqual(structure_XetraEnLightStatusBroadcast.description, "")

        structure_members = structure_XetraEnLightStatusBroadcast.members
        structure_member_MHO = structure_members['MessageHeaderOut']
        
        self.assertEqual(structure_member_MHO.name, "MessageHeaderOut")
        self.assertEqual(structure_member_MHO.member_type, "MessageHeaderOutComp")
        self.assertEqual(structure_member_MHO.package, "eti_Cash")
        self.assertEqual(structure_member_MHO.min_cardinality, None)
        self.assertEqual(structure_member_MHO.cardinality, '1')
        self.assertEqual(structure_member_MHO.counter, None)
        self.assertEqual(structure_member_MHO.description, "")

        # Test application messages
        application_messages_BEN = schema_result.application_messages["BroadcastErrorNotification"]
        self.assertEqual(application_messages_BEN.name, "BroadcastErrorNotification")
        self.assertEqual(application_messages_BEN.package, "eti_Cash")
        self.assertEqual(application_messages_BEN.application_message_type, "BroadcastErrorNotification")
        self.assertEqual(application_messages_BEN.numeric_id, '10032')
        self.assertEqual(application_messages_BEN.description, "")
        self.assertEqual(application_messages_BEN.functional_category, "Other")
        self.assertEqual(application_messages_BEN.alias, "Gap Fill")
        self.assertEqual(application_messages_BEN.service, None)

        members_or_groups_dict = application_messages_BEN.members_or_groups
        group_MHO = members_or_groups_dict["MessageHeaderOut"]
        
        self.assertEqual(group_MHO.name, "MessageHeaderOut")
        self.assertEqual(group_MHO.group_type, "MessageHeaderOutComp")
        self.assertEqual(group_MHO.package, "eti_Cash")
        self.assertEqual(group_MHO.min_cardinality, None)
        self.assertEqual(group_MHO.cardinality, '1')
        self.assertEqual(group_MHO.description, "")
        self.assertEqual(len(group_MHO.members), 3)

        group_MHO_member_BL = group_MHO.members["BodyLen"]
        self.assertEqual(group_MHO_member_BL.name, "BodyLen")
        self.assertEqual(group_MHO_member_BL.member_type, "BodyLen")
        self.assertEqual(group_MHO_member_BL.package, "eti_Cash")
        self.assertEqual(group_MHO_member_BL.numeric_id, '9')
        self.assertEqual(group_MHO_member_BL.usage, ApplicationMessage_Usage.MANDATORY)
        self.assertEqual(group_MHO_member_BL.offset, '0')
        self.assertEqual(group_MHO_member_BL.cardinality, '1')
        self.assertEqual(group_MHO_member_BL.description, "")

        group_MHO_member_Pad2 = group_MHO.members["Pad2"]
        self.assertEqual(group_MHO_member_Pad2.name, "Pad2")
        self.assertEqual(group_MHO_member_Pad2.member_type, "Pad2")
        self.assertEqual(group_MHO_member_Pad2.package, "eti_Cash")
        self.assertEqual(group_MHO_member_Pad2.numeric_id, '39020')
        self.assertEqual(group_MHO_member_Pad2.usage, ApplicationMessage_Usage.UNUSED)
        self.assertEqual(group_MHO_member_Pad2.offset, '6')
        self.assertEqual(group_MHO_member_Pad2.cardinality, '1')
        self.assertEqual(group_MHO_member_Pad2.description, "")
