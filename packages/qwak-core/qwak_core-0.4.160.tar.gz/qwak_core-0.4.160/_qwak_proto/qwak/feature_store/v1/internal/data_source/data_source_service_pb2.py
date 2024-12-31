# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/feature_store/v1/internal/data_source/data_source_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDqwak/feature_store/v1/internal/data_source/data_source_service.proto\x12\x31qwak.feature.store.management.v1.internal.sources\"E\n)GetDataSourceSourceCodeDownloadURLRequest\x12\x18\n\x10\x64\x61ta_source_name\x18\x01 \x01(\t\"B\n*GetDataSourceSourceCodeDownloadURLResponse\x12\x14\n\x0c\x64ownload_url\x18\x01 \x01(\t\"@\n$GetDataSourceSourceCodeUploadRequest\x12\x18\n\x10\x64\x61ta_source_name\x18\x01 \x01(\t\";\n%GetDataSourceSourceCodeUploadResponse\x12\x12\n\nupload_url\x18\x01 \x01(\t2\xcf\x03\n\x11\x44\x61taSourceService\x12\xd5\x01\n GetDataSourceSourceCodeUploadURL\x12W.qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeUploadRequest\x1aX.qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeUploadResponse\x12\xe1\x01\n\"GetDataSourceSourceCodeDownloadURL\x12\\.qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeDownloadURLRequest\x1a].qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeDownloadURLResponseBw\n<com.qwak.ai.feature.store.management.v1.api.internal.sourcesP\x01Z5qwak/featurestore/sources;featurestoreinternalsourcesb\x06proto3')



_GETDATASOURCESOURCECODEDOWNLOADURLREQUEST = DESCRIPTOR.message_types_by_name['GetDataSourceSourceCodeDownloadURLRequest']
_GETDATASOURCESOURCECODEDOWNLOADURLRESPONSE = DESCRIPTOR.message_types_by_name['GetDataSourceSourceCodeDownloadURLResponse']
_GETDATASOURCESOURCECODEUPLOADREQUEST = DESCRIPTOR.message_types_by_name['GetDataSourceSourceCodeUploadRequest']
_GETDATASOURCESOURCECODEUPLOADRESPONSE = DESCRIPTOR.message_types_by_name['GetDataSourceSourceCodeUploadResponse']
GetDataSourceSourceCodeDownloadURLRequest = _reflection.GeneratedProtocolMessageType('GetDataSourceSourceCodeDownloadURLRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCESOURCECODEDOWNLOADURLREQUEST,
  '__module__' : 'qwak.feature_store.v1.internal.data_source.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeDownloadURLRequest)
  })
_sym_db.RegisterMessage(GetDataSourceSourceCodeDownloadURLRequest)

GetDataSourceSourceCodeDownloadURLResponse = _reflection.GeneratedProtocolMessageType('GetDataSourceSourceCodeDownloadURLResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCESOURCECODEDOWNLOADURLRESPONSE,
  '__module__' : 'qwak.feature_store.v1.internal.data_source.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeDownloadURLResponse)
  })
_sym_db.RegisterMessage(GetDataSourceSourceCodeDownloadURLResponse)

GetDataSourceSourceCodeUploadRequest = _reflection.GeneratedProtocolMessageType('GetDataSourceSourceCodeUploadRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCESOURCECODEUPLOADREQUEST,
  '__module__' : 'qwak.feature_store.v1.internal.data_source.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeUploadRequest)
  })
_sym_db.RegisterMessage(GetDataSourceSourceCodeUploadRequest)

GetDataSourceSourceCodeUploadResponse = _reflection.GeneratedProtocolMessageType('GetDataSourceSourceCodeUploadResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASOURCESOURCECODEUPLOADRESPONSE,
  '__module__' : 'qwak.feature_store.v1.internal.data_source.data_source_service_pb2'
  # @@protoc_insertion_point(class_scope:qwak.feature.store.management.v1.internal.sources.GetDataSourceSourceCodeUploadResponse)
  })
_sym_db.RegisterMessage(GetDataSourceSourceCodeUploadResponse)

_DATASOURCESERVICE = DESCRIPTOR.services_by_name['DataSourceService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n<com.qwak.ai.feature.store.management.v1.api.internal.sourcesP\001Z5qwak/featurestore/sources;featurestoreinternalsources'
  _GETDATASOURCESOURCECODEDOWNLOADURLREQUEST._serialized_start=123
  _GETDATASOURCESOURCECODEDOWNLOADURLREQUEST._serialized_end=192
  _GETDATASOURCESOURCECODEDOWNLOADURLRESPONSE._serialized_start=194
  _GETDATASOURCESOURCECODEDOWNLOADURLRESPONSE._serialized_end=260
  _GETDATASOURCESOURCECODEUPLOADREQUEST._serialized_start=262
  _GETDATASOURCESOURCECODEUPLOADREQUEST._serialized_end=326
  _GETDATASOURCESOURCECODEUPLOADRESPONSE._serialized_start=328
  _GETDATASOURCESOURCECODEUPLOADRESPONSE._serialized_end=387
  _DATASOURCESERVICE._serialized_start=390
  _DATASOURCESERVICE._serialized_end=853
# @@protoc_insertion_point(module_scope)
