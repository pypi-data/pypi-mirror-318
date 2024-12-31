"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class RowLevelStreamingAggregationIngestion(google.protobuf.message.Message):
    """Row Level Ingestion"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURESET_NAME_FIELD_NUMBER: builtins.int
    featureset_name: builtins.str
    def __init__(
        self,
        *,
        featureset_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["featureset_name", b"featureset_name"]) -> None: ...

global___RowLevelStreamingAggregationIngestion = RowLevelStreamingAggregationIngestion

class CompactionStreamingAggregationIngestion(google.protobuf.message.Message):
    """Offline Ingestion"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURESET_NAME_FIELD_NUMBER: builtins.int
    SCHEDULED_COMPACTION_FIELD_NUMBER: builtins.int
    MANUAL_COMPACTION_FIELD_NUMBER: builtins.int
    featureset_name: builtins.str
    @property
    def scheduled_compaction(self) -> global___ScheduledCompaction: ...
    @property
    def manual_compaction(self) -> global___ManualCompaction: ...
    def __init__(
        self,
        *,
        featureset_name: builtins.str = ...,
        scheduled_compaction: global___ScheduledCompaction | None = ...,
        manual_compaction: global___ManualCompaction | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["manual_compaction", b"manual_compaction", "scheduled_compaction", b"scheduled_compaction", "trigger_type", b"trigger_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["featureset_name", b"featureset_name", "manual_compaction", b"manual_compaction", "scheduled_compaction", b"scheduled_compaction", "trigger_type", b"trigger_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["trigger_type", b"trigger_type"]) -> typing_extensions.Literal["scheduled_compaction", "manual_compaction"] | None: ...

global___CompactionStreamingAggregationIngestion = CompactionStreamingAggregationIngestion

class ScheduledCompaction(google.protobuf.message.Message):
    """Scheduled Compaction ingestion (e.g., AirFlow)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ScheduledCompaction = ScheduledCompaction

class ManualCompaction(google.protobuf.message.Message):
    """Manual Compaction ingestion (that is, someone manually running from the UI)"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ManualCompaction = ManualCompaction

class StreamingAggregationBackfillIngestion(google.protobuf.message.Message):
    """Streaming Aggregation Backfill"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FEATURESET_NAME_FIELD_NUMBER: builtins.int
    featureset_name: builtins.str
    def __init__(
        self,
        *,
        featureset_name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["featureset_name", b"featureset_name"]) -> None: ...

global___StreamingAggregationBackfillIngestion = StreamingAggregationBackfillIngestion
