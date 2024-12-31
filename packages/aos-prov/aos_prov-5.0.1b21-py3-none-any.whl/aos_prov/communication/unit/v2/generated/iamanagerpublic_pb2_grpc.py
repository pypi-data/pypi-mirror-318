# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from aos_prov.communication.unit.v2.generated import (
    iamanagercommon_pb2 as iamanager_dot_v2_dot_iamanagercommon__pb2,
)
from aos_prov.communication.unit.v2.generated import (
    iamanagerpublic_pb2 as iamanager_dot_v2_dot_iamanagerpublic__pb2,
)
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class IAMPublicServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetSystemInfo = channel.unary_unary(
                '/iamanager.v2.IAMPublicService/GetSystemInfo',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.SystemInfo.FromString,
                )
        self.GetCertTypes = channel.unary_unary(
                '/iamanager.v2.IAMPublicService/GetCertTypes',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.CertTypes.FromString,
                )
        self.GetCert = channel.unary_unary(
                '/iamanager.v2.IAMPublicService/GetCert',
                request_serializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.GetCertRequest.SerializeToString,
                response_deserializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.GetCertResponse.FromString,
                )
        self.GetPermissions = channel.unary_unary(
                '/iamanager.v2.IAMPublicService/GetPermissions',
                request_serializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.PermissionsRequest.SerializeToString,
                response_deserializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.PermissionsResponse.FromString,
                )
        self.GetUsers = channel.unary_unary(
                '/iamanager.v2.IAMPublicService/GetUsers',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=iamanager_dot_v2_dot_iamanagercommon__pb2.Users.FromString,
                )
        self.SubscribeUsersChanged = channel.unary_stream(
                '/iamanager.v2.IAMPublicService/SubscribeUsersChanged',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=iamanager_dot_v2_dot_iamanagercommon__pb2.Users.FromString,
                )
        self.GetAPIVersion = channel.unary_unary(
                '/iamanager.v2.IAMPublicService/GetAPIVersion',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.APIVersion.FromString,
                )


class IAMPublicServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetSystemInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCertTypes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPermissions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUsers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeUsersChanged(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAPIVersion(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IAMPublicServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetSystemInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSystemInfo,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.SystemInfo.SerializeToString,
            ),
            'GetCertTypes': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCertTypes,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.CertTypes.SerializeToString,
            ),
            'GetCert': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCert,
                    request_deserializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.GetCertRequest.FromString,
                    response_serializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.GetCertResponse.SerializeToString,
            ),
            'GetPermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPermissions,
                    request_deserializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.PermissionsRequest.FromString,
                    response_serializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.PermissionsResponse.SerializeToString,
            ),
            'GetUsers': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUsers,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=iamanager_dot_v2_dot_iamanagercommon__pb2.Users.SerializeToString,
            ),
            'SubscribeUsersChanged': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeUsersChanged,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=iamanager_dot_v2_dot_iamanagercommon__pb2.Users.SerializeToString,
            ),
            'GetAPIVersion': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAPIVersion,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=iamanager_dot_v2_dot_iamanagerpublic__pb2.APIVersion.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'iamanager.v2.IAMPublicService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IAMPublicService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetSystemInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iamanager.v2.IAMPublicService/GetSystemInfo',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            iamanager_dot_v2_dot_iamanagerpublic__pb2.SystemInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCertTypes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iamanager.v2.IAMPublicService/GetCertTypes',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            iamanager_dot_v2_dot_iamanagerpublic__pb2.CertTypes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iamanager.v2.IAMPublicService/GetCert',
            iamanager_dot_v2_dot_iamanagerpublic__pb2.GetCertRequest.SerializeToString,
            iamanager_dot_v2_dot_iamanagerpublic__pb2.GetCertResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetPermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iamanager.v2.IAMPublicService/GetPermissions',
            iamanager_dot_v2_dot_iamanagerpublic__pb2.PermissionsRequest.SerializeToString,
            iamanager_dot_v2_dot_iamanagerpublic__pb2.PermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iamanager.v2.IAMPublicService/GetUsers',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            iamanager_dot_v2_dot_iamanagercommon__pb2.Users.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubscribeUsersChanged(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/iamanager.v2.IAMPublicService/SubscribeUsersChanged',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            iamanager_dot_v2_dot_iamanagercommon__pb2.Users.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAPIVersion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/iamanager.v2.IAMPublicService/GetAPIVersion',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            iamanager_dot_v2_dot_iamanagerpublic__pb2.APIVersion.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
