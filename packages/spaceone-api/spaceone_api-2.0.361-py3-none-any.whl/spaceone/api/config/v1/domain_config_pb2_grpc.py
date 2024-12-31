# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from spaceone.api.config.v1 import domain_config_pb2 as spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in spaceone/api/config/v1/domain_config_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DomainConfigStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.config.v1.DomainConfig/create',
                request_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.config.v1.DomainConfig/update',
                request_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
                _registered_method=True)
        self.set = channel.unary_unary(
                '/spaceone.api.config.v1.DomainConfig/set',
                request_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.config.v1.DomainConfig/delete',
                request_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.config.v1.DomainConfig/get',
                request_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.config.v1.DomainConfig/list',
                request_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigSearchQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigsInfo.FromString,
                _registered_method=True)


class DomainConfigServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DomainConfigServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.SerializeToString,
            ),
            'set': grpc.unary_unary_rpc_method_handler(
                    servicer.set,
                    request_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigSearchQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigsInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.config.v1.DomainConfig', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.config.v1.DomainConfig', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DomainConfig(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.config.v1.DomainConfig/create',
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.SerializeToString,
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.config.v1.DomainConfig/update',
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.SerializeToString,
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def set(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.config.v1.DomainConfig/set',
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.SetDomainConfigRequest.SerializeToString,
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.config.v1.DomainConfig/delete',
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.config.v1.DomainConfig/get',
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigRequest.SerializeToString,
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/spaceone.api.config.v1.DomainConfig/list',
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigSearchQuery.SerializeToString,
            spaceone_dot_api_dot_config_dot_v1_dot_domain__config__pb2.DomainConfigsInfo.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
