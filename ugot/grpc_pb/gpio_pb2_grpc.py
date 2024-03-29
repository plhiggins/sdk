# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import gpio_pb2 as gpio__pb2


class GpioServiceGrpcStub(object):
    """

    一: gpio 引脚对应，传值的时候转换一下

    1  146 
    2  147
    3  149 (此接口当前是 USB 供电口，不可用)
    4  150
    5  151
    6  131

    二: 引脚 PWM 输出

    frequency: 频率赫兹
    duty_cycle: slider 的值，范围（0 ～ 255）
    range: 范围，根据需求填 255

    三: 串口，开放接口上的串口默认值为：

    /dev/ttyS0

    四：串口写字符换行功能

    只要在字符串后面添加 \r\n 就能实现换行


    定义服务,用在rpc传输中
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.setGpioExport = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/setGpioExport',
                request_serializer=gpio__pb2.SetGpioExportRequest.SerializeToString,
                response_deserializer=gpio__pb2.SetGpioExportResponse.FromString,
                )
        self.readGpio = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/readGpio',
                request_serializer=gpio__pb2.ReadGpioRequest.SerializeToString,
                response_deserializer=gpio__pb2.ReadGpioResponse.FromString,
                )
        self.setGpioStartExportPwm = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/setGpioStartExportPwm',
                request_serializer=gpio__pb2.SetGpioStartExportPwmRequest.SerializeToString,
                response_deserializer=gpio__pb2.SetGpioStartExportPwmResponse.FromString,
                )
        self.setGpioStopExportPwm = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/setGpioStopExportPwm',
                request_serializer=gpio__pb2.SetGpioStopExportPwmRequest.SerializeToString,
                response_deserializer=gpio__pb2.SetGpioStopExportPwmResponse.FromString,
                )
        self.setSerbaud = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/setSerbaud',
                request_serializer=gpio__pb2.SetSerbaudRequest.SerializeToString,
                response_deserializer=gpio__pb2.SetSerbaudResponse.FromString,
                )
        self.serialExportString = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/serialExportString',
                request_serializer=gpio__pb2.SerialExportStringRequest.SerializeToString,
                response_deserializer=gpio__pb2.SerialExportStringResponse.FromString,
                )
        self.serialReadByte = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/serialReadByte',
                request_serializer=gpio__pb2.SerialReadByteRequest.SerializeToString,
                response_deserializer=gpio__pb2.SerialReadByteResponse.FromString,
                )
        self.serialReadString = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/serialReadString',
                request_serializer=gpio__pb2.SerialReadStringRequest.SerializeToString,
                response_deserializer=gpio__pb2.SerialReadStringResponse.FromString,
                )
        self.serialReadUtil = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/serialReadUtil',
                request_serializer=gpio__pb2.SerialReadUtilRequest.SerializeToString,
                response_deserializer=gpio__pb2.SerialReadUtilResponse.FromString,
                )
        self.clearAllGpioAndSerial = channel.unary_unary(
                '/GpioPackage.GpioServiceGrpc/clearAllGpioAndSerial',
                request_serializer=gpio__pb2.ClearAllGpioAndSerialRequest.SerializeToString,
                response_deserializer=gpio__pb2.ClearAllGpioAndSerialResponse.FromString,
                )


class GpioServiceGrpcServicer(object):
    """

    一: gpio 引脚对应，传值的时候转换一下

    1  146 
    2  147
    3  149 (此接口当前是 USB 供电口，不可用)
    4  150
    5  151
    6  131

    二: 引脚 PWM 输出

    frequency: 频率赫兹
    duty_cycle: slider 的值，范围（0 ～ 255）
    range: 范围，根据需求填 255

    三: 串口，开放接口上的串口默认值为：

    /dev/ttyS0

    四：串口写字符换行功能

    只要在字符串后面添加 \r\n 就能实现换行


    定义服务,用在rpc传输中
    """

    def setGpioExport(self, request, context):
        """gpio
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readGpio(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setGpioStartExportPwm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setGpioStopExportPwm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def setSerbaud(self, request, context):
        """serial
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def serialExportString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def serialReadByte(self, request, context):
        """将数字转换成字符串发送
        rpc serialExportNum(SerialExportNumRequest) returns (SerialExportNumResponse) {};
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def serialReadString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def serialReadUtil(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def clearAllGpioAndSerial(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GpioServiceGrpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'setGpioExport': grpc.unary_unary_rpc_method_handler(
                    servicer.setGpioExport,
                    request_deserializer=gpio__pb2.SetGpioExportRequest.FromString,
                    response_serializer=gpio__pb2.SetGpioExportResponse.SerializeToString,
            ),
            'readGpio': grpc.unary_unary_rpc_method_handler(
                    servicer.readGpio,
                    request_deserializer=gpio__pb2.ReadGpioRequest.FromString,
                    response_serializer=gpio__pb2.ReadGpioResponse.SerializeToString,
            ),
            'setGpioStartExportPwm': grpc.unary_unary_rpc_method_handler(
                    servicer.setGpioStartExportPwm,
                    request_deserializer=gpio__pb2.SetGpioStartExportPwmRequest.FromString,
                    response_serializer=gpio__pb2.SetGpioStartExportPwmResponse.SerializeToString,
            ),
            'setGpioStopExportPwm': grpc.unary_unary_rpc_method_handler(
                    servicer.setGpioStopExportPwm,
                    request_deserializer=gpio__pb2.SetGpioStopExportPwmRequest.FromString,
                    response_serializer=gpio__pb2.SetGpioStopExportPwmResponse.SerializeToString,
            ),
            'setSerbaud': grpc.unary_unary_rpc_method_handler(
                    servicer.setSerbaud,
                    request_deserializer=gpio__pb2.SetSerbaudRequest.FromString,
                    response_serializer=gpio__pb2.SetSerbaudResponse.SerializeToString,
            ),
            'serialExportString': grpc.unary_unary_rpc_method_handler(
                    servicer.serialExportString,
                    request_deserializer=gpio__pb2.SerialExportStringRequest.FromString,
                    response_serializer=gpio__pb2.SerialExportStringResponse.SerializeToString,
            ),
            'serialReadByte': grpc.unary_unary_rpc_method_handler(
                    servicer.serialReadByte,
                    request_deserializer=gpio__pb2.SerialReadByteRequest.FromString,
                    response_serializer=gpio__pb2.SerialReadByteResponse.SerializeToString,
            ),
            'serialReadString': grpc.unary_unary_rpc_method_handler(
                    servicer.serialReadString,
                    request_deserializer=gpio__pb2.SerialReadStringRequest.FromString,
                    response_serializer=gpio__pb2.SerialReadStringResponse.SerializeToString,
            ),
            'serialReadUtil': grpc.unary_unary_rpc_method_handler(
                    servicer.serialReadUtil,
                    request_deserializer=gpio__pb2.SerialReadUtilRequest.FromString,
                    response_serializer=gpio__pb2.SerialReadUtilResponse.SerializeToString,
            ),
            'clearAllGpioAndSerial': grpc.unary_unary_rpc_method_handler(
                    servicer.clearAllGpioAndSerial,
                    request_deserializer=gpio__pb2.ClearAllGpioAndSerialRequest.FromString,
                    response_serializer=gpio__pb2.ClearAllGpioAndSerialResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'GpioPackage.GpioServiceGrpc', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GpioServiceGrpc(object):
    """

    一: gpio 引脚对应，传值的时候转换一下

    1  146 
    2  147
    3  149 (此接口当前是 USB 供电口，不可用)
    4  150
    5  151
    6  131

    二: 引脚 PWM 输出

    frequency: 频率赫兹
    duty_cycle: slider 的值，范围（0 ～ 255）
    range: 范围，根据需求填 255

    三: 串口，开放接口上的串口默认值为：

    /dev/ttyS0

    四：串口写字符换行功能

    只要在字符串后面添加 \r\n 就能实现换行


    定义服务,用在rpc传输中
    """

    @staticmethod
    def setGpioExport(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/setGpioExport',
            gpio__pb2.SetGpioExportRequest.SerializeToString,
            gpio__pb2.SetGpioExportResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readGpio(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/readGpio',
            gpio__pb2.ReadGpioRequest.SerializeToString,
            gpio__pb2.ReadGpioResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setGpioStartExportPwm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/setGpioStartExportPwm',
            gpio__pb2.SetGpioStartExportPwmRequest.SerializeToString,
            gpio__pb2.SetGpioStartExportPwmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setGpioStopExportPwm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/setGpioStopExportPwm',
            gpio__pb2.SetGpioStopExportPwmRequest.SerializeToString,
            gpio__pb2.SetGpioStopExportPwmResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def setSerbaud(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/setSerbaud',
            gpio__pb2.SetSerbaudRequest.SerializeToString,
            gpio__pb2.SetSerbaudResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def serialExportString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/serialExportString',
            gpio__pb2.SerialExportStringRequest.SerializeToString,
            gpio__pb2.SerialExportStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def serialReadByte(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/serialReadByte',
            gpio__pb2.SerialReadByteRequest.SerializeToString,
            gpio__pb2.SerialReadByteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def serialReadString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/serialReadString',
            gpio__pb2.SerialReadStringRequest.SerializeToString,
            gpio__pb2.SerialReadStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def serialReadUtil(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/serialReadUtil',
            gpio__pb2.SerialReadUtilRequest.SerializeToString,
            gpio__pb2.SerialReadUtilResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def clearAllGpioAndSerial(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/GpioPackage.GpioServiceGrpc/clearAllGpioAndSerial',
            gpio__pb2.ClearAllGpioAndSerialRequest.SerializeToString,
            gpio__pb2.ClearAllGpioAndSerialResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
