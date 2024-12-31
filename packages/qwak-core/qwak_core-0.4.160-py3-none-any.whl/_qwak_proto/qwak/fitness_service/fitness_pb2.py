# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/fitness_service/fitness.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from _qwak_proto.qwak.fitness_service import constructs_pb2 as qwak_dot_fitness__service_dot_constructs__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"qwak/fitness_service/fitness.proto\x12\x14qwak.fitness.service\x1a%qwak/fitness_service/constructs.proto\"\xac\x04\n\tBuildSpec\x12?\n\x10\x62uild_properties\x18\x01 \x01(\x0b\x32%.qwak.fitness.service.BuildProperties\x12\x31\n\tbuild_env\x18\x02 \x01(\x0b\x32\x1e.qwak.fitness.service.BuildEnv\x12;\n\rcpu_resources\x18\x03 \x01(\x0b\x32\".qwak.fitness.service.CpuResourcesH\x00\x12;\n\rgpu_resources\x18\x07 \x01(\x0b\x32\".qwak.fitness.service.GpuResourcesH\x00\x12\x0f\n\x07verbose\x18\x04 \x01(\x05\x12\x14\n\x0c\x62uild_config\x18\x05 \x01(\t\x12\x15\n\rbuild_v1_flag\x18\x06 \x01(\x08\x12\x44\n\x13\x62uild_properties_v1\x18\x08 \x01(\x0b\x32\'.qwak.fitness.service.BuildPropertiesV1\x12=\n\x0fpurchase_option\x18\t \x01(\x0e\x32$.qwak.fitness.service.PurchaseOption\x12\x1c\n\x14\x62uild_destined_image\x18\n \x01(\t\x12\"\n\x1aprovision_instance_timeout\x18\x0b \x01(\x05\x12\x1f\n\x17\x61rtifactory_project_key\x18\x0c \x01(\tB\x0b\n\tResources\"g\n\x11\x42uildPropertiesV1\x12\x18\n\x10\x62uild_config_url\x18\x01 \x01(\t\x12\x1a\n\x12qwak_sdk_wheel_url\x18\x02 \x01(\t\x12\x1c\n\x14qwak_sdk_version_url\x18\x03 \x01(\t*e\n\x0ePurchaseOption\x12\x1b\n\x17INVALID_PURCHASE_OPTION\x10\x00\x12\x18\n\x14SPOT_PURCHASE_OPTION\x10\x01\x12\x1c\n\x18ONDEMAND_PURCHASE_OPTION\x10\x02\x42#\n\x1f\x63om.qwak.ai.fitness.service.apiP\x01\x62\x06proto3')

_PURCHASEOPTION = DESCRIPTOR.enum_types_by_name['PurchaseOption']
PurchaseOption = enum_type_wrapper.EnumTypeWrapper(_PURCHASEOPTION)
INVALID_PURCHASE_OPTION = 0
SPOT_PURCHASE_OPTION = 1
ONDEMAND_PURCHASE_OPTION = 2


_BUILDSPEC = DESCRIPTOR.message_types_by_name['BuildSpec']
_BUILDPROPERTIESV1 = DESCRIPTOR.message_types_by_name['BuildPropertiesV1']
BuildSpec = _reflection.GeneratedProtocolMessageType('BuildSpec', (_message.Message,), {
  'DESCRIPTOR' : _BUILDSPEC,
  '__module__' : 'qwak.fitness_service.fitness_pb2'
  # @@protoc_insertion_point(class_scope:qwak.fitness.service.BuildSpec)
  })
_sym_db.RegisterMessage(BuildSpec)

BuildPropertiesV1 = _reflection.GeneratedProtocolMessageType('BuildPropertiesV1', (_message.Message,), {
  'DESCRIPTOR' : _BUILDPROPERTIESV1,
  '__module__' : 'qwak.fitness_service.fitness_pb2'
  # @@protoc_insertion_point(class_scope:qwak.fitness.service.BuildPropertiesV1)
  })
_sym_db.RegisterMessage(BuildPropertiesV1)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.qwak.ai.fitness.service.apiP\001'
  _PURCHASEOPTION._serialized_start=763
  _PURCHASEOPTION._serialized_end=864
  _BUILDSPEC._serialized_start=100
  _BUILDSPEC._serialized_end=656
  _BUILDPROPERTIESV1._serialized_start=658
  _BUILDPROPERTIESV1._serialized_end=761
# @@protoc_insertion_point(module_scope)
