# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.alert_manager.v1 import service_channel_pb2 as spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2

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
        + f' but the generated code in spaceone/api/alert_manager/v1/service_channel_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ServiceChannelStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.create = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/create',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelCreateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
                _registered_method=True)
        self.create_forward_channel = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/create_forward_channel',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelCreateForwardChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
                _registered_method=True)
        self.update = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/update',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelUpdateRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
                _registered_method=True)
        self.enable = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/enable',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
                _registered_method=True)
        self.disable = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/disable',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
                _registered_method=True)
        self.delete = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/delete',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/get',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/list',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelSearchQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelsInfo.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.alert_manager.v1.ServiceChannel/stat',
                request_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class ServiceChannelServicer(object):
    """Missing associated documentation comment in .proto file."""

    def create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_forward_channel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def enable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disable(self, request, context):
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

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServiceChannelServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'create': grpc.unary_unary_rpc_method_handler(
                    servicer.create,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelCreateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.SerializeToString,
            ),
            'create_forward_channel': grpc.unary_unary_rpc_method_handler(
                    servicer.create_forward_channel,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelCreateForwardChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelUpdateRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.SerializeToString,
            ),
            'enable': grpc.unary_unary_rpc_method_handler(
                    servicer.enable,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.SerializeToString,
            ),
            'disable': grpc.unary_unary_rpc_method_handler(
                    servicer.disable,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelSearchQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelsInfo.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.alert_manager.v1.ServiceChannel', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.alert_manager.v1.ServiceChannel', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ServiceChannel(object):
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/create',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelCreateRequest.SerializeToString,
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
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
    def create_forward_channel(request,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/create_forward_channel',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelCreateForwardChannelRequest.SerializeToString,
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/update',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelUpdateRequest.SerializeToString,
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
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
    def enable(request,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/enable',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
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
    def disable(request,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/disable',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/delete',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/get',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelRequest.SerializeToString,
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelInfo.FromString,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/list',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelSearchQuery.SerializeToString,
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelsInfo.FromString,
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
    def stat(request,
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
            '/spaceone.api.alert_manager.v1.ServiceChannel/stat',
            spaceone_dot_api_dot_alert__manager_dot_v1_dot_service__channel__pb2.ServiceChannelStatQuery.SerializeToString,
            google_dot_protobuf_dot_struct__pb2.Struct.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
