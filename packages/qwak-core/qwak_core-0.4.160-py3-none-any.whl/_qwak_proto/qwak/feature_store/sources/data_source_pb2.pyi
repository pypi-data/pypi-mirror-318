"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import qwak.feature_store.sources.batch_pb2
import qwak.feature_store.sources.data_source_attribute_pb2
import qwak.feature_store.sources.streaming_pb2
import qwak.feature_store.v1.common.source_code.source_code_pb2
import sys
import typing

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class DataSource(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_SOURCE_DEFINITION_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    FEATURE_SETS_FIELD_NUMBER: builtins.int
    @property
    def data_source_definition(self) -> global___DataSourceDefinition:
        """Complete domain definition of the data source"""
    @property
    def metadata(self) -> global___DataSourceMetadata:
        """System generated metadata of the data source"""
    @property
    def feature_sets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___FeatureSetBrief]:
        """Linked feature sets"""
    def __init__(
        self,
        *,
        data_source_definition: global___DataSourceDefinition | None = ...,
        metadata: global___DataSourceMetadata | None = ...,
        feature_sets: collections.abc.Iterable[global___FeatureSetBrief] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data_source_definition", b"data_source_definition", "metadata", b"metadata"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_source_definition", b"data_source_definition", "feature_sets", b"feature_sets", "metadata", b"metadata"]) -> None: ...

global___DataSource = DataSource

class DataSourceDefinition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DATA_SOURCE_ID_FIELD_NUMBER: builtins.int
    DATA_SOURCE_SPEC_FIELD_NUMBER: builtins.int
    data_source_id: builtins.str
    """Assigned unique id"""
    @property
    def data_source_spec(self) -> global___DataSourceSpec:
        """Specifications of the data source"""
    def __init__(
        self,
        *,
        data_source_id: builtins.str = ...,
        data_source_spec: global___DataSourceSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["data_source_spec", b"data_source_spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["data_source_id", b"data_source_id", "data_source_spec", b"data_source_spec"]) -> None: ...

global___DataSourceDefinition = DataSourceDefinition

class DataSourceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_AT_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_BY_FIELD_NUMBER: builtins.int
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """When the data source was created"""
    created_by: builtins.str
    """Created by"""
    @property
    def last_modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Last modified"""
    last_modified_by: builtins.str
    """Last modified by"""
    def __init__(
        self,
        *,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        last_modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_modified_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "last_modified_at", b"last_modified_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["created_at", b"created_at", "created_by", b"created_by", "last_modified_at", b"last_modified_at", "last_modified_by", b"last_modified_by"]) -> None: ...

global___DataSourceMetadata = DataSourceMetadata

class DataSourceSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BATCH_SOURCE_FIELD_NUMBER: builtins.int
    STREAM_SOURCE_FIELD_NUMBER: builtins.int
    SOURCE_CODE_SPEC_FIELD_NUMBER: builtins.int
    DATA_SOURCE_ATTRIBUTES_FIELD_NUMBER: builtins.int
    FEATURESET_REPOSITORY_NAME_FIELD_NUMBER: builtins.int
    @property
    def batch_source(self) -> qwak.feature_store.sources.batch_pb2.BatchSource: ...
    @property
    def stream_source(self) -> qwak.feature_store.sources.streaming_pb2.StreamingSource: ...
    @property
    def source_code_spec(self) -> qwak.feature_store.v1.common.source_code.source_code_pb2.SourceCodeSpec: ...
    @property
    def data_source_attributes(self) -> qwak.feature_store.sources.data_source_attribute_pb2.DataSourceAttributes:
        """Data source attributes"""
    featureset_repository_name: builtins.str
    """Featureset repository name"""
    def __init__(
        self,
        *,
        batch_source: qwak.feature_store.sources.batch_pb2.BatchSource | None = ...,
        stream_source: qwak.feature_store.sources.streaming_pb2.StreamingSource | None = ...,
        source_code_spec: qwak.feature_store.v1.common.source_code.source_code_pb2.SourceCodeSpec | None = ...,
        data_source_attributes: qwak.feature_store.sources.data_source_attribute_pb2.DataSourceAttributes | None = ...,
        featureset_repository_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["batch_source", b"batch_source", "data_source_attributes", b"data_source_attributes", "featureset_repository_identifier", b"featureset_repository_identifier", "featureset_repository_name", b"featureset_repository_name", "source_code_spec", b"source_code_spec", "stream_source", b"stream_source", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["batch_source", b"batch_source", "data_source_attributes", b"data_source_attributes", "featureset_repository_identifier", b"featureset_repository_identifier", "featureset_repository_name", b"featureset_repository_name", "source_code_spec", b"source_code_spec", "stream_source", b"stream_source", "type", b"type"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["featureset_repository_identifier", b"featureset_repository_identifier"]) -> typing_extensions.Literal["featureset_repository_name"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["batch_source", "stream_source"] | None: ...

global___DataSourceSpec = DataSourceSpec

class FeatureSetBrief(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURE_SET_ID_FIELD_NUMBER: builtins.int
    FEATURE_SET_NAME_FIELD_NUMBER: builtins.int
    FEATURE_SET_TYPE_FIELD_NUMBER: builtins.int
    feature_set_id: builtins.str
    """Feature set id"""
    feature_set_name: builtins.str
    """Feature set name"""
    feature_set_type: builtins.int
    """Feature set type"""
    def __init__(
        self,
        *,
        feature_set_id: builtins.str = ...,
        feature_set_name: builtins.str = ...,
        feature_set_type: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["feature_set_id", b"feature_set_id", "feature_set_name", b"feature_set_name", "feature_set_type", b"feature_set_type"]) -> None: ...

global___FeatureSetBrief = FeatureSetBrief
