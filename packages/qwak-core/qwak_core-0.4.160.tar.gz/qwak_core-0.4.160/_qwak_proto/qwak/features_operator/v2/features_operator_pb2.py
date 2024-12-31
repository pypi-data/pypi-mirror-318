# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/features_operator/v2/features_operator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1qwak/features_operator/v2/features_operator.proto\x12\x19qwak.features_operator.v2\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa1\x02\n\x19ValidationSuccessResponse\x12\x0e\n\x06sample\x18\x01 \x01(\t\x12H\n\x12\x63olumn_description\x18\x02 \x03(\x0b\x32,.qwak.features_operator.v2.ColumnDescription\x12U\n\x19pandas_column_description\x18\x03 \x03(\x0b\x32\x32.qwak.features_operator.v2.PandasColumnDescription\x12S\n\x18spark_column_description\x18\x04 \x03(\x0b\x32\x31.qwak.features_operator.v2.SparkColumnDescription\"<\n\x11\x43olumnDescription\x12\x13\n\x0b\x63olumn_name\x18\x01 \x01(\t\x12\x12\n\nspark_type\x18\x02 \x01(\t\"C\n\x17PandasColumnDescription\x12\x13\n\x0b\x63olumn_name\x18\x01 \x01(\t\x12\x13\n\x0bpandas_type\x18\x02 \x01(\t\"A\n\x16SparkColumnDescription\x12\x13\n\x0b\x63olumn_name\x18\x01 \x01(\t\x12\x12\n\nspark_type\x18\x02 \x01(\t\"V\n\x19ValidationFailureResponse\x12\r\n\x05phase\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"\x1c\n\x1aValidationNotReadyResponseB(\n$com.qwak.ai.features.operator.api.v2P\x01\x62\x06proto3')



_VALIDATIONSUCCESSRESPONSE = DESCRIPTOR.message_types_by_name['ValidationSuccessResponse']
_COLUMNDESCRIPTION = DESCRIPTOR.message_types_by_name['ColumnDescription']
_PANDASCOLUMNDESCRIPTION = DESCRIPTOR.message_types_by_name['PandasColumnDescription']
_SPARKCOLUMNDESCRIPTION = DESCRIPTOR.message_types_by_name['SparkColumnDescription']
_VALIDATIONFAILURERESPONSE = DESCRIPTOR.message_types_by_name['ValidationFailureResponse']
_VALIDATIONNOTREADYRESPONSE = DESCRIPTOR.message_types_by_name['ValidationNotReadyResponse']
ValidationSuccessResponse = _reflection.GeneratedProtocolMessageType('ValidationSuccessResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATIONSUCCESSRESPONSE,
  '__module__' : 'qwak.features_operator.v2.features_operator_pb2'
  # @@protoc_insertion_point(class_scope:qwak.features_operator.v2.ValidationSuccessResponse)
  })
_sym_db.RegisterMessage(ValidationSuccessResponse)

ColumnDescription = _reflection.GeneratedProtocolMessageType('ColumnDescription', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNDESCRIPTION,
  '__module__' : 'qwak.features_operator.v2.features_operator_pb2'
  # @@protoc_insertion_point(class_scope:qwak.features_operator.v2.ColumnDescription)
  })
_sym_db.RegisterMessage(ColumnDescription)

PandasColumnDescription = _reflection.GeneratedProtocolMessageType('PandasColumnDescription', (_message.Message,), {
  'DESCRIPTOR' : _PANDASCOLUMNDESCRIPTION,
  '__module__' : 'qwak.features_operator.v2.features_operator_pb2'
  # @@protoc_insertion_point(class_scope:qwak.features_operator.v2.PandasColumnDescription)
  })
_sym_db.RegisterMessage(PandasColumnDescription)

SparkColumnDescription = _reflection.GeneratedProtocolMessageType('SparkColumnDescription', (_message.Message,), {
  'DESCRIPTOR' : _SPARKCOLUMNDESCRIPTION,
  '__module__' : 'qwak.features_operator.v2.features_operator_pb2'
  # @@protoc_insertion_point(class_scope:qwak.features_operator.v2.SparkColumnDescription)
  })
_sym_db.RegisterMessage(SparkColumnDescription)

ValidationFailureResponse = _reflection.GeneratedProtocolMessageType('ValidationFailureResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATIONFAILURERESPONSE,
  '__module__' : 'qwak.features_operator.v2.features_operator_pb2'
  # @@protoc_insertion_point(class_scope:qwak.features_operator.v2.ValidationFailureResponse)
  })
_sym_db.RegisterMessage(ValidationFailureResponse)

ValidationNotReadyResponse = _reflection.GeneratedProtocolMessageType('ValidationNotReadyResponse', (_message.Message,), {
  'DESCRIPTOR' : _VALIDATIONNOTREADYRESPONSE,
  '__module__' : 'qwak.features_operator.v2.features_operator_pb2'
  # @@protoc_insertion_point(class_scope:qwak.features_operator.v2.ValidationNotReadyResponse)
  })
_sym_db.RegisterMessage(ValidationNotReadyResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$com.qwak.ai.features.operator.api.v2P\001'
  _VALIDATIONSUCCESSRESPONSE._serialized_start=114
  _VALIDATIONSUCCESSRESPONSE._serialized_end=403
  _COLUMNDESCRIPTION._serialized_start=405
  _COLUMNDESCRIPTION._serialized_end=465
  _PANDASCOLUMNDESCRIPTION._serialized_start=467
  _PANDASCOLUMNDESCRIPTION._serialized_end=534
  _SPARKCOLUMNDESCRIPTION._serialized_start=536
  _SPARKCOLUMNDESCRIPTION._serialized_end=601
  _VALIDATIONFAILURERESPONSE._serialized_start=603
  _VALIDATIONFAILURERESPONSE._serialized_end=689
  _VALIDATIONNOTREADYRESPONSE._serialized_start=691
  _VALIDATIONNOTREADYRESPONSE._serialized_end=719
# @@protoc_insertion_point(module_scope)
