import ctypes

MAX_MSG_LEN = 8
XL_CAN_EXT_MSG_ID = 0x80000000
XLuint64 = ctypes.c_uint64
XLstatus = ctypes.c_short

XLlong = ctypes.c_long
XLportHandle = XLlong
pXLportHandle = ctypes.POINTER(XLportHandle)

XLaccessMark = ctypes.c_uint
class CAN(ctypes.Structure):
    _fields_ = [
        ("bitRate", ctypes.c_uint),
        ("sjw", ctypes.c_ubyte),
        ("tseg1", ctypes.c_ubyte),
        ("tseg2", ctypes.c_ubyte),
        ("sam", ctypes.c_ubyte),
        ("outputMode", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte * 7),
        ("canOpMode", ctypes.c_ubyte)
    ]

class CANFD(ctypes.Structure):
    _fields_ = [
        ("arbitrationBitRate", ctypes.c_uint),
        ("sjwAbr", ctypes.c_ubyte),
        ("tseg1Abr", ctypes.c_ubyte),
        ("tseg2Abr", ctypes.c_ubyte),
        ("samAbr", ctypes.c_ubyte),
        ("outputMode", ctypes.c_ubyte),
        ("sjwDbr", ctypes.c_ubyte),
        ("tseg1Dbr", ctypes.c_ubyte),
        ("tseg2Dbr", ctypes.c_ubyte),
        ("dataBitRate", ctypes.c_uint),
        ("canOpMode", ctypes.c_ubyte)
    ]

class MOST(ctypes.Structure):
    _fields_ = [
        ("activeSpeedGrade", ctypes.c_uint),
        ("compatibleSpeedGrade", ctypes.c_uint),
        ("inicFwVersion", ctypes.c_uint)
    ]

class FlexRay(ctypes.Structure):
    _fields_ = [
        ("status", ctypes.c_uint),
        ("cfgMode", ctypes.c_uint),
        ("baudrate", ctypes.c_uint)
    ]

class Ethernet(ctypes.Structure):
    _fields_ = [
        ("macAddr", ctypes.c_ubyte * 6),
        ("connector", ctypes.c_ubyte),
        ("phy", ctypes.c_ubyte),
        ("link", ctypes.c_ubyte),
        ("speed", ctypes.c_ubyte),
        ("clockMode", ctypes.c_ubyte),
        ("bypass", ctypes.c_ubyte)
    ]

class Tx(ctypes.Structure):
    _fields_ = [
        ("bitrate", ctypes.c_uint),
        ("parity", ctypes.c_uint),
        ("minGap", ctypes.c_uint)
    ]

class Rx(ctypes.Structure):
    _fields_ = [
        ("bitrate", ctypes.c_uint),
        ("minBitrate", ctypes.c_uint),
        ("maxBitrate", ctypes.c_uint),
        ("parity", ctypes.c_uint),
        ("minGap", ctypes.c_uint),
        ("autoBaudrate", ctypes.c_uint)
    ]

class Dir(ctypes.Union):
    _fields_ = [
        ("tx", Tx),
        ("rx", Rx),
        ("raw", ctypes.c_ubyte * 24)
    ]

class A429(ctypes.Structure):
    _fields_ = [
        ("channelDirection", ctypes.c_ushort),
        ("res1", ctypes.c_ushort),
        ("dir", Dir)
    ]

class Data(ctypes.Union):
    _fields_ = [
        ("can", CAN),
        ("canFD", CANFD),
        ("most", MOST),
        ("flexray", FlexRay),
        ("ethernet", Ethernet),
        ("a429", A429),
        ("raw", ctypes.c_ubyte * 28)
    ]
class XLbusParams(ctypes.Structure):
    _fields_ = [
        ("busType", ctypes.c_uint),
        ("data", Data)
    ]
class XLchannelConfig(ctypes.Structure):
    _pack_ = 1
    _fields_ = [
        ("name", ctypes.c_char * 32),
        ("hwType", ctypes.c_ubyte),
        ("hwIndex", ctypes.c_ubyte),
        ("hwChannel", ctypes.c_ubyte),
        ("transceiverType", ctypes.c_ushort),
        ("transceiverState", ctypes.c_uint),
        ("channelIndex", ctypes.c_ubyte),
        ("channelMask", XLuint64),
        ("channelCapabilities", ctypes.c_uint),
        ("channelBusCapabilities", ctypes.c_uint),
        ("isOnBus", ctypes.c_ubyte),
        ("connectedBusType", ctypes.c_uint),
        ("busParams", XLbusParams),
        ("driverVersion", ctypes.c_uint),
        ("interfaceVersion", ctypes.c_uint),
        ("raw_data", ctypes.c_uint * 10),
        ("serialNumber", ctypes.c_uint),
        ("articleNumber", ctypes.c_uint),
        ("transceiverName", ctypes.c_char * 32),
        ("specialCabFlags", ctypes.c_uint),
        ("dominantTimeout", ctypes.c_uint),
        ("reserved", ctypes.c_uint * 8)
    ]
class XLdriverConfig (ctypes.Structure):
    _fields_ = [
        ("dllVersion", ctypes.c_uint),
        ("channelCount", ctypes.c_uint),
        ("reserved", ctypes.c_uint * 10),
        ("channel", XLchannelConfig * 64)
    ]

class XLcanMsg(ctypes.Structure):
    _fields_ = [
        ("id", ctypes.c_ulong),
        ("flags", ctypes.c_ushort),
        ("dlc", ctypes.c_ushort),
        ("res1", XLuint64),
        ("data", ctypes.c_ubyte * MAX_MSG_LEN),
        ("res2", XLuint64)
    ]
class XLevent(ctypes.Structure):
    _fields_ = [
        ("tag", ctypes.c_ubyte),
        ("chanIndex", ctypes.c_ubyte),
        ("transId", ctypes.c_ushort),
        ("portHandle", ctypes.c_ushort),
        ("flags", ctypes.c_ubyte),
        ("reserved", ctypes.c_ubyte),
        ("timeStamp", XLuint64),
        ("msg", XLcanMsg)
    ]

class CanMessage():
    def __init__(self, id, data, period):
        self.id = id
        self.data = data
        self.period = period

