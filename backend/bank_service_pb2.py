# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank_service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x62\x61nk_service.proto\"\x1f\n\x0b\x42\x61nkRequest\x12\x10\n\x08\x62ranchID\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty\"3\n\x1aGetCashRequirementResponse\x12\x15\n\rbranchMinCash\x18\x01 \x01(\x05\"1\n\x16TotalEmployeesResponse\x12\x17\n\x0ftotal_employees\x18\x01 \x01(\x05\"?\n\x08\x45mployee\x12\x13\n\x0b\x65mployee_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x62ranchID\x18\x03 \x01(\t\"#\n\x10\x45mployeeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"!\n\nEmployeeID\x12\x13\n\x0b\x65mployee_id\x18\x01 \x01(\t\"!\n\x0e\x44\x65leteResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x1e\n\nBranchInfo\x12\x10\n\x08\x62ranchID\x18\x01 \x01(\t\"%\n\x0c\x43\x61shResponse\x12\x15\n\rbranchMinCash\x18\x01 \x01(\x01\"<\n\x11\x43\x61shUpdateRequest\x12\x10\n\x08\x62ranchID\x18\x01 \x01(\t\x12\x15\n\rbranchMinCash\x18\x02 \x01(\x01\"%\n\x12\x43\x61shUpdateResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\";\n\x06\x43lient\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08\x62ranchID\x18\x03 \x01(\t\"7\n\x06\x42ranch\x12\x10\n\x08location\x18\x01 \x01(\t\x12\x1b\n\x13number_of_employees\x18\x02 \x01(\x05\"!\n\x0e\x42ranchResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"I\n\x17UpdateBranchSizeRequest\x12\x10\n\x08\x62ranchID\x18\x01 \x01(\x05\x12\x1c\n\x14newNumberOfEmployees\x18\x02 \x01(\x05\"o\n\x18\x42\x61nkAllAtributesResponse\x12\x10\n\x08\x62ranchID\x18\x01 \x01(\x05\x12\x12\n\nbranchSize\x18\x02 \x01(\x05\x12\x16\n\x0e\x62ranchLocation\x18\x03 \x01(\t\x12\x15\n\rbranchMinCash\x18\x04 \x01(\x05\"B\n\x13\x42ranchesResponseAll\x12+\n\x08\x62ranches\x18\x01 \x03(\x0b\x32\x19.BankAllAtributesResponse\"[\n\x18UpdateBranchSizeResponse\x12\x10\n\x08\x62ranchID\x18\x01 \x01(\x05\x12\x15\n\rbranchMinCash\x18\x02 \x01(\x05\x12\x16\n\x0e\x62ranchLocation\x18\x03 \x01(\t2\xbd\x02\n\x07Greeter\x12:\n\x11GetTotalEmployees\x12\x0c.BankRequest\x1a\x17.TotalEmployeesResponse\x12\x37\n\tAddBranch\x12\x19.BankAllAtributesResponse\x1a\x0f.BranchResponse\x12\x33\n\x0eGetBranchesAll\x12\x06.Empty\x1a\x19.BankAllAtributesResponse\x12?\n\x12GetCashRequirement\x12\x0c.BankRequest\x1a\x1b.GetCashRequirementResponse\x12G\n\x10UpdateBranchSize\x12\x18.UpdateBranchSizeRequest\x1a\x19.UpdateBranchSizeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bank_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BANKREQUEST']._serialized_start=22
  _globals['_BANKREQUEST']._serialized_end=53
  _globals['_EMPTY']._serialized_start=55
  _globals['_EMPTY']._serialized_end=62
  _globals['_GETCASHREQUIREMENTRESPONSE']._serialized_start=64
  _globals['_GETCASHREQUIREMENTRESPONSE']._serialized_end=115
  _globals['_TOTALEMPLOYEESRESPONSE']._serialized_start=117
  _globals['_TOTALEMPLOYEESRESPONSE']._serialized_end=166
  _globals['_EMPLOYEE']._serialized_start=168
  _globals['_EMPLOYEE']._serialized_end=231
  _globals['_EMPLOYEERESPONSE']._serialized_start=233
  _globals['_EMPLOYEERESPONSE']._serialized_end=268
  _globals['_EMPLOYEEID']._serialized_start=270
  _globals['_EMPLOYEEID']._serialized_end=303
  _globals['_DELETERESPONSE']._serialized_start=305
  _globals['_DELETERESPONSE']._serialized_end=338
  _globals['_BRANCHINFO']._serialized_start=340
  _globals['_BRANCHINFO']._serialized_end=370
  _globals['_CASHRESPONSE']._serialized_start=372
  _globals['_CASHRESPONSE']._serialized_end=409
  _globals['_CASHUPDATEREQUEST']._serialized_start=411
  _globals['_CASHUPDATEREQUEST']._serialized_end=471
  _globals['_CASHUPDATERESPONSE']._serialized_start=473
  _globals['_CASHUPDATERESPONSE']._serialized_end=510
  _globals['_CLIENT']._serialized_start=512
  _globals['_CLIENT']._serialized_end=571
  _globals['_BRANCH']._serialized_start=573
  _globals['_BRANCH']._serialized_end=628
  _globals['_BRANCHRESPONSE']._serialized_start=630
  _globals['_BRANCHRESPONSE']._serialized_end=663
  _globals['_UPDATEBRANCHSIZEREQUEST']._serialized_start=665
  _globals['_UPDATEBRANCHSIZEREQUEST']._serialized_end=738
  _globals['_BANKALLATRIBUTESRESPONSE']._serialized_start=740
  _globals['_BANKALLATRIBUTESRESPONSE']._serialized_end=851
  _globals['_BRANCHESRESPONSEALL']._serialized_start=853
  _globals['_BRANCHESRESPONSEALL']._serialized_end=919
  _globals['_UPDATEBRANCHSIZERESPONSE']._serialized_start=921
  _globals['_UPDATEBRANCHSIZERESPONSE']._serialized_end=1012
  _globals['_GREETER']._serialized_start=1015
  _globals['_GREETER']._serialized_end=1332
# @@protoc_insertion_point(module_scope)
