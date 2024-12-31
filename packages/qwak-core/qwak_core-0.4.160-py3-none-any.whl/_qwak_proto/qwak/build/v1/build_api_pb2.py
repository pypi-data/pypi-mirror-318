# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: qwak/build/v1/build_api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from _qwak_proto.qwak.build.v1 import build_pb2 as qwak_dot_build_dot_v1_dot_build__pb2
from _qwak_proto.qwak.user_application.common.v0 import resources_pb2 as qwak_dot_user__application_dot_common_dot_v0_dot_resources__pb2
from _qwak_proto.qwak.fitness_service import fitness_pb2 as qwak_dot_fitness__service_dot_fitness__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dqwak/build/v1/build_api.proto\x12\x11\x63om.qwak.build.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19qwak/build/v1/build.proto\x1a/qwak/user_application/common/v0/resources.proto\x1a\"qwak/fitness_service/fitness.proto\"R\n\x1aSaveFrameworkModelsRequest\x12\x34\n\x04spec\x18\x01 \x01(\x0b\x32&.com.qwak.build.v1.FrameworkModelsSpec\"\x1d\n\x1bSaveFrameworkModelsResponse\"|\n\x14RegisterBuildRequest\x12\x0f\n\x07\x62uildId\x18\x01 \x01(\t\x12\x10\n\x08\x63ommitId\x18\x02 \x01(\t\x12\x0f\n\x07modelId\x18\x03 \x01(\t\x12\x13\n\x0b\x62uildConfig\x18\x04 \x01(\t\x12\x0c\n\x04tags\x18\x05 \x03(\t\x12\r\n\x05steps\x18\x06 \x03(\t\"\x17\n\x15RegisterBuildResponse\"a\n\x18UpdateBuildStatusRequest\x12\x0f\n\x07\x62uildId\x18\x01 \x01(\t\x12\x34\n\x0c\x62uild_status\x18\x02 \x01(\x0e\x32\x1e.com.qwak.build.v1.BuildStatus\"\x1b\n\x19UpdateBuildStatusResponse\"\xba\x02\n!RegisterExperimentTrackingRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12P\n\x06params\x18\x02 \x03(\x0b\x32@.com.qwak.build.v1.RegisterExperimentTrackingRequest.ParamsEntry\x12R\n\x07metrics\x18\x03 \x03(\x0b\x32\x41.com.qwak.build.v1.RegisterExperimentTrackingRequest.MetricsEntry\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a.\n\x0cMetricsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\"$\n\"RegisterExperimentTrackingResponse\"d\n\x1aRegisterModelSchemaRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x34\n\x0cmodel_schema\x18\x02 \x01(\x0b\x32\x1e.com.qwak.build.v1.ModelSchema\"\x1d\n\x1bRegisterModelSchemaResponse\"#\n\x0fGetBuildRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\";\n\x10GetBuildResponse\x12\'\n\x05\x62uild\x18\x01 \x01(\x0b\x32\x18.com.qwak.build.v1.Build\"n\n\x11ListBuildsRequest\x12\x15\n\tbranch_id\x18\x01 \x01(\tB\x02\x18\x01\x12.\n\x06\x66ilter\x18\x02 \x01(\x0b\x32\x1e.com.qwak.build.v1.BuildFilter\x12\x12\n\nmodel_uuid\x18\x03 \x01(\t\"=\n\x12ListBuildsResponse\x12\'\n\x05\x62uild\x18\x01 \x03(\x0b\x32\x18.com.qwak.build.v1.Build\"5\n\x13RegisterTagsRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x0c\n\x04tags\x18\x02 \x03(\t\"\x16\n\x14RegisterTagsResponse\"\x8e\x01\n\x15LogPhaseStatusRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x10\n\x08phase_id\x18\x02 \x01(\t\x12.\n\x06status\x18\x03 \x01(\x0e\x32\x1e.com.qwak.build.v1.PhaseStatus\x12!\n\x19phase_duration_in_seconds\x18\x04 \x01(\x05\"\x18\n\x16LogPhaseStatusResponse\"+\n\x17GetPhaseStatusesRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\"\x99\x02\n\x0ePhaseStatusLog\x12\x10\n\x08phase_id\x18\x01 \x01(\t\x12.\n\x06status\x18\x02 \x01(\x0e\x32\x1e.com.qwak.build.v1.PhaseStatus\x12!\n\x19phase_duration_in_seconds\x18\x03 \x01(\x05\x12<\n\x12pod_failure_reason\x18\x04 \x01(\x0e\x32 .com.qwak.build.v1.FailureReason\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10last_modified_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"O\n\x18GetPhaseStatusesResponse\x12\x33\n\x08statuses\x18\x01 \x03(\x0b\x32!.com.qwak.build.v1.PhaseStatusLog\"\'\n\x12\x44\x65leteBuildRequest\x12\x11\n\tbuild_ids\x18\x01 \x03(\t\"\x15\n\x13\x44\x65leteBuildResponse\"a\n\x11GetTagPathRequest\x12\x16\n\x0e\x65nvironment_id\x18\x01 \x01(\t\x12\x10\n\x08model_id\x18\x02 \x01(\t\x12\x10\n\x08\x62uild_id\x18\x03 \x01(\t\x12\x10\n\x08tag_name\x18\x04 \x01(\t\"&\n\x12GetTagPathResponse\x12\x10\n\x08key_path\x18\x01 \x01(\t\"\xa4\x02\n\x1dRerunBuildFromExistingRequest\x12\x19\n\x11\x65xisting_build_id\x18\x01 \x01(\t\x12\x46\n\x17new_build_configuration\x18\x02 \x01(\x0b\x32%.com.qwak.build.v1.BuildConfiguration\x12M\n\tresources\x18\x03 \x01(\x0b\x32:.qwak.user_application.common.v0.ClientPodComputeResources\x12=\n\x0fpurchase_option\x18\x04 \x01(\x0e\x32$.qwak.fitness.service.PurchaseOption\x12\x12\n\nbuild_name\x18\x05 \x01(\t\" \n\x1eRerunBuildFromExistingResponse\"S\n$GetBuildsArtifactsScanSummaryRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x19\n\rartifact_name\x18\x02 \x01(\tB\x02\x18\x01\"\xd5\x02\n%GetBuildsArtifactsScanSummaryResponse\x12\x38\n\x06result\x18\x01 \x01(\x0b\x32$.com.qwak.build.v1.ScanResultSummaryB\x02\x18\x01\x12\x1a\n\x0eui_direct_link\x18\x02 \x01(\tB\x02\x18\x01\x12s\n\x17result_by_artifact_name\x18\x03 \x03(\x0b\x32R.com.qwak.build.v1.GetBuildsArtifactsScanSummaryResponse.ResultByArtifactNameEntry\x1a\x61\n\x19ResultByArtifactNameEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32$.com.qwak.build.v1.ScanResultSummary:\x02\x38\x01\"G\n\x1bGetBuildImageDetailsRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x16\n\x0e\x65nvironment_id\x18\x02 \x01(\t\"a\n\x1cGetBuildImageDetailsResponse\x12\x41\n\x13\x62uild_image_details\x18\x01 \x01(\x0b\x32$.com.qwak.build.v1.BuildImageDetails\">\n\x16UpdateBuildNameRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12\x12\n\nbuild_name\x18\x02 \x01(\t\"\x19\n\x17UpdateBuildNameResponse\"p\n\x1dGetBuildsArtifactsScanRequest\x12\x10\n\x08\x62uild_id\x18\x01 \x01(\t\x12=\n\x11scan_request_type\x18\x02 \x01(\x0b\x32\".com.qwak.build.v1.ScanRequestType\"2\n\x1eGetBuildsArtifactsScanResponse\x12\x10\n\x08raw_data\x18\x01 \x01(\t*\x97\x01\n\x0bPhaseStatus\x12\x18\n\x14PHASE_STATUS_INVALID\x10\x00\x12\x1c\n\x18PHASE_STATUS_IN_PROGRESS\x10\x01\x12\x1b\n\x17PHASE_STATUS_SUCCESSFUL\x10\x02\x12\x17\n\x13PHASE_STATUS_FAILED\x10\x03\x12\x1a\n\x16PHASE_STATUS_CANCELLED\x10\x04*w\n\rFailureReason\x12\x1e\n\x1a\x46\x41ILURE_REASON_UNSPECIFIED\x10\x00\x12$\n FAILURE_REASON_AVAILABLE_IN_LOGS\x10\x01\x12 \n\x1c\x46\x41ILURE_REASON_OUT_OF_MEMORY\x10\x02\x32\xea\x0e\n\x08\x42uildAPI\x12\x62\n\rRegisterBuild\x12\'.com.qwak.build.v1.RegisterBuildRequest\x1a(.com.qwak.build.v1.RegisterBuildResponse\x12n\n\x11UpdateBuildStatus\x12+.com.qwak.build.v1.UpdateBuildStatusRequest\x1a,.com.qwak.build.v1.UpdateBuildStatusResponse\x12\x89\x01\n\x1aRegisterExperimentTracking\x12\x34.com.qwak.build.v1.RegisterExperimentTrackingRequest\x1a\x35.com.qwak.build.v1.RegisterExperimentTrackingResponse\x12_\n\x0cRegisterTags\x12&.com.qwak.build.v1.RegisterTagsRequest\x1a\'.com.qwak.build.v1.RegisterTagsResponse\x12t\n\x13RegisterModelSchema\x12-.com.qwak.build.v1.RegisterModelSchemaRequest\x1a..com.qwak.build.v1.RegisterModelSchemaResponse\x12S\n\x08GetBuild\x12\".com.qwak.build.v1.GetBuildRequest\x1a#.com.qwak.build.v1.GetBuildResponse\x12Y\n\nListBuilds\x12$.com.qwak.build.v1.ListBuildsRequest\x1a%.com.qwak.build.v1.ListBuildsResponse\x12\\\n\x0b\x44\x65leteBuild\x12%.com.qwak.build.v1.DeleteBuildRequest\x1a&.com.qwak.build.v1.DeleteBuildResponse\x12\x65\n\x0eLogPhaseStatus\x12(.com.qwak.build.v1.LogPhaseStatusRequest\x1a).com.qwak.build.v1.LogPhaseStatusResponse\x12k\n\x10GetPhaseStatuses\x12*.com.qwak.build.v1.GetPhaseStatusesRequest\x1a+.com.qwak.build.v1.GetPhaseStatusesResponse\x12Y\n\nGetTagPath\x12$.com.qwak.build.v1.GetTagPathRequest\x1a%.com.qwak.build.v1.GetTagPathResponse\x12}\n\x16RerunBuildFromExisting\x12\x30.com.qwak.build.v1.RerunBuildFromExistingRequest\x1a\x31.com.qwak.build.v1.RerunBuildFromExistingResponse\x12t\n\x13SaveFrameworkModels\x12-.com.qwak.build.v1.SaveFrameworkModelsRequest\x1a..com.qwak.build.v1.SaveFrameworkModelsResponse\x12\x92\x01\n\x1dGetBuildsArtifactsScanSummary\x12\x37.com.qwak.build.v1.GetBuildsArtifactsScanSummaryRequest\x1a\x38.com.qwak.build.v1.GetBuildsArtifactsScanSummaryResponse\x12w\n\x14GetBuildImageDetails\x12..com.qwak.build.v1.GetBuildImageDetailsRequest\x1a/.com.qwak.build.v1.GetBuildImageDetailsResponse\x12h\n\x0fUpdateBuildName\x12).com.qwak.build.v1.UpdateBuildNameRequest\x1a*.com.qwak.build.v1.UpdateBuildNameResponse\x12}\n\x16GetBuildsArtifactsScan\x12\x30.com.qwak.build.v1.GetBuildsArtifactsScanRequest\x1a\x31.com.qwak.build.v1.GetBuildsArtifactsScanResponseB$\n\x11\x63om.qwak.build.v1B\rBuildApiProtoP\x01\x62\x06proto3')

_PHASESTATUS = DESCRIPTOR.enum_types_by_name['PhaseStatus']
PhaseStatus = enum_type_wrapper.EnumTypeWrapper(_PHASESTATUS)
_FAILUREREASON = DESCRIPTOR.enum_types_by_name['FailureReason']
FailureReason = enum_type_wrapper.EnumTypeWrapper(_FAILUREREASON)
PHASE_STATUS_INVALID = 0
PHASE_STATUS_IN_PROGRESS = 1
PHASE_STATUS_SUCCESSFUL = 2
PHASE_STATUS_FAILED = 3
PHASE_STATUS_CANCELLED = 4
FAILURE_REASON_UNSPECIFIED = 0
FAILURE_REASON_AVAILABLE_IN_LOGS = 1
FAILURE_REASON_OUT_OF_MEMORY = 2


_SAVEFRAMEWORKMODELSREQUEST = DESCRIPTOR.message_types_by_name['SaveFrameworkModelsRequest']
_SAVEFRAMEWORKMODELSRESPONSE = DESCRIPTOR.message_types_by_name['SaveFrameworkModelsResponse']
_REGISTERBUILDREQUEST = DESCRIPTOR.message_types_by_name['RegisterBuildRequest']
_REGISTERBUILDRESPONSE = DESCRIPTOR.message_types_by_name['RegisterBuildResponse']
_UPDATEBUILDSTATUSREQUEST = DESCRIPTOR.message_types_by_name['UpdateBuildStatusRequest']
_UPDATEBUILDSTATUSRESPONSE = DESCRIPTOR.message_types_by_name['UpdateBuildStatusResponse']
_REGISTEREXPERIMENTTRACKINGREQUEST = DESCRIPTOR.message_types_by_name['RegisterExperimentTrackingRequest']
_REGISTEREXPERIMENTTRACKINGREQUEST_PARAMSENTRY = _REGISTEREXPERIMENTTRACKINGREQUEST.nested_types_by_name['ParamsEntry']
_REGISTEREXPERIMENTTRACKINGREQUEST_METRICSENTRY = _REGISTEREXPERIMENTTRACKINGREQUEST.nested_types_by_name['MetricsEntry']
_REGISTEREXPERIMENTTRACKINGRESPONSE = DESCRIPTOR.message_types_by_name['RegisterExperimentTrackingResponse']
_REGISTERMODELSCHEMAREQUEST = DESCRIPTOR.message_types_by_name['RegisterModelSchemaRequest']
_REGISTERMODELSCHEMARESPONSE = DESCRIPTOR.message_types_by_name['RegisterModelSchemaResponse']
_GETBUILDREQUEST = DESCRIPTOR.message_types_by_name['GetBuildRequest']
_GETBUILDRESPONSE = DESCRIPTOR.message_types_by_name['GetBuildResponse']
_LISTBUILDSREQUEST = DESCRIPTOR.message_types_by_name['ListBuildsRequest']
_LISTBUILDSRESPONSE = DESCRIPTOR.message_types_by_name['ListBuildsResponse']
_REGISTERTAGSREQUEST = DESCRIPTOR.message_types_by_name['RegisterTagsRequest']
_REGISTERTAGSRESPONSE = DESCRIPTOR.message_types_by_name['RegisterTagsResponse']
_LOGPHASESTATUSREQUEST = DESCRIPTOR.message_types_by_name['LogPhaseStatusRequest']
_LOGPHASESTATUSRESPONSE = DESCRIPTOR.message_types_by_name['LogPhaseStatusResponse']
_GETPHASESTATUSESREQUEST = DESCRIPTOR.message_types_by_name['GetPhaseStatusesRequest']
_PHASESTATUSLOG = DESCRIPTOR.message_types_by_name['PhaseStatusLog']
_GETPHASESTATUSESRESPONSE = DESCRIPTOR.message_types_by_name['GetPhaseStatusesResponse']
_DELETEBUILDREQUEST = DESCRIPTOR.message_types_by_name['DeleteBuildRequest']
_DELETEBUILDRESPONSE = DESCRIPTOR.message_types_by_name['DeleteBuildResponse']
_GETTAGPATHREQUEST = DESCRIPTOR.message_types_by_name['GetTagPathRequest']
_GETTAGPATHRESPONSE = DESCRIPTOR.message_types_by_name['GetTagPathResponse']
_RERUNBUILDFROMEXISTINGREQUEST = DESCRIPTOR.message_types_by_name['RerunBuildFromExistingRequest']
_RERUNBUILDFROMEXISTINGRESPONSE = DESCRIPTOR.message_types_by_name['RerunBuildFromExistingResponse']
_GETBUILDSARTIFACTSSCANSUMMARYREQUEST = DESCRIPTOR.message_types_by_name['GetBuildsArtifactsScanSummaryRequest']
_GETBUILDSARTIFACTSSCANSUMMARYRESPONSE = DESCRIPTOR.message_types_by_name['GetBuildsArtifactsScanSummaryResponse']
_GETBUILDSARTIFACTSSCANSUMMARYRESPONSE_RESULTBYARTIFACTNAMEENTRY = _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE.nested_types_by_name['ResultByArtifactNameEntry']
_GETBUILDIMAGEDETAILSREQUEST = DESCRIPTOR.message_types_by_name['GetBuildImageDetailsRequest']
_GETBUILDIMAGEDETAILSRESPONSE = DESCRIPTOR.message_types_by_name['GetBuildImageDetailsResponse']
_UPDATEBUILDNAMEREQUEST = DESCRIPTOR.message_types_by_name['UpdateBuildNameRequest']
_UPDATEBUILDNAMERESPONSE = DESCRIPTOR.message_types_by_name['UpdateBuildNameResponse']
_GETBUILDSARTIFACTSSCANREQUEST = DESCRIPTOR.message_types_by_name['GetBuildsArtifactsScanRequest']
_GETBUILDSARTIFACTSSCANRESPONSE = DESCRIPTOR.message_types_by_name['GetBuildsArtifactsScanResponse']
SaveFrameworkModelsRequest = _reflection.GeneratedProtocolMessageType('SaveFrameworkModelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVEFRAMEWORKMODELSREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.SaveFrameworkModelsRequest)
  })
_sym_db.RegisterMessage(SaveFrameworkModelsRequest)

SaveFrameworkModelsResponse = _reflection.GeneratedProtocolMessageType('SaveFrameworkModelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _SAVEFRAMEWORKMODELSRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.SaveFrameworkModelsResponse)
  })
_sym_db.RegisterMessage(SaveFrameworkModelsResponse)

RegisterBuildRequest = _reflection.GeneratedProtocolMessageType('RegisterBuildRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERBUILDREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterBuildRequest)
  })
_sym_db.RegisterMessage(RegisterBuildRequest)

RegisterBuildResponse = _reflection.GeneratedProtocolMessageType('RegisterBuildResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERBUILDRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterBuildResponse)
  })
_sym_db.RegisterMessage(RegisterBuildResponse)

UpdateBuildStatusRequest = _reflection.GeneratedProtocolMessageType('UpdateBuildStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBUILDSTATUSREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.UpdateBuildStatusRequest)
  })
_sym_db.RegisterMessage(UpdateBuildStatusRequest)

UpdateBuildStatusResponse = _reflection.GeneratedProtocolMessageType('UpdateBuildStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBUILDSTATUSRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.UpdateBuildStatusResponse)
  })
_sym_db.RegisterMessage(UpdateBuildStatusResponse)

RegisterExperimentTrackingRequest = _reflection.GeneratedProtocolMessageType('RegisterExperimentTrackingRequest', (_message.Message,), {

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTEREXPERIMENTTRACKINGREQUEST_PARAMSENTRY,
    '__module__' : 'qwak.build.v1.build_api_pb2'
    # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterExperimentTrackingRequest.ParamsEntry)
    })
  ,

  'MetricsEntry' : _reflection.GeneratedProtocolMessageType('MetricsEntry', (_message.Message,), {
    'DESCRIPTOR' : _REGISTEREXPERIMENTTRACKINGREQUEST_METRICSENTRY,
    '__module__' : 'qwak.build.v1.build_api_pb2'
    # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterExperimentTrackingRequest.MetricsEntry)
    })
  ,
  'DESCRIPTOR' : _REGISTEREXPERIMENTTRACKINGREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterExperimentTrackingRequest)
  })
_sym_db.RegisterMessage(RegisterExperimentTrackingRequest)
_sym_db.RegisterMessage(RegisterExperimentTrackingRequest.ParamsEntry)
_sym_db.RegisterMessage(RegisterExperimentTrackingRequest.MetricsEntry)

RegisterExperimentTrackingResponse = _reflection.GeneratedProtocolMessageType('RegisterExperimentTrackingResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTEREXPERIMENTTRACKINGRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterExperimentTrackingResponse)
  })
_sym_db.RegisterMessage(RegisterExperimentTrackingResponse)

RegisterModelSchemaRequest = _reflection.GeneratedProtocolMessageType('RegisterModelSchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERMODELSCHEMAREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterModelSchemaRequest)
  })
_sym_db.RegisterMessage(RegisterModelSchemaRequest)

RegisterModelSchemaResponse = _reflection.GeneratedProtocolMessageType('RegisterModelSchemaResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERMODELSCHEMARESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterModelSchemaResponse)
  })
_sym_db.RegisterMessage(RegisterModelSchemaResponse)

GetBuildRequest = _reflection.GeneratedProtocolMessageType('GetBuildRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUILDREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildRequest)
  })
_sym_db.RegisterMessage(GetBuildRequest)

GetBuildResponse = _reflection.GeneratedProtocolMessageType('GetBuildResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBUILDRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildResponse)
  })
_sym_db.RegisterMessage(GetBuildResponse)

ListBuildsRequest = _reflection.GeneratedProtocolMessageType('ListBuildsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUILDSREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.ListBuildsRequest)
  })
_sym_db.RegisterMessage(ListBuildsRequest)

ListBuildsResponse = _reflection.GeneratedProtocolMessageType('ListBuildsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTBUILDSRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.ListBuildsResponse)
  })
_sym_db.RegisterMessage(ListBuildsResponse)

RegisterTagsRequest = _reflection.GeneratedProtocolMessageType('RegisterTagsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTAGSREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterTagsRequest)
  })
_sym_db.RegisterMessage(RegisterTagsRequest)

RegisterTagsResponse = _reflection.GeneratedProtocolMessageType('RegisterTagsResponse', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERTAGSRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RegisterTagsResponse)
  })
_sym_db.RegisterMessage(RegisterTagsResponse)

LogPhaseStatusRequest = _reflection.GeneratedProtocolMessageType('LogPhaseStatusRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGPHASESTATUSREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.LogPhaseStatusRequest)
  })
_sym_db.RegisterMessage(LogPhaseStatusRequest)

LogPhaseStatusResponse = _reflection.GeneratedProtocolMessageType('LogPhaseStatusResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOGPHASESTATUSRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.LogPhaseStatusResponse)
  })
_sym_db.RegisterMessage(LogPhaseStatusResponse)

GetPhaseStatusesRequest = _reflection.GeneratedProtocolMessageType('GetPhaseStatusesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPHASESTATUSESREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetPhaseStatusesRequest)
  })
_sym_db.RegisterMessage(GetPhaseStatusesRequest)

PhaseStatusLog = _reflection.GeneratedProtocolMessageType('PhaseStatusLog', (_message.Message,), {
  'DESCRIPTOR' : _PHASESTATUSLOG,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.PhaseStatusLog)
  })
_sym_db.RegisterMessage(PhaseStatusLog)

GetPhaseStatusesResponse = _reflection.GeneratedProtocolMessageType('GetPhaseStatusesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPHASESTATUSESRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetPhaseStatusesResponse)
  })
_sym_db.RegisterMessage(GetPhaseStatusesResponse)

DeleteBuildRequest = _reflection.GeneratedProtocolMessageType('DeleteBuildRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBUILDREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.DeleteBuildRequest)
  })
_sym_db.RegisterMessage(DeleteBuildRequest)

DeleteBuildResponse = _reflection.GeneratedProtocolMessageType('DeleteBuildResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEBUILDRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.DeleteBuildResponse)
  })
_sym_db.RegisterMessage(DeleteBuildResponse)

GetTagPathRequest = _reflection.GeneratedProtocolMessageType('GetTagPathRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETTAGPATHREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetTagPathRequest)
  })
_sym_db.RegisterMessage(GetTagPathRequest)

GetTagPathResponse = _reflection.GeneratedProtocolMessageType('GetTagPathResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETTAGPATHRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetTagPathResponse)
  })
_sym_db.RegisterMessage(GetTagPathResponse)

RerunBuildFromExistingRequest = _reflection.GeneratedProtocolMessageType('RerunBuildFromExistingRequest', (_message.Message,), {
  'DESCRIPTOR' : _RERUNBUILDFROMEXISTINGREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RerunBuildFromExistingRequest)
  })
_sym_db.RegisterMessage(RerunBuildFromExistingRequest)

RerunBuildFromExistingResponse = _reflection.GeneratedProtocolMessageType('RerunBuildFromExistingResponse', (_message.Message,), {
  'DESCRIPTOR' : _RERUNBUILDFROMEXISTINGRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.RerunBuildFromExistingResponse)
  })
_sym_db.RegisterMessage(RerunBuildFromExistingResponse)

GetBuildsArtifactsScanSummaryRequest = _reflection.GeneratedProtocolMessageType('GetBuildsArtifactsScanSummaryRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUILDSARTIFACTSSCANSUMMARYREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildsArtifactsScanSummaryRequest)
  })
_sym_db.RegisterMessage(GetBuildsArtifactsScanSummaryRequest)

GetBuildsArtifactsScanSummaryResponse = _reflection.GeneratedProtocolMessageType('GetBuildsArtifactsScanSummaryResponse', (_message.Message,), {

  'ResultByArtifactNameEntry' : _reflection.GeneratedProtocolMessageType('ResultByArtifactNameEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE_RESULTBYARTIFACTNAMEENTRY,
    '__module__' : 'qwak.build.v1.build_api_pb2'
    # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildsArtifactsScanSummaryResponse.ResultByArtifactNameEntry)
    })
  ,
  'DESCRIPTOR' : _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildsArtifactsScanSummaryResponse)
  })
_sym_db.RegisterMessage(GetBuildsArtifactsScanSummaryResponse)
_sym_db.RegisterMessage(GetBuildsArtifactsScanSummaryResponse.ResultByArtifactNameEntry)

GetBuildImageDetailsRequest = _reflection.GeneratedProtocolMessageType('GetBuildImageDetailsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUILDIMAGEDETAILSREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildImageDetailsRequest)
  })
_sym_db.RegisterMessage(GetBuildImageDetailsRequest)

GetBuildImageDetailsResponse = _reflection.GeneratedProtocolMessageType('GetBuildImageDetailsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBUILDIMAGEDETAILSRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildImageDetailsResponse)
  })
_sym_db.RegisterMessage(GetBuildImageDetailsResponse)

UpdateBuildNameRequest = _reflection.GeneratedProtocolMessageType('UpdateBuildNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBUILDNAMEREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.UpdateBuildNameRequest)
  })
_sym_db.RegisterMessage(UpdateBuildNameRequest)

UpdateBuildNameResponse = _reflection.GeneratedProtocolMessageType('UpdateBuildNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEBUILDNAMERESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.UpdateBuildNameResponse)
  })
_sym_db.RegisterMessage(UpdateBuildNameResponse)

GetBuildsArtifactsScanRequest = _reflection.GeneratedProtocolMessageType('GetBuildsArtifactsScanRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBUILDSARTIFACTSSCANREQUEST,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildsArtifactsScanRequest)
  })
_sym_db.RegisterMessage(GetBuildsArtifactsScanRequest)

GetBuildsArtifactsScanResponse = _reflection.GeneratedProtocolMessageType('GetBuildsArtifactsScanResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBUILDSARTIFACTSSCANRESPONSE,
  '__module__' : 'qwak.build.v1.build_api_pb2'
  # @@protoc_insertion_point(class_scope:com.qwak.build.v1.GetBuildsArtifactsScanResponse)
  })
_sym_db.RegisterMessage(GetBuildsArtifactsScanResponse)

_BUILDAPI = DESCRIPTOR.services_by_name['BuildAPI']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021com.qwak.build.v1B\rBuildApiProtoP\001'
  _REGISTEREXPERIMENTTRACKINGREQUEST_PARAMSENTRY._options = None
  _REGISTEREXPERIMENTTRACKINGREQUEST_PARAMSENTRY._serialized_options = b'8\001'
  _REGISTEREXPERIMENTTRACKINGREQUEST_METRICSENTRY._options = None
  _REGISTEREXPERIMENTTRACKINGREQUEST_METRICSENTRY._serialized_options = b'8\001'
  _LISTBUILDSREQUEST.fields_by_name['branch_id']._options = None
  _LISTBUILDSREQUEST.fields_by_name['branch_id']._serialized_options = b'\030\001'
  _GETBUILDSARTIFACTSSCANSUMMARYREQUEST.fields_by_name['artifact_name']._options = None
  _GETBUILDSARTIFACTSSCANSUMMARYREQUEST.fields_by_name['artifact_name']._serialized_options = b'\030\001'
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE_RESULTBYARTIFACTNAMEENTRY._options = None
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE_RESULTBYARTIFACTNAMEENTRY._serialized_options = b'8\001'
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE.fields_by_name['result']._options = None
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE.fields_by_name['result']._serialized_options = b'\030\001'
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE.fields_by_name['ui_direct_link']._options = None
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE.fields_by_name['ui_direct_link']._serialized_options = b'\030\001'
  _PHASESTATUS._serialized_start=3403
  _PHASESTATUS._serialized_end=3554
  _FAILUREREASON._serialized_start=3556
  _FAILUREREASON._serialized_end=3675
  _SAVEFRAMEWORKMODELSREQUEST._serialized_start=197
  _SAVEFRAMEWORKMODELSREQUEST._serialized_end=279
  _SAVEFRAMEWORKMODELSRESPONSE._serialized_start=281
  _SAVEFRAMEWORKMODELSRESPONSE._serialized_end=310
  _REGISTERBUILDREQUEST._serialized_start=312
  _REGISTERBUILDREQUEST._serialized_end=436
  _REGISTERBUILDRESPONSE._serialized_start=438
  _REGISTERBUILDRESPONSE._serialized_end=461
  _UPDATEBUILDSTATUSREQUEST._serialized_start=463
  _UPDATEBUILDSTATUSREQUEST._serialized_end=560
  _UPDATEBUILDSTATUSRESPONSE._serialized_start=562
  _UPDATEBUILDSTATUSRESPONSE._serialized_end=589
  _REGISTEREXPERIMENTTRACKINGREQUEST._serialized_start=592
  _REGISTEREXPERIMENTTRACKINGREQUEST._serialized_end=906
  _REGISTEREXPERIMENTTRACKINGREQUEST_PARAMSENTRY._serialized_start=813
  _REGISTEREXPERIMENTTRACKINGREQUEST_PARAMSENTRY._serialized_end=858
  _REGISTEREXPERIMENTTRACKINGREQUEST_METRICSENTRY._serialized_start=860
  _REGISTEREXPERIMENTTRACKINGREQUEST_METRICSENTRY._serialized_end=906
  _REGISTEREXPERIMENTTRACKINGRESPONSE._serialized_start=908
  _REGISTEREXPERIMENTTRACKINGRESPONSE._serialized_end=944
  _REGISTERMODELSCHEMAREQUEST._serialized_start=946
  _REGISTERMODELSCHEMAREQUEST._serialized_end=1046
  _REGISTERMODELSCHEMARESPONSE._serialized_start=1048
  _REGISTERMODELSCHEMARESPONSE._serialized_end=1077
  _GETBUILDREQUEST._serialized_start=1079
  _GETBUILDREQUEST._serialized_end=1114
  _GETBUILDRESPONSE._serialized_start=1116
  _GETBUILDRESPONSE._serialized_end=1175
  _LISTBUILDSREQUEST._serialized_start=1177
  _LISTBUILDSREQUEST._serialized_end=1287
  _LISTBUILDSRESPONSE._serialized_start=1289
  _LISTBUILDSRESPONSE._serialized_end=1350
  _REGISTERTAGSREQUEST._serialized_start=1352
  _REGISTERTAGSREQUEST._serialized_end=1405
  _REGISTERTAGSRESPONSE._serialized_start=1407
  _REGISTERTAGSRESPONSE._serialized_end=1429
  _LOGPHASESTATUSREQUEST._serialized_start=1432
  _LOGPHASESTATUSREQUEST._serialized_end=1574
  _LOGPHASESTATUSRESPONSE._serialized_start=1576
  _LOGPHASESTATUSRESPONSE._serialized_end=1600
  _GETPHASESTATUSESREQUEST._serialized_start=1602
  _GETPHASESTATUSESREQUEST._serialized_end=1645
  _PHASESTATUSLOG._serialized_start=1648
  _PHASESTATUSLOG._serialized_end=1929
  _GETPHASESTATUSESRESPONSE._serialized_start=1931
  _GETPHASESTATUSESRESPONSE._serialized_end=2010
  _DELETEBUILDREQUEST._serialized_start=2012
  _DELETEBUILDREQUEST._serialized_end=2051
  _DELETEBUILDRESPONSE._serialized_start=2053
  _DELETEBUILDRESPONSE._serialized_end=2074
  _GETTAGPATHREQUEST._serialized_start=2076
  _GETTAGPATHREQUEST._serialized_end=2173
  _GETTAGPATHRESPONSE._serialized_start=2175
  _GETTAGPATHRESPONSE._serialized_end=2213
  _RERUNBUILDFROMEXISTINGREQUEST._serialized_start=2216
  _RERUNBUILDFROMEXISTINGREQUEST._serialized_end=2508
  _RERUNBUILDFROMEXISTINGRESPONSE._serialized_start=2510
  _RERUNBUILDFROMEXISTINGRESPONSE._serialized_end=2542
  _GETBUILDSARTIFACTSSCANSUMMARYREQUEST._serialized_start=2544
  _GETBUILDSARTIFACTSSCANSUMMARYREQUEST._serialized_end=2627
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE._serialized_start=2630
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE._serialized_end=2971
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE_RESULTBYARTIFACTNAMEENTRY._serialized_start=2874
  _GETBUILDSARTIFACTSSCANSUMMARYRESPONSE_RESULTBYARTIFACTNAMEENTRY._serialized_end=2971
  _GETBUILDIMAGEDETAILSREQUEST._serialized_start=2973
  _GETBUILDIMAGEDETAILSREQUEST._serialized_end=3044
  _GETBUILDIMAGEDETAILSRESPONSE._serialized_start=3046
  _GETBUILDIMAGEDETAILSRESPONSE._serialized_end=3143
  _UPDATEBUILDNAMEREQUEST._serialized_start=3145
  _UPDATEBUILDNAMEREQUEST._serialized_end=3207
  _UPDATEBUILDNAMERESPONSE._serialized_start=3209
  _UPDATEBUILDNAMERESPONSE._serialized_end=3234
  _GETBUILDSARTIFACTSSCANREQUEST._serialized_start=3236
  _GETBUILDSARTIFACTSSCANREQUEST._serialized_end=3348
  _GETBUILDSARTIFACTSSCANRESPONSE._serialized_start=3350
  _GETBUILDSARTIFACTSSCANRESPONSE._serialized_end=3400
  _BUILDAPI._serialized_start=3678
  _BUILDAPI._serialized_end=5576
# @@protoc_insertion_point(module_scope)
