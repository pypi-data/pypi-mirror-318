"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import qwak.offline.serving.v1.feature_values_pb2
import qwak.offline.serving.v1.options_pb2
import qwak.offline.serving.v1.population_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _FeatureValuesRequestStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FeatureValuesRequestStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FeatureValuesRequestStatus.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FEATURE_VALUES_REQUEST_STATUS_INVALID: _FeatureValuesRequestStatus.ValueType  # 0
    """Invalid status"""
    FEATURE_VALUES_REQUEST_STATUS_SUCCEEDED: _FeatureValuesRequestStatus.ValueType  # 1
    """Request Success"""
    FEATURE_VALUES_REQUEST_STATUS_PENDING: _FeatureValuesRequestStatus.ValueType  # 2
    """Request Pending"""
    FEATURE_VALUES_REQUEST_STATUS_CANCELLED: _FeatureValuesRequestStatus.ValueType  # 3
    """Request Canceled"""
    FEATURE_VALUES_REQUEST_STATUS_FAILED: _FeatureValuesRequestStatus.ValueType  # 4
    """Request Failed"""

class FeatureValuesRequestStatus(_FeatureValuesRequestStatus, metaclass=_FeatureValuesRequestStatusEnumTypeWrapper): ...

FEATURE_VALUES_REQUEST_STATUS_INVALID: FeatureValuesRequestStatus.ValueType  # 0
"""Invalid status"""
FEATURE_VALUES_REQUEST_STATUS_SUCCEEDED: FeatureValuesRequestStatus.ValueType  # 1
"""Request Success"""
FEATURE_VALUES_REQUEST_STATUS_PENDING: FeatureValuesRequestStatus.ValueType  # 2
"""Request Pending"""
FEATURE_VALUES_REQUEST_STATUS_CANCELLED: FeatureValuesRequestStatus.ValueType  # 3
"""Request Canceled"""
FEATURE_VALUES_REQUEST_STATUS_FAILED: FeatureValuesRequestStatus.ValueType  # 4
"""Request Failed"""
global___FeatureValuesRequestStatus = FeatureValuesRequestStatus

class _FileFormat:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _FileFormatEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_FileFormat.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    FILE_FORMAT_INVALID: _FileFormat.ValueType  # 0
    """Invalid format"""
    FILE_FORMAT_CSV: _FileFormat.ValueType  # 1
    """Csv format"""

class FileFormat(_FileFormat, metaclass=_FileFormatEnumTypeWrapper): ...

FILE_FORMAT_INVALID: FileFormat.ValueType  # 0
"""Invalid format"""
FILE_FORMAT_CSV: FileFormat.ValueType  # 1
"""Csv format"""
global___FileFormat = FileFormat

class GetFileUploadUrlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POPULATION_FIELD_NUMBER: builtins.int
    @property
    def population(self) -> qwak.offline.serving.v1.population_pb2.PopulationFileUploadUrlType:
        """Used to Get File Upload Url for population dataset"""
    def __init__(
        self,
        *,
        population: qwak.offline.serving.v1.population_pb2.PopulationFileUploadUrlType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["population", b"population", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["population", b"population", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["population"] | None: ...

global___GetFileUploadUrlRequest = GetFileUploadUrlRequest

class GetFileUploadUrlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FILE_UPLOAD_URL_FIELD_NUMBER: builtins.int
    file_upload_url: builtins.str
    """The generated url to which the file can be uploaded"""
    def __init__(
        self,
        *,
        file_upload_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["file_upload_url", b"file_upload_url"]) -> None: ...

global___GetFileUploadUrlResponse = GetFileUploadUrlResponse

class GetFeatureValuesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURES_FIELD_NUMBER: builtins.int
    POPULATION_FIELD_NUMBER: builtins.int
    RESULT_FILE_FORMAT_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def features(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[qwak.offline.serving.v1.feature_values_pb2.FeaturesetFeatures]:
        """a List of featureset name and it's feature names"""
    @property
    def population(self) -> qwak.offline.serving.v1.population_pb2.TimedPopulation:
        """The population dataset with timestamp column"""
    result_file_format: global___FileFormat.ValueType
    """The format of the result files"""
    @property
    def options(self) -> qwak.offline.serving.v1.options_pb2.OfflineServingQueryOptions:
        """Query Options"""
    def __init__(
        self,
        *,
        features: collections.abc.Iterable[qwak.offline.serving.v1.feature_values_pb2.FeaturesetFeatures] | None = ...,
        population: qwak.offline.serving.v1.population_pb2.TimedPopulation | None = ...,
        result_file_format: global___FileFormat.ValueType = ...,
        options: qwak.offline.serving.v1.options_pb2.OfflineServingQueryOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options", b"options", "population", b"population"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["features", b"features", "options", b"options", "population", b"population", "result_file_format", b"result_file_format"]) -> None: ...

global___GetFeatureValuesRequest = GetFeatureValuesRequest

class GetFeatureValuesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """The request_id. used as a handler to retrieve results"""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["request_id", b"request_id"]) -> None: ...

global___GetFeatureValuesResponse = GetFeatureValuesResponse

class GetFeatureValuesInRangeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURES_FIELD_NUMBER: builtins.int
    LOWER_TIME_BOUND_FIELD_NUMBER: builtins.int
    UPPER_TIME_BOUND_FIELD_NUMBER: builtins.int
    POPULATION_FIELD_NUMBER: builtins.int
    RESULT_FILE_FORMAT_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def features(self) -> qwak.offline.serving.v1.feature_values_pb2.FeaturesetFeatures:
        """A single featureset name and it's feature names"""
    @property
    def lower_time_bound(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Lower time bound for range query"""
    @property
    def upper_time_bound(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Upper time bound for range query"""
    @property
    def population(self) -> qwak.offline.serving.v1.population_pb2.Population: ...
    result_file_format: global___FileFormat.ValueType
    """The format of the result files"""
    @property
    def options(self) -> qwak.offline.serving.v1.options_pb2.OfflineServingQueryOptions:
        """Query Options"""
    def __init__(
        self,
        *,
        features: qwak.offline.serving.v1.feature_values_pb2.FeaturesetFeatures | None = ...,
        lower_time_bound: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        upper_time_bound: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        population: qwak.offline.serving.v1.population_pb2.Population | None = ...,
        result_file_format: global___FileFormat.ValueType = ...,
        options: qwak.offline.serving.v1.options_pb2.OfflineServingQueryOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["features", b"features", "lower_time_bound", b"lower_time_bound", "optional_population", b"optional_population", "options", b"options", "population", b"population", "upper_time_bound", b"upper_time_bound"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["features", b"features", "lower_time_bound", b"lower_time_bound", "optional_population", b"optional_population", "options", b"options", "population", b"population", "result_file_format", b"result_file_format", "upper_time_bound", b"upper_time_bound"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["optional_population", b"optional_population"]) -> typing_extensions.Literal["population"] | None: ...

global___GetFeatureValuesInRangeRequest = GetFeatureValuesInRangeRequest

class GetFeatureValuesInRangeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """The request_id. used as a handler to retrieve results"""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["request_id", b"request_id"]) -> None: ...

global___GetFeatureValuesInRangeResponse = GetFeatureValuesInRangeResponse

class GetFeatureValuesResultRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    """The request_id handler returned by one of the Get-Feature-Values endpoints"""
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["request_id", b"request_id"]) -> None: ...

global___GetFeatureValuesResultRequest = GetFeatureValuesResultRequest

class GetFeatureValuesResultResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    LINK_TO_FILES_FIELD_NUMBER: builtins.int
    FAILURE_REASON_FIELD_NUMBER: builtins.int
    status: global___FeatureValuesRequestStatus.ValueType
    """The status of the request"""
    @property
    def link_to_files(self) -> global___LinkToFiles: ...
    @property
    def failure_reason(self) -> global___FailureReason: ...
    def __init__(
        self,
        *,
        status: global___FeatureValuesRequestStatus.ValueType = ...,
        link_to_files: global___LinkToFiles | None = ...,
        failure_reason: global___FailureReason | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["failure_reason", b"failure_reason", "link_to_files", b"link_to_files", "payload", b"payload"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["failure_reason", b"failure_reason", "link_to_files", b"link_to_files", "payload", b"payload", "status", b"status"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["payload", b"payload"]) -> typing_extensions.Literal["link_to_files", "failure_reason"] | None: ...

global___GetFeatureValuesResultResponse = GetFeatureValuesResultResponse

class FailureReason(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MESSAGE_FIELD_NUMBER: builtins.int
    message: builtins.str
    """Failure reason"""
    def __init__(
        self,
        *,
        message: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["message", b"message"]) -> None: ...

global___FailureReason = FailureReason

class LinkToFiles(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LINK_TO_FILES_FIELD_NUMBER: builtins.int
    @property
    def link_to_files(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of urls to the files"""
    def __init__(
        self,
        *,
        link_to_files: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["link_to_files", b"link_to_files"]) -> None: ...

global___LinkToFiles = LinkToFiles
