# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import network_pb2 as network__pb2


class NetworkServiceGrpcStub(object):
    """包括Wifi、热点、蓝牙服务等
    定义服务,用在rpc传输中
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getWifiList = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/getWifiList',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.WifiListResponse.FromString,
                )
        self.connectWifi = channel.unary_stream(
                '/NetworkPackage.NetworkServiceGrpc/connectWifi',
                request_serializer=network__pb2.WifiConnectRequest.SerializeToString,
                response_deserializer=network__pb2.WifiConnectResponse.FromString,
                )
        self.getWifiStatus = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/getWifiStatus',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.WifiStateResponse.FromString,
                )
        self.setWifiEnable = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/setWifiEnable',
                request_serializer=network__pb2.WifiEnableRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.disconnectWifi = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/disconnectWifi',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.startWifiStateListener = channel.unary_stream(
                '/NetworkPackage.NetworkServiceGrpc/startWifiStateListener',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.WifiStateResponse.FromString,
                )
        self.stopWifiStateListener = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/stopWifiStateListener',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.startHotspot = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/startHotspot',
                request_serializer=network__pb2.HotspotInfoRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.stopHotspot = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/stopHotspot',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.getHotspotState = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/getHotspotState',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.HotspotStateResponse.FromString,
                )
        self.getBTJoypadStatus = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/getBTJoypadStatus',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.BTJoypadStatusResponse.FromString,
                )
        self.setBrocastEnable = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/setBrocastEnable',
                request_serializer=network__pb2.SetBrocastEnableRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.setBrocastPort = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/setBrocastPort',
                request_serializer=network__pb2.SetBrocastPortRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.sendBrocastMsg = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/sendBrocastMsg',
                request_serializer=network__pb2.SendBrocastMsgRequest.SerializeToString,
                response_deserializer=network__pb2.NetworkCommonResponse.FromString,
                )
        self.getReceivedBrocastMsg = channel.unary_unary(
                '/NetworkPackage.NetworkServiceGrpc/getReceivedBrocastMsg',
                request_serializer=network__pb2.NetworkCommonRequest.SerializeToString,
                response_deserializer=network__pb2.GetReceivedBrocastMsgResponse.FromString,
                )


class NetworkServiceGrpcServicer(object):
    """包括Wifi、热点、蓝牙服务等
    定义服务,用在rpc传输中
    """

    def getWifiList(self, request, context):
        """定义Wifi服务
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def connectWifi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getWifiStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setWifiEnable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disconnectWifi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def startWifiStateListener(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stopWifiStateListener(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def startHotspot(self, request, context):
        """定义热点服务
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def stopHotspot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getHotspotState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getBTJoypadStatus(self, request, context):
        """定义蓝牙手柄服务
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setBrocastEnable(self, request, context):
        """物联网相关
        开/关
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setBrocastPort(self, request, context):
        """设置频道
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendBrocastMsg(self, request, context):
        """发送广播
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def getReceivedBrocastMsg(self, request, context):
        """获取接收到的广播消息
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NetworkServiceGrpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getWifiList': grpc.unary_unary_rpc_method_handler(
                    servicer.getWifiList,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.WifiListResponse.SerializeToString,
            ),
            'connectWifi': grpc.unary_stream_rpc_method_handler(
                    servicer.connectWifi,
                    request_deserializer=network__pb2.WifiConnectRequest.FromString,
                    response_serializer=network__pb2.WifiConnectResponse.SerializeToString,
            ),
            'getWifiStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.getWifiStatus,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.WifiStateResponse.SerializeToString,
            ),
            'setWifiEnable': grpc.unary_unary_rpc_method_handler(
                    servicer.setWifiEnable,
                    request_deserializer=network__pb2.WifiEnableRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'disconnectWifi': grpc.unary_unary_rpc_method_handler(
                    servicer.disconnectWifi,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'startWifiStateListener': grpc.unary_stream_rpc_method_handler(
                    servicer.startWifiStateListener,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.WifiStateResponse.SerializeToString,
            ),
            'stopWifiStateListener': grpc.unary_unary_rpc_method_handler(
                    servicer.stopWifiStateListener,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'startHotspot': grpc.unary_unary_rpc_method_handler(
                    servicer.startHotspot,
                    request_deserializer=network__pb2.HotspotInfoRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'stopHotspot': grpc.unary_unary_rpc_method_handler(
                    servicer.stopHotspot,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'getHotspotState': grpc.unary_unary_rpc_method_handler(
                    servicer.getHotspotState,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.HotspotStateResponse.SerializeToString,
            ),
            'getBTJoypadStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.getBTJoypadStatus,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.BTJoypadStatusResponse.SerializeToString,
            ),
            'setBrocastEnable': grpc.unary_unary_rpc_method_handler(
                    servicer.setBrocastEnable,
                    request_deserializer=network__pb2.SetBrocastEnableRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'setBrocastPort': grpc.unary_unary_rpc_method_handler(
                    servicer.setBrocastPort,
                    request_deserializer=network__pb2.SetBrocastPortRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'sendBrocastMsg': grpc.unary_unary_rpc_method_handler(
                    servicer.sendBrocastMsg,
                    request_deserializer=network__pb2.SendBrocastMsgRequest.FromString,
                    response_serializer=network__pb2.NetworkCommonResponse.SerializeToString,
            ),
            'getReceivedBrocastMsg': grpc.unary_unary_rpc_method_handler(
                    servicer.getReceivedBrocastMsg,
                    request_deserializer=network__pb2.NetworkCommonRequest.FromString,
                    response_serializer=network__pb2.GetReceivedBrocastMsgResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NetworkPackage.NetworkServiceGrpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NetworkServiceGrpc(object):
    """包括Wifi、热点、蓝牙服务等
    定义服务,用在rpc传输中
    """

    @staticmethod
    def getWifiList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/getWifiList',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.WifiListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def connectWifi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/NetworkPackage.NetworkServiceGrpc/connectWifi',
            network__pb2.WifiConnectRequest.SerializeToString,
            network__pb2.WifiConnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getWifiStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/getWifiStatus',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.WifiStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setWifiEnable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/setWifiEnable',
            network__pb2.WifiEnableRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def disconnectWifi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/disconnectWifi',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def startWifiStateListener(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/NetworkPackage.NetworkServiceGrpc/startWifiStateListener',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.WifiStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stopWifiStateListener(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/stopWifiStateListener',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def startHotspot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/startHotspot',
            network__pb2.HotspotInfoRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def stopHotspot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/stopHotspot',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getHotspotState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/getHotspotState',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.HotspotStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getBTJoypadStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/getBTJoypadStatus',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.BTJoypadStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setBrocastEnable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/setBrocastEnable',
            network__pb2.SetBrocastEnableRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setBrocastPort(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/setBrocastPort',
            network__pb2.SetBrocastPortRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendBrocastMsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/sendBrocastMsg',
            network__pb2.SendBrocastMsgRequest.SerializeToString,
            network__pb2.NetworkCommonResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def getReceivedBrocastMsg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NetworkPackage.NetworkServiceGrpc/getReceivedBrocastMsg',
            network__pb2.NetworkCommonRequest.SerializeToString,
            network__pb2.GetReceivedBrocastMsgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
