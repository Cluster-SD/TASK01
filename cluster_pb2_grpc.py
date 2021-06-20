# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import cluster_pb2 as cluster__pb2


class WorkerStub(object):
    """All the RCP comunications between client-server:
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateWorkers = channel.unary_unary(
                '/Worker/CreateWorkers',
                request_serializer=cluster__pb2.Workers.SerializeToString,
                response_deserializer=cluster__pb2.Response.FromString,
                )
        self.DeleteWorkers = channel.unary_unary(
                '/Worker/DeleteWorkers',
                request_serializer=cluster__pb2.Workers.SerializeToString,
                response_deserializer=cluster__pb2.Response.FromString,
                )
        self.List = channel.unary_stream(
                '/Worker/List',
                request_serializer=cluster__pb2.Workers.SerializeToString,
                response_deserializer=cluster__pb2.Response.FromString,
                )
        self.CoutingWords = channel.stream_unary(
                '/Worker/CoutingWords',
                request_serializer=cluster__pb2.File.SerializeToString,
                response_deserializer=cluster__pb2.Words.FromString,
                )
        self.WordCounts = channel.stream_stream(
                '/Worker/WordCounts',
                request_serializer=cluster__pb2.File.SerializeToString,
                response_deserializer=cluster__pb2.WordCount.FromString,
                )


class WorkerServicer(object):
    """All the RCP comunications between client-server:
    """

    def CreateWorkers(self, request, context):
        """Unary RCP: client send to server the number of workers to create.
        recieve a estandar message from server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteWorkers(self, request, context):
        """Unary RCP: client send to server the number of workers to delete.
        recieve a estandar message from server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Server streaming RCP: client asks server about the workers.
        recieve a stream of estandar messages from server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CoutingWords(self, request_iterator, context):
        """Client streaming RCP: client send a/some file/s to server.
        recieve the number of words from all files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WordCounts(self, request_iterator, context):
        """Bidierctional streaming RCP: client send a/some file/s to server.
        recieve the number of occurencies of each word in all files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateWorkers': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWorkers,
                    request_deserializer=cluster__pb2.Workers.FromString,
                    response_serializer=cluster__pb2.Response.SerializeToString,
            ),
            'DeleteWorkers': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteWorkers,
                    request_deserializer=cluster__pb2.Workers.FromString,
                    response_serializer=cluster__pb2.Response.SerializeToString,
            ),
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=cluster__pb2.Workers.FromString,
                    response_serializer=cluster__pb2.Response.SerializeToString,
            ),
            'CoutingWords': grpc.stream_unary_rpc_method_handler(
                    servicer.CoutingWords,
                    request_deserializer=cluster__pb2.File.FromString,
                    response_serializer=cluster__pb2.Words.SerializeToString,
            ),
            'WordCounts': grpc.stream_stream_rpc_method_handler(
                    servicer.WordCounts,
                    request_deserializer=cluster__pb2.File.FromString,
                    response_serializer=cluster__pb2.WordCount.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Worker', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Worker(object):
    """All the RCP comunications between client-server:
    """

    @staticmethod
    def CreateWorkers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Worker/CreateWorkers',
            cluster__pb2.Workers.SerializeToString,
            cluster__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteWorkers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Worker/DeleteWorkers',
            cluster__pb2.Workers.SerializeToString,
            cluster__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Worker/List',
            cluster__pb2.Workers.SerializeToString,
            cluster__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CoutingWords(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/Worker/CoutingWords',
            cluster__pb2.File.SerializeToString,
            cluster__pb2.Words.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WordCounts(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Worker/WordCounts',
            cluster__pb2.File.SerializeToString,
            cluster__pb2.WordCount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)