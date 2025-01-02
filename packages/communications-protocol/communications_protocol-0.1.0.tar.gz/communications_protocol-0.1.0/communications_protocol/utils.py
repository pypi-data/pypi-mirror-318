import struct
from ctypes import c_ubyte
from PySide6.QtCore import QByteArray
from typing import List

#检测帧校验位
def check_frame_digit(frame):
    # print("frame[8:-4]:",frame[8:-4])
    checksum = (modbus_crc16( bytearray.fromhex(frame[8:-4])))
    byte_value = c_ubyte(checksum & 0xFF).value  # Extract integer value
    crc_high = (bytearray([byte_value]))  # Use integer for bytearray
    crc_low = (bytearray([c_ubyte((checksum >> 8) & 0xFF).value]))  # Append high byte too
    return  crc_high,crc_low

def modbus_crc16( senddata):
    wcrc = 0xFFFF  # 预置16位crc寄存器，初值全部为1
    for byte in senddata:  # 循环计算每个数据
        wcrc ^= byte if isinstance(byte, int) else ord(byte)  # 转换为整数
        for _ in range(8):  # 循环8次
            if wcrc & 0x0001:  # 判断右移出的是不是1，如果是1则与多项式进行异或
                wcrc >>= 1  # 先将数据右移一位
                wcrc ^= 0xA001  # 与上面的多项式进行异或
            else:
                wcrc >>= 1  # 如果不是1，则直接移出
    return wcrc


def check_sum(frame: QByteArray) -> int:
    sum = 0
    header_length = 4  # 假设帧头长度为4字节
    for i in range(header_length, frame.size()):
        byte = int.from_bytes(frame[i], byteorder='big')  # 将字节转换为整数
        sum += byte
    return sum & 0xFFFF  # 取最后两个字节作为校验和


def ieee754_hex_str_to_float_little_endian(val: str) -> float:
    ba = bytes.fromhex(val)
    if len(ba) != 4:
        return 0.0

    # Little-endian format
    word = (ba[3] << 24) | (ba[2] << 16) | (ba[1] << 8) | ba[0]
    return struct.unpack('<f', struct.pack('<I', word))[0]

def ieee754_hex_str_to_float_big_endian(val: str) -> float:
    ba = bytes.fromhex(val)
    if len(ba) != 4:
        return 0.0

    # Big-endian format
    word = (ba[0] << 24) | (ba[1] << 16) | (ba[2] << 8) | ba[3]
    return struct.unpack('>f', struct.pack('>I', word))[0]


def hex_str_to_bytearray(data):
    def hex_str_to_char(data):
        if '0' <= data <= '9':
            return ord(data) - 0x30
        elif 'A' <= data <= 'F':
            return ord(data) - ord('A') + 10
        elif 'a' <= data <= 'f':
            return ord(data) - ord('a') + 10
        else:
            return -1

    senddata = bytearray()
    len_data = len(data)
    i = 0

    while i < len_data:
        hstr = data[i]
        if hstr == ' ':
            i += 1
            continue
        i += 1
        if i >= len_data:
            break
        lstr = data[i]
        hexdata = hex_str_to_char(hstr)
        lowhexdata = hex_str_to_char(lstr)
        if hexdata == -1 or lowhexdata == -1:
            break
        senddata.append((hexdata << 4) + lowhexdata)
        i += 1

    return senddata

def float_to_hex(value):
    # Convert float to bytes
    byte_array = struct.pack('!f', value)
    
    # Convert bytes to hexadecimal string
    hex_string = byte_array.hex().upper().rjust(8, '0')  # Ensures it's 4 bytes long, padded with zeros if necessary

    return hex_string

def uint_to_hex_32(value):
    # 使用 & 0xFFFFFFFF 确保负数被正确转换为32位无符号整数的十六进制表示
    return hex(value & 0xFFFFFFFF)[2:].zfill(8)

def int_to_hex_32(value):
    return hex(value & 0xFFFFFFFF)[2:].zfill(8)

def int_to_hex_8(value):
    return hex(value & 0xFF)[2:].zfill(2)

def is_positive_float_include_zero(s):
    try:
        f = float(s)
        return f >= 0
    except ValueError:
        return False

def is_positive_float(s):
    try:
        f = float(s)
        return f > 0
    except ValueError:
        return False
    
def get_six_axis_data(frame:str) -> List[int]:
    frame = frame[16:64]
    data = []
    for i in range(6):
        hex_value = frame[8*i:8*i+8]
        decimal_value = int(hex_value, 16)
        if decimal_value >= 2**31:  # 检查是否为负数
            decimal_value -= 2**32  # 转换为有符号整数
        data.append(decimal_value)
    return data
