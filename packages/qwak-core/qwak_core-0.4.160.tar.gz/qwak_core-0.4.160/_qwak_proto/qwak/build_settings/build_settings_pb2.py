# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/build_settings/build_settings.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(qwak/build_settings/build_settings.proto\x12\x17\x63om.qwak.build_settings\"c\n\rBuildSettings\x12R\n\x18model_repository_setting\x18\x01 \x01(\x0b\x32\x30.com.qwak.build_settings.ModelRepositorySettings\"\xcc\x02\n\x17ModelRepositorySettings\x12!\n\x19\x63ontainer_registry_prefix\x18\x01 \x01(\t\x12Q\n\x17repository_settings_ecr\x18\x02 \x01(\x0b\x32..com.qwak.build_settings.RepositorySettingsECRH\x00\x12U\n\x19repository_settings_jfrog\x18\x03 \x01(\x0b\x32\x30.com.qwak.build_settings.RepositorySettingsJFrogH\x00\x12Q\n\x17repository_settings_gcr\x18\x04 \x01(\x0b\x32..com.qwak.build_settings.RepositorySettingsGCRH\x00\x42\x11\n\x0frepository_type\"\xe2\x01\n\x17RepositorySettingsJFrog\x12P\n\x17\x61uthentication_settings\x18\x01 \x01(\x0b\x32/.com.qwak.build_settings.AuthenticationSettings\x12\x1a\n\x12jfrog_project_name\x18\x02 \x01(\t\x12Y\n\x1c\x65xternal_repository_settings\x18\x03 \x01(\x0b\x32\x33.com.qwak.build_settings.ExternalRepositorySettings\"\xb3\x01\n\x1a\x45xternalRepositorySettings\x12\x19\n\x11python_repository\x18\x01 \x03(\t\x12\x1e\n\x16huggingface_repository\x18\x02 \x01(\t\x12*\n\"allow_external_python_repositories\x18\x03 \x01(\x08\x12.\n&virtual_python_dependencies_repository\x18\x04 \x01(\t\"9\n\x16\x41uthenticationSettings\x12\r\n\x05token\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"\x17\n\x15RepositorySettingsECR\"\x17\n\x15RepositorySettingsGCRB/\n\x17\x63om.qwak.build_settingsB\x12\x42uildSettingsProtoP\x01\x62\x06proto3')



_BUILDSETTINGS = DESCRIPTOR.message_types_by_name['BuildSettings']
_MODELREPOSITORYSETTINGS = DESCRIPTOR.message_types_by_name['ModelRepositorySettings']
_REPOSITORYSETTINGSJFROG = DESCRIPTOR.message_types_by_name['RepositorySettingsJFrog']
_EXTERNALREPOSITORYSETTINGS = DESCRIPTOR.message_types_by_name['ExternalRepositorySettings']
_AUTHENTICATIONSETTINGS = DESCRIPTOR.message_types_by_name['AuthenticationSettings']
_REPOSITORYSETTINGSECR = DESCRIPTOR.message_types_by_name['RepositorySettingsECR']
_REPOSITORYSETTINGSGCR = DESCRIPTOR.message_types_by_name['RepositorySettingsGCR']
BuildSettings = _reflection.GeneratedProtocolMessageType('BuildSettings', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSETTINGS,
  '__module__' : 'qwak.build_settings.build_settings_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build_settings.BuildSettings)
  })
_sym_db.RegisterMessage(BuildSettings)

ModelRepositorySettings = _reflection.GeneratedProtocolMessageType('ModelRepositorySettings', (_message.Message,), {
  'DESCRIPTOR' : _MODELREPOSITORYSETTINGS,
  '__module__' : 'qwak.build_settings.build_settings_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build_settings.ModelRepositorySettings)
  })
_sym_db.RegisterMessage(ModelRepositorySettings)

RepositorySettingsJFrog = _reflection.GeneratedProtocolMessageType('RepositorySettingsJFrog', (_message.Message,), {
  'DESCRIPTOR' : _REPOSITORYSETTINGSJFROG,
  '__module__' : 'qwak.build_settings.build_settings_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build_settings.RepositorySettingsJFrog)
  })
_sym_db.RegisterMessage(RepositorySettingsJFrog)

ExternalRepositorySettings = _reflection.GeneratedProtocolMessageType('ExternalRepositorySettings', (_message.Message,), {
  'DESCRIPTOR' : _EXTERNALREPOSITORYSETTINGS,
  '__module__' : 'qwak.build_settings.build_settings_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build_settings.ExternalRepositorySettings)
  })
_sym_db.RegisterMessage(ExternalRepositorySettings)

AuthenticationSettings = _reflection.GeneratedProtocolMessageType('AuthenticationSettings', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONSETTINGS,
  '__module__' : 'qwak.build_settings.build_settings_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build_settings.AuthenticationSettings)
  })
_sym_db.RegisterMessage(AuthenticationSettings)

RepositorySettingsECR = _reflection.GeneratedProtocolMessageType('RepositorySettingsECR', (_message.Message,), {
  'DESCRIPTOR' : _REPOSITORYSETTINGSECR,
  '__module__' : 'qwak.build_settings.build_settings_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build_settings.RepositorySettingsECR)
  })
_sym_db.RegisterMessage(RepositorySettingsECR)

RepositorySettingsGCR = _reflection.GeneratedProtocolMessageType('RepositorySettingsGCR', (_message.Message,), {
  'DESCRIPTOR' : _REPOSITORYSETTINGSGCR,
  '__module__' : 'qwak.build_settings.build_settings_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build_settings.RepositorySettingsGCR)
  })
_sym_db.RegisterMessage(RepositorySettingsGCR)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.qwak.build_settingsB\022BuildSettingsProtoP\001'
  _BUILDSETTINGS._serialized_start=69
  _BUILDSETTINGS._serialized_end=168
  _MODELREPOSITORYSETTINGS._serialized_start=171
  _MODELREPOSITORYSETTINGS._serialized_end=503
  _REPOSITORYSETTINGSJFROG._serialized_start=506
  _REPOSITORYSETTINGSJFROG._serialized_end=732
  _EXTERNALREPOSITORYSETTINGS._serialized_start=735
  _EXTERNALREPOSITORYSETTINGS._serialized_end=914
  _AUTHENTICATIONSETTINGS._serialized_start=916
  _AUTHENTICATIONSETTINGS._serialized_end=973
  _REPOSITORYSETTINGSECR._serialized_start=975
  _REPOSITORYSETTINGSECR._serialized_end=998
  _REPOSITORYSETTINGSGCR._serialized_start=1000
  _REPOSITORYSETTINGSGCR._serialized_end=1023
# @@protoc_insertion_point(module_scope)
