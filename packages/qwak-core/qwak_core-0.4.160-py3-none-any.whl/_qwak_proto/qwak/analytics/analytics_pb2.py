# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/analytics/analytics.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eqwak/analytics/analytics.proto\x12\x0eqwak.analytics\"w\n\nResultData\x12\x0f\n\x07headers\x18\x01 \x03(\t\x12/\n\x0bheadersDesc\x18\x03 \x03(\x0b\x32\x1a.qwak.analytics.HeaderDesc\x12\'\n\x04rows\x18\x02 \x03(\x0b\x32\x19.qwak.analytics.ResultRow\"(\n\nHeaderDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"\x1b\n\tResultRow\x12\x0e\n\x06values\x18\x01 \x03(\t\":\n\x0bTableColumn\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07\x63omment\x18\x03 \x01(\t\"O\n\x15TableColumnDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x04type\x18\x02 \x01(\x0e\x32\x1a.qwak.analytics.ColumnType\"\xe8\x01\n\x0fTableDefinition\x12\x0f\n\x07\x64\x62_name\x18\x01 \x01(\t\x12\x12\n\ntable_name\x18\x02 \x01(\t\x12\x36\n\x07\x63olumns\x18\x03 \x03(\x0b\x32%.qwak.analytics.TableColumnDefinition\x12\x11\n\tdata_path\x18\x04 \x01(\t\x12*\n\x06\x66ormat\x18\x05 \x01(\x0b\x32\x1a.qwak.analytics.DataFormat\x12\x39\n\npartitions\x18\x06 \x03(\x0b\x32%.qwak.analytics.TableColumnDefinition\"?\n\nDataFormat\x12\'\n\x03\x63sv\x18\x01 \x01(\x0b\x32\x18.qwak.analytics.CsvInputH\x00\x42\x08\n\x06\x66ormat\"F\n\x08\x43svInput\x12\x11\n\tdelimiter\x18\x01 \x01(\t\x12\x12\n\nquote_char\x18\x02 \x01(\t\x12\x13\n\x0b\x65scape_char\x18\x03 \x01(\t\"0\n\x1cQueryResultDownloadURLParams\x12\x10\n\x08query_id\x18\x01 \x01(\t*N\n\x0bQueryStatus\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04*\xad\x01\n\nColumnType\x12\x10\n\x0cINVALID_TYPE\x10\x00\x12\x0b\n\x07\x42OOLEAN\x10\x01\x12\x0b\n\x07TINYINT\x10\x02\x12\x0c\n\x08SMALLINT\x10\x03\x12\x07\n\x03INT\x10\x04\x12\n\n\x06\x42IGINT\x10\x05\x12\n\n\x06\x44OUBLE\x10\x06\x12\t\n\x05\x46LOAT\x10\x07\x12\x08\n\x04\x43HAR\x10\x08\x12\n\n\x06STRING\x10\t\x12\n\n\x06\x42INARY\x10\n\x12\x08\n\x04\x44\x41TE\x10\x0b\x12\r\n\tTIMESTAMP\x10\x0c\x42\x86\x01\n\x19\x63om.qwak.ai.analytics.apiP\x01Zggithub.com/qwak-ai/qwak-platform/services/core/java/analytics/analytics-api/pb/qwak/analytics;analyticsb\x06proto3')

_QUERYSTATUS = DESCRIPTOR.enum_types_by_name['QueryStatus']
QueryStatus = enum_type_wrapper.EnumTypeWrapper(_QUERYSTATUS)
_COLUMNTYPE = DESCRIPTOR.enum_types_by_name['ColumnType']
ColumnType = enum_type_wrapper.EnumTypeWrapper(_COLUMNTYPE)
INVALID = 0
SUCCESS = 1
PENDING = 2
CANCELED = 3
FAILED = 4
INVALID_TYPE = 0
BOOLEAN = 1
TINYINT = 2
SMALLINT = 3
INT = 4
BIGINT = 5
DOUBLE = 6
FLOAT = 7
CHAR = 8
STRING = 9
BINARY = 10
DATE = 11
TIMESTAMP = 12


_RESULTDATA = DESCRIPTOR.message_types_by_name['ResultData']
_HEADERDESC = DESCRIPTOR.message_types_by_name['HeaderDesc']
_RESULTROW = DESCRIPTOR.message_types_by_name['ResultRow']
_TABLECOLUMN = DESCRIPTOR.message_types_by_name['TableColumn']
_TABLECOLUMNDEFINITION = DESCRIPTOR.message_types_by_name['TableColumnDefinition']
_TABLEDEFINITION = DESCRIPTOR.message_types_by_name['TableDefinition']
_DATAFORMAT = DESCRIPTOR.message_types_by_name['DataFormat']
_CSVINPUT = DESCRIPTOR.message_types_by_name['CsvInput']
_QUERYRESULTDOWNLOADURLPARAMS = DESCRIPTOR.message_types_by_name['QueryResultDownloadURLParams']
ResultData = _reflection.GeneratedProtocolMessageType('ResultData', (_message.Message,), {
  'DESCRIPTOR' : _RESULTDATA,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.ResultData)
  })
_sym_db.RegisterMessage(ResultData)

HeaderDesc = _reflection.GeneratedProtocolMessageType('HeaderDesc', (_message.Message,), {
  'DESCRIPTOR' : _HEADERDESC,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.HeaderDesc)
  })
_sym_db.RegisterMessage(HeaderDesc)

ResultRow = _reflection.GeneratedProtocolMessageType('ResultRow', (_message.Message,), {
  'DESCRIPTOR' : _RESULTROW,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.ResultRow)
  })
_sym_db.RegisterMessage(ResultRow)

TableColumn = _reflection.GeneratedProtocolMessageType('TableColumn', (_message.Message,), {
  'DESCRIPTOR' : _TABLECOLUMN,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.TableColumn)
  })
_sym_db.RegisterMessage(TableColumn)

TableColumnDefinition = _reflection.GeneratedProtocolMessageType('TableColumnDefinition', (_message.Message,), {
  'DESCRIPTOR' : _TABLECOLUMNDEFINITION,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.TableColumnDefinition)
  })
_sym_db.RegisterMessage(TableColumnDefinition)

TableDefinition = _reflection.GeneratedProtocolMessageType('TableDefinition', (_message.Message,), {
  'DESCRIPTOR' : _TABLEDEFINITION,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.TableDefinition)
  })
_sym_db.RegisterMessage(TableDefinition)

DataFormat = _reflection.GeneratedProtocolMessageType('DataFormat', (_message.Message,), {
  'DESCRIPTOR' : _DATAFORMAT,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.DataFormat)
  })
_sym_db.RegisterMessage(DataFormat)

CsvInput = _reflection.GeneratedProtocolMessageType('CsvInput', (_message.Message,), {
  'DESCRIPTOR' : _CSVINPUT,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.CsvInput)
  })
_sym_db.RegisterMessage(CsvInput)

QueryResultDownloadURLParams = _reflection.GeneratedProtocolMessageType('QueryResultDownloadURLParams', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESULTDOWNLOADURLPARAMS,
  '__module__' : 'qwak.analytics.analytics_pb2'
  # @@protoc_insertion_point(class_scope:qwak.analytics.QueryResultDownloadURLParams)
  })
_sym_db.RegisterMessage(QueryResultDownloadURLParams)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.qwak.ai.analytics.apiP\001Zggithub.com/qwak-ai/qwak-platform/services/core/java/analytics/analytics-api/pb/qwak/analytics;analytics'
  _QUERYSTATUS._serialized_start=805
  _QUERYSTATUS._serialized_end=883
  _COLUMNTYPE._serialized_start=886
  _COLUMNTYPE._serialized_end=1059
  _RESULTDATA._serialized_start=50
  _RESULTDATA._serialized_end=169
  _HEADERDESC._serialized_start=171
  _HEADERDESC._serialized_end=211
  _RESULTROW._serialized_start=213
  _RESULTROW._serialized_end=240
  _TABLECOLUMN._serialized_start=242
  _TABLECOLUMN._serialized_end=300
  _TABLECOLUMNDEFINITION._serialized_start=302
  _TABLECOLUMNDEFINITION._serialized_end=381
  _TABLEDEFINITION._serialized_start=384
  _TABLEDEFINITION._serialized_end=616
  _DATAFORMAT._serialized_start=618
  _DATAFORMAT._serialized_end=681
  _CSVINPUT._serialized_start=683
  _CSVINPUT._serialized_end=753
  _QUERYRESULTDOWNLOADURLPARAMS._serialized_start=755
  _QUERYRESULTDOWNLOADURLPARAMS._serialized_end=803
# @@protoc_insertion_point(module_scope)
