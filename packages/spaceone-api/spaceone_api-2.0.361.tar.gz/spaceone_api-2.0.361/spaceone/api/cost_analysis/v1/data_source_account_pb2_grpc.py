# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from spaceone.api.cost_analysis.v1 import data_source_account_pb2 as spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2

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
        + f' but the generated code in spaceone/api/cost_analysis/v1/data_source_account_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DataSourceAccountStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.update = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.DataSourceAccount/update',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.UpdateDataSourceAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountInfo.FromString,
                _registered_method=True)
        self.reset = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.DataSourceAccount/reset',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.ResetDataSourceAccountRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.get = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.DataSourceAccount/get',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountRequest.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountInfo.FromString,
                _registered_method=True)
        self.list = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.DataSourceAccount/list',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountQuery.SerializeToString,
                response_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountsInfo.FromString,
                _registered_method=True)
        self.analyze = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.DataSourceAccount/analyze',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountAnalyzeQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)
        self.stat = channel.unary_unary(
                '/spaceone.api.cost_analysis.v1.DataSourceAccount/stat',
                request_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountStatQuery.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_struct__pb2.Struct.FromString,
                _registered_method=True)


class DataSourceAccountServicer(object):
    """Missing associated documentation comment in .proto file."""

    def update(self, request, context):
        """Update a DataSourceAccount with the specified DataSourceAccount ID related to the DataSource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reset(self, request, context):
        """Reset a DataSourceAccount state and linked workspace with the specified DataSourceAccount ID related to the DataSource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Get a DataSourceAccount with the specified DataSourceAccount ID related to the DataSource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def analyze(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataSourceAccountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.UpdateDataSourceAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountInfo.SerializeToString,
            ),
            'reset': grpc.unary_unary_rpc_method_handler(
                    servicer.reset,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.ResetDataSourceAccountRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountRequest.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountInfo.SerializeToString,
            ),
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountQuery.FromString,
                    response_serializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountsInfo.SerializeToString,
            ),
            'analyze': grpc.unary_unary_rpc_method_handler(
                    servicer.analyze,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountAnalyzeQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
            'stat': grpc.unary_unary_rpc_method_handler(
                    servicer.stat,
                    request_deserializer=spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountStatQuery.FromString,
                    response_serializer=google_dot_protobuf_dot_struct__pb2.Struct.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'spaceone.api.cost_analysis.v1.DataSourceAccount', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('spaceone.api.cost_analysis.v1.DataSourceAccount', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class DataSourceAccount(object):
    """Missing associated documentation comment in .proto file."""

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
            '/spaceone.api.cost_analysis.v1.DataSourceAccount/update',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.UpdateDataSourceAccountRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountInfo.FromString,
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
    def reset(request,
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
            '/spaceone.api.cost_analysis.v1.DataSourceAccount/reset',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.ResetDataSourceAccountRequest.SerializeToString,
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
            '/spaceone.api.cost_analysis.v1.DataSourceAccount/get',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountRequest.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountInfo.FromString,
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
            '/spaceone.api.cost_analysis.v1.DataSourceAccount/list',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountQuery.SerializeToString,
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountsInfo.FromString,
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
    def analyze(request,
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
            '/spaceone.api.cost_analysis.v1.DataSourceAccount/analyze',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountAnalyzeQuery.SerializeToString,
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
            '/spaceone.api.cost_analysis.v1.DataSourceAccount/stat',
            spaceone_dot_api_dot_cost__analysis_dot_v1_dot_data__source__account__pb2.DataSourceAccountStatQuery.SerializeToString,
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
