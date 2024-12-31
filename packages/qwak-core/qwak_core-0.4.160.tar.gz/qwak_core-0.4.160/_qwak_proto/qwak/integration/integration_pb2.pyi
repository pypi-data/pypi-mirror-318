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
import qwak.integration.hugging_face_integration_pb2
import qwak.integration.open_a_i_integration_pb2
import qwak.integration.opsgenie_integration_pb2
import qwak.integration.pagerduty_integration_pb2
import qwak.integration.slack_app_integration_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _IntegrationType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _IntegrationTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_IntegrationType.ValueType], builtins.type):  # noqa: F821
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    INTEGRATION_TYPE_INVALID: _IntegrationType.ValueType  # 0
    INTEGRATION_TYPE_JFROG: _IntegrationType.ValueType  # 1
    INTEGRATION_TYPE_OPSGENIE: _IntegrationType.ValueType  # 2
    INTEGRATION_TYPE_PAGERDUTY: _IntegrationType.ValueType  # 3
    INTEGRATION_TYPE_QWAK_SLACK_APP: _IntegrationType.ValueType  # 4
    INTEGRATION_TYPE_OPENAI: _IntegrationType.ValueType  # 5
    INTEGRATION_TYPE_HUGGING_FACE: _IntegrationType.ValueType  # 6

class IntegrationType(_IntegrationType, metaclass=_IntegrationTypeEnumTypeWrapper): ...

INTEGRATION_TYPE_INVALID: IntegrationType.ValueType  # 0
INTEGRATION_TYPE_JFROG: IntegrationType.ValueType  # 1
INTEGRATION_TYPE_OPSGENIE: IntegrationType.ValueType  # 2
INTEGRATION_TYPE_PAGERDUTY: IntegrationType.ValueType  # 3
INTEGRATION_TYPE_QWAK_SLACK_APP: IntegrationType.ValueType  # 4
INTEGRATION_TYPE_OPENAI: IntegrationType.ValueType  # 5
INTEGRATION_TYPE_HUGGING_FACE: IntegrationType.ValueType  # 6
global___IntegrationType = IntegrationType

class Integration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTEGRATION_ID_FIELD_NUMBER: builtins.int
    JFROG_INTEGRATION_FIELD_NUMBER: builtins.int
    OPSGENIE_INTEGRATION_FIELD_NUMBER: builtins.int
    PAGERDUTY_INTEGRATION_FIELD_NUMBER: builtins.int
    QWAK_SLACK_APP_INTEGRATION_FIELD_NUMBER: builtins.int
    OPENAI_INTEGRATION_FIELD_NUMBER: builtins.int
    HUGGING_FACE_INTEGRATION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    integration_id: builtins.str
    @property
    def jfrog_integration(self) -> global___JFrogIntegration: ...
    @property
    def opsgenie_integration(self) -> qwak.integration.opsgenie_integration_pb2.OpsgenieIntegration: ...
    @property
    def pagerduty_integration(self) -> qwak.integration.pagerduty_integration_pb2.PagerdutyIntegration: ...
    @property
    def qwak_slack_app_integration(self) -> qwak.integration.slack_app_integration_pb2.SlackAppIntegration: ...
    @property
    def openai_integration(self) -> qwak.integration.open_a_i_integration_pb2.OpenAIIntegration: ...
    @property
    def hugging_face_integration(self) -> qwak.integration.hugging_face_integration_pb2.HuggingFaceIntegration: ...
    name: builtins.str
    """Integration Name"""
    def __init__(
        self,
        *,
        integration_id: builtins.str = ...,
        jfrog_integration: global___JFrogIntegration | None = ...,
        opsgenie_integration: qwak.integration.opsgenie_integration_pb2.OpsgenieIntegration | None = ...,
        pagerduty_integration: qwak.integration.pagerduty_integration_pb2.PagerdutyIntegration | None = ...,
        qwak_slack_app_integration: qwak.integration.slack_app_integration_pb2.SlackAppIntegration | None = ...,
        openai_integration: qwak.integration.open_a_i_integration_pb2.OpenAIIntegration | None = ...,
        hugging_face_integration: qwak.integration.hugging_face_integration_pb2.HuggingFaceIntegration | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hugging_face_integration", b"hugging_face_integration", "jfrog_integration", b"jfrog_integration", "openai_integration", b"openai_integration", "opsgenie_integration", b"opsgenie_integration", "pagerduty_integration", b"pagerduty_integration", "qwak_slack_app_integration", b"qwak_slack_app_integration", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hugging_face_integration", b"hugging_face_integration", "integration_id", b"integration_id", "jfrog_integration", b"jfrog_integration", "name", b"name", "openai_integration", b"openai_integration", "opsgenie_integration", b"opsgenie_integration", "pagerduty_integration", b"pagerduty_integration", "qwak_slack_app_integration", b"qwak_slack_app_integration", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["jfrog_integration", "opsgenie_integration", "pagerduty_integration", "qwak_slack_app_integration", "openai_integration", "hugging_face_integration"] | None: ...

global___Integration = Integration

class IntegrationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JFROG_INTEGRATION_SPEC_FIELD_NUMBER: builtins.int
    OPSGENIE_INTEGRATION_SPEC_FIELD_NUMBER: builtins.int
    PAGERDUTY_INTEGRATION_SPEC_FIELD_NUMBER: builtins.int
    QWAK_SLACK_APP_INTEGRATION_SPEC_FIELD_NUMBER: builtins.int
    OPENAI_INTEGRATION_SPEC_FIELD_NUMBER: builtins.int
    HUGGING_FACE_INTEGRATION_SPEC_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    @property
    def jfrog_integration_spec(self) -> global___JFrogIntegrationSpec: ...
    @property
    def opsgenie_integration_spec(self) -> qwak.integration.opsgenie_integration_pb2.OpsgenieIntegrationSpec: ...
    @property
    def pagerduty_integration_spec(self) -> qwak.integration.pagerduty_integration_pb2.PagerdutyIntegrationSpec: ...
    @property
    def qwak_slack_app_integration_spec(self) -> qwak.integration.slack_app_integration_pb2.SlackAppIntegrationSpec: ...
    @property
    def openai_integration_spec(self) -> qwak.integration.open_a_i_integration_pb2.OpenAIIntegrationSpec: ...
    @property
    def hugging_face_integration_spec(self) -> qwak.integration.hugging_face_integration_pb2.HuggingFaceIntegrationSpec: ...
    name: builtins.str
    """Integration Name"""
    def __init__(
        self,
        *,
        jfrog_integration_spec: global___JFrogIntegrationSpec | None = ...,
        opsgenie_integration_spec: qwak.integration.opsgenie_integration_pb2.OpsgenieIntegrationSpec | None = ...,
        pagerduty_integration_spec: qwak.integration.pagerduty_integration_pb2.PagerdutyIntegrationSpec | None = ...,
        qwak_slack_app_integration_spec: qwak.integration.slack_app_integration_pb2.SlackAppIntegrationSpec | None = ...,
        openai_integration_spec: qwak.integration.open_a_i_integration_pb2.OpenAIIntegrationSpec | None = ...,
        hugging_face_integration_spec: qwak.integration.hugging_face_integration_pb2.HuggingFaceIntegrationSpec | None = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hugging_face_integration_spec", b"hugging_face_integration_spec", "jfrog_integration_spec", b"jfrog_integration_spec", "openai_integration_spec", b"openai_integration_spec", "opsgenie_integration_spec", b"opsgenie_integration_spec", "pagerduty_integration_spec", b"pagerduty_integration_spec", "qwak_slack_app_integration_spec", b"qwak_slack_app_integration_spec", "spec", b"spec"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hugging_face_integration_spec", b"hugging_face_integration_spec", "jfrog_integration_spec", b"jfrog_integration_spec", "name", b"name", "openai_integration_spec", b"openai_integration_spec", "opsgenie_integration_spec", b"opsgenie_integration_spec", "pagerduty_integration_spec", b"pagerduty_integration_spec", "qwak_slack_app_integration_spec", b"qwak_slack_app_integration_spec", "spec", b"spec"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["spec", b"spec"]) -> typing_extensions.Literal["jfrog_integration_spec", "opsgenie_integration_spec", "pagerduty_integration_spec", "qwak_slack_app_integration_spec", "openai_integration_spec", "hugging_face_integration_spec"] | None: ...

global___IntegrationSpec = IntegrationSpec

class JFrogIntegration(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JFROG_SETTINGS_FIELD_NUMBER: builtins.int
    @property
    def jfrog_settings(self) -> global___JFrogSettings: ...
    def __init__(
        self,
        *,
        jfrog_settings: global___JFrogSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["jfrog_settings", b"jfrog_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["jfrog_settings", b"jfrog_settings"]) -> None: ...

global___JFrogIntegration = JFrogIntegration

class JFrogIntegrationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADMIN_TOKEN_FIELD_NUMBER: builtins.int
    JFROG_SETTINGS_FIELD_NUMBER: builtins.int
    admin_token: builtins.str
    """The token to use - has to had admin role in jfrog"""
    @property
    def jfrog_settings(self) -> global___JFrogSettings:
        """All user provided JFrog integration settings"""
    def __init__(
        self,
        *,
        admin_token: builtins.str = ...,
        jfrog_settings: global___JFrogSettings | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["jfrog_settings", b"jfrog_settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["admin_token", b"admin_token", "jfrog_settings", b"jfrog_settings"]) -> None: ...

global___JFrogIntegrationSpec = JFrogIntegrationSpec

class JFrogSettings(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BASE_URL_FIELD_NUMBER: builtins.int
    PYTHON_REPOSITORIES_FIELD_NUMBER: builtins.int
    HUGGINGFACE_REPOSITORY_FIELD_NUMBER: builtins.int
    ALLOW_ADDITIONAL_REPOSITORIES_FIELD_NUMBER: builtins.int
    CREATE_HUGGINGFACE_REMOTE_REPOSITORY_FIELD_NUMBER: builtins.int
    base_url: builtins.str
    """The base url to connect to"""
    @property
    def python_repositories(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of private JFrog repositories to resolve dependencies from"""
    huggingface_repository: builtins.str
    """Private HuggingFace repositories to resolve models from"""
    allow_additional_repositories: builtins.bool
    """Whether or not to allow for additional external repositories to be used, usually public repositories"""
    create_huggingface_remote_repository: builtins.bool
    """Create a HuggingFace remote repository if it doesn't exist"""
    def __init__(
        self,
        *,
        base_url: builtins.str = ...,
        python_repositories: collections.abc.Iterable[builtins.str] | None = ...,
        huggingface_repository: builtins.str = ...,
        allow_additional_repositories: builtins.bool = ...,
        create_huggingface_remote_repository: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["allow_additional_repositories", b"allow_additional_repositories", "base_url", b"base_url", "create_huggingface_remote_repository", b"create_huggingface_remote_repository", "huggingface_repository", b"huggingface_repository", "python_repositories", b"python_repositories"]) -> None: ...

global___JFrogSettings = JFrogSettings

class IntegrationValidationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JFROG_VALIDATION_SPEC_FIELD_NUMBER: builtins.int
    OPSGENIE_VALIDATION_SPEC_FIELD_NUMBER: builtins.int
    PAGERDUTY_VALIDATION_SPEC_FIELD_NUMBER: builtins.int
    QWAK_SLACK_APP_VALIDATION_SPEC_FIELD_NUMBER: builtins.int
    OPENAI_VALIDATION_SPEC_FIELD_NUMBER: builtins.int
    HUGGING_FACE_VALIDATION_SPEC_FIELD_NUMBER: builtins.int
    @property
    def jfrog_validation_spec(self) -> global___JFrogValidationSpec: ...
    @property
    def opsgenie_validation_spec(self) -> qwak.integration.opsgenie_integration_pb2.OpsgenieValidationSpec: ...
    @property
    def pagerduty_validation_spec(self) -> qwak.integration.pagerduty_integration_pb2.PagerdutyValidationSpec: ...
    @property
    def qwak_slack_app_validation_spec(self) -> qwak.integration.slack_app_integration_pb2.SlackAppValidationSpec: ...
    @property
    def openai_validation_spec(self) -> qwak.integration.open_a_i_integration_pb2.OpenAIValidationSpec: ...
    @property
    def hugging_face_validation_spec(self) -> qwak.integration.hugging_face_integration_pb2.HuggingFaceValidationSpec: ...
    def __init__(
        self,
        *,
        jfrog_validation_spec: global___JFrogValidationSpec | None = ...,
        opsgenie_validation_spec: qwak.integration.opsgenie_integration_pb2.OpsgenieValidationSpec | None = ...,
        pagerduty_validation_spec: qwak.integration.pagerduty_integration_pb2.PagerdutyValidationSpec | None = ...,
        qwak_slack_app_validation_spec: qwak.integration.slack_app_integration_pb2.SlackAppValidationSpec | None = ...,
        openai_validation_spec: qwak.integration.open_a_i_integration_pb2.OpenAIValidationSpec | None = ...,
        hugging_face_validation_spec: qwak.integration.hugging_face_integration_pb2.HuggingFaceValidationSpec | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hugging_face_validation_spec", b"hugging_face_validation_spec", "jfrog_validation_spec", b"jfrog_validation_spec", "openai_validation_spec", b"openai_validation_spec", "opsgenie_validation_spec", b"opsgenie_validation_spec", "pagerduty_validation_spec", b"pagerduty_validation_spec", "qwak_slack_app_validation_spec", b"qwak_slack_app_validation_spec", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hugging_face_validation_spec", b"hugging_face_validation_spec", "jfrog_validation_spec", b"jfrog_validation_spec", "openai_validation_spec", b"openai_validation_spec", "opsgenie_validation_spec", b"opsgenie_validation_spec", "pagerduty_validation_spec", b"pagerduty_validation_spec", "qwak_slack_app_validation_spec", b"qwak_slack_app_validation_spec", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["jfrog_validation_spec", "opsgenie_validation_spec", "pagerduty_validation_spec", "qwak_slack_app_validation_spec", "openai_validation_spec", "hugging_face_validation_spec"] | None: ...

global___IntegrationValidationSpec = IntegrationValidationSpec

class JFrogValidationSpec(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ADMIN_TOKEN_FIELD_NUMBER: builtins.int
    BASE_URL_FIELD_NUMBER: builtins.int
    admin_token: builtins.str
    """The token to use - has to had admin role in jfrog"""
    base_url: builtins.str
    """The base url to connect to"""
    def __init__(
        self,
        *,
        admin_token: builtins.str = ...,
        base_url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["admin_token", b"admin_token", "base_url", b"base_url"]) -> None: ...

global___JFrogValidationSpec = JFrogValidationSpec

class IntegrationOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JFROG_INTEGRATION_OPTIONS_FIELD_NUMBER: builtins.int
    OPSGENIE_INTEGRATION_OPTIONS_FIELD_NUMBER: builtins.int
    PAGERDUTY_INTEGRATION_OPTIONS_FIELD_NUMBER: builtins.int
    QWAK_SLACK_APP_INTEGRATION_OPTIONS_FIELD_NUMBER: builtins.int
    OPENAI_INTEGRATION_OPTIONS_FIELD_NUMBER: builtins.int
    HUGGING_FACE_INTEGRATION_OPTIONS_FIELD_NUMBER: builtins.int
    @property
    def jfrog_integration_options(self) -> global___JFrogIntegrationOptions:
        """Options for jfrog integration"""
    @property
    def opsgenie_integration_options(self) -> qwak.integration.opsgenie_integration_pb2.OpsgenieIntegrationOptions: ...
    @property
    def pagerduty_integration_options(self) -> qwak.integration.pagerduty_integration_pb2.PagerdutyIntegrationOptions: ...
    @property
    def qwak_slack_app_integration_options(self) -> qwak.integration.slack_app_integration_pb2.SlackAppIntegrationOptions: ...
    @property
    def openai_integration_options(self) -> qwak.integration.open_a_i_integration_pb2.OpenAIIntegrationOptions: ...
    @property
    def hugging_face_integration_options(self) -> qwak.integration.hugging_face_integration_pb2.HuggingFaceIntegrationOptions: ...
    def __init__(
        self,
        *,
        jfrog_integration_options: global___JFrogIntegrationOptions | None = ...,
        opsgenie_integration_options: qwak.integration.opsgenie_integration_pb2.OpsgenieIntegrationOptions | None = ...,
        pagerduty_integration_options: qwak.integration.pagerduty_integration_pb2.PagerdutyIntegrationOptions | None = ...,
        qwak_slack_app_integration_options: qwak.integration.slack_app_integration_pb2.SlackAppIntegrationOptions | None = ...,
        openai_integration_options: qwak.integration.open_a_i_integration_pb2.OpenAIIntegrationOptions | None = ...,
        hugging_face_integration_options: qwak.integration.hugging_face_integration_pb2.HuggingFaceIntegrationOptions | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["hugging_face_integration_options", b"hugging_face_integration_options", "jfrog_integration_options", b"jfrog_integration_options", "openai_integration_options", b"openai_integration_options", "opsgenie_integration_options", b"opsgenie_integration_options", "pagerduty_integration_options", b"pagerduty_integration_options", "qwak_slack_app_integration_options", b"qwak_slack_app_integration_options", "type", b"type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["hugging_face_integration_options", b"hugging_face_integration_options", "jfrog_integration_options", b"jfrog_integration_options", "openai_integration_options", b"openai_integration_options", "opsgenie_integration_options", b"opsgenie_integration_options", "pagerduty_integration_options", b"pagerduty_integration_options", "qwak_slack_app_integration_options", b"qwak_slack_app_integration_options", "type", b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["type", b"type"]) -> typing_extensions.Literal["jfrog_integration_options", "opsgenie_integration_options", "pagerduty_integration_options", "qwak_slack_app_integration_options", "openai_integration_options", "hugging_face_integration_options"] | None: ...

global___IntegrationOptions = IntegrationOptions

class JFrogIntegrationOptions(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AVAILABLE_PRIVATE_PYTHON_REPOSITORIES_FIELD_NUMBER: builtins.int
    AVAILABLE_PRIVATE_HUGGINGFACE_REPOSITORIES_FIELD_NUMBER: builtins.int
    @property
    def available_private_python_repositories(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JfrogRepository]:
        """available private python repositories in the Jfrog account"""
    @property
    def available_private_huggingface_repositories(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___JfrogRepository]:
        """available private huggingface repositories in the Jfrog account"""
    def __init__(
        self,
        *,
        available_private_python_repositories: collections.abc.Iterable[global___JfrogRepository] | None = ...,
        available_private_huggingface_repositories: collections.abc.Iterable[global___JfrogRepository] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["available_private_huggingface_repositories", b"available_private_huggingface_repositories", "available_private_python_repositories", b"available_private_python_repositories"]) -> None: ...

global___JFrogIntegrationOptions = JFrogIntegrationOptions

class JfrogRepository(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___JfrogRepository = JfrogRepository

class ValidationIntegrationResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    IS_SUCCESSFUL_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    ERROR_MESSAGE_FIELD_NUMBER: builtins.int
    is_successful: builtins.bool
    """Is the validation successful"""
    @property
    def options(self) -> global___IntegrationOptions:
        """The integration options after it validate"""
    error_message: builtins.str
    """The error if validation failed"""
    def __init__(
        self,
        *,
        is_successful: builtins.bool = ...,
        options: global___IntegrationOptions | None = ...,
        error_message: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["options", b"options"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["error_message", b"error_message", "is_successful", b"is_successful", "options", b"options"]) -> None: ...

global___ValidationIntegrationResult = ValidationIntegrationResult
