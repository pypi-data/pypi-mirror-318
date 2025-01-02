from enum import IntEnum
from dataclasses import dataclass
from PySide6.QtCore import QByteArray
from ctypes import c_ubyte
from utils import check_sum
from utils import float_to_hex,hex_str_to_bytearray,int_to_hex_32

class Command(IntEnum):
    """通信命令枚举"""
    HANDSHAKE = 0x01
    REQUEST_DATA = 0x02
    SET_SPEED = 0x19
    STOP_MOTION = 0x20
    ZERO_POSITION = 0x24
    SINGLE_AXIS_MOTION = 0x25

@dataclass
class FrameHeader:
    """帧头配置"""
    START_BYTE = 0x7F
    VERSION = 0x00
    DEVICE_ID = 0x01

class CommunicationsProtocol:
    def __init__(self):
        self._header = self._create_header()
    
    def _create_header(self) -> QByteArray:
        """创建固定帧头"""
        header = QByteArray()
        header.append(FrameHeader.START_BYTE)
        header.append(QByteArray.fromHex(b'C0'))
        header.append(FrameHeader.VERSION)
        header.append(FrameHeader.DEVICE_ID)
        return header

    def _create_hex_frame(self, command: Command, data: QByteArray) -> QByteArray:
        """创建通信帧"""
        if not isinstance(command, Command):
            raise ValueError("命令必须是Command枚举类型")

        data_length = 2 + 1 + len(data) + 2  # datalength(2) + command ID(1) + 数据长度 + CRC(2)
        
        frame = QByteArray()
        frame.append(self._header)
        frame.append((data_length >> 8) & 0xFF)
        frame.append(data_length & 0xFF)
        frame.append(command)
        frame.append(data)

        # 计算校验和
        checksum = check_sum(frame)
        frame.append(bytearray([c_ubyte((checksum >> 8) & 0xFF).value]))
        frame.append(bytearray([c_ubyte(checksum & 0xFF).value]))
        
        return frame

    def handshake(self) -> QByteArray:
        """握手请求"""
        return self._create_hex_frame(Command.HANDSHAKE, QByteArray())
    
    def request_data(self) -> QByteArray:
        """请求数据"""
        return self._create_hex_frame(Command.REQUEST_DATA, QByteArray())
    
    def set_speed(self, speed: float) -> QByteArray:
        """设置速度
        
        Args:
            speed: 目标速度值
        """
        data = QByteArray()
        data.append(0x01)
        speed = hex_str_to_bytearray(float_to_hex(speed))
        data.append(speed)
        data.append(0x00)
        data.append(0x00)
        return self._create_hex_frame(Command.SET_SPEED, data)

    def stop_motion(self, stop_type: hex) -> QByteArray:
        """停止运动
        
        Args:
            stop_type: 停止类型(0x00:不带保持力停止, 0x01:带保持力停止)
        """

        data = QByteArray()
        data.append(0x01)
        data.append(stop_type)
        return self._create_hex_frame(Command.STOP_MOTION, data)
    
    def zero_position(self) -> QByteArray:
        """设置零位"""
        data = QByteArray()
        data.append(0x01)
        data.append(0x00)
        return self._create_hex_frame(Command.ZERO_POSITION, data)
    
    def single_axis_motion(self,position:int)->QByteArray:
        """单轴运动
        
        Args:
            position: 目标位置
        """
        data = QByteArray()
        data.append(0x01)
        position = hex_str_to_bytearray(int_to_hex_32(position))
        data.append(position)
        return self._create_hex_frame(Command.SINGLE_AXIS_MOTION, data)

if __name__ == "__main__":
    protocol = CommunicationsProtocol()
    print(protocol.handshake().toHex().toUpper())
    print(protocol.request_data().toHex().toUpper())
    print(protocol.set_speed(1000).toHex().toUpper())
    print(protocol.stop_motion(0x00).toHex().toUpper())
    print(protocol.zero_position().toHex().toUpper())
    print(protocol.single_axis_motion(1000).toHex().toUpper())


