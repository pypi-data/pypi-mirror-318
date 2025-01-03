import ctypes
import logging
from simpleCan.util import dataStructure as ds
import os

util_path = os.path.dirname(os.path.abspath(__file__))
simpleCan_path = os.path.dirname(util_path)
dll_file_path = os.path.join(simpleCan_path, 'dll_file')
dll_path = os.path.join(dll_file_path,'vxlapi64.dll')
_xlapi_dll = ctypes.windll.LoadLibrary(dll_path)
libc = ctypes.CDLL("msvcrt.dll")

# initialize functions
xlOpenDriver = _xlapi_dll.xlOpenDriver
xlGetDriverConfig = _xlapi_dll.xlGetDriverConfig
xlGetDriverConfig.argtypes = [ctypes.POINTER(ds.XLdriverConfig)]

xlOpenPort = _xlapi_dll.xlOpenPort
xlActivateChannel = _xlapi_dll.xlActivateChannel

xlCanTransmit = _xlapi_dll.xlCanTransmit
xlCanTransmit.argtypes = [
    ds.XLportHandle,
    ds.XLaccessMark,
    ctypes.POINTER(ctypes.c_uint),
    ctypes.POINTER(ds.XLevent),
]
xlCanTransmit.restype = ds.XLstatus

xlGetErrorString = _xlapi_dll.xlGetErrorString

libc.memset.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_size_t]
libc.memset.restype = ctypes.c_void_p

# initialize parameters
xlChannelConfig = ds.XLchannelConfig()

portHandle = ds.XLportHandle()
userName = " "
accessMark = 1
permissionMask = ctypes.c_uint64(1)
rx_queue_size = ctypes.c_uint(1)
xlInterfaceVersion = ctypes.c_uint(3)
busType = ctypes.c_uint(1)
XLeventTag_transmit = 10
flags = 0
dlc = 8

# send signal per function call
def sendData(messageID, data):
    canID = ds.XL_CAN_EXT_MSG_ID | messageID
    myXLevent = (ds.XLevent * 10)()
    message_count = ctypes.c_uint(len(data))
    try:
        libc.memset(myXLevent, 0, ctypes.sizeof(myXLevent))
        for i in range(10):
            myXLevent[i].tag = XLeventTag_transmit
            myXLevent[i].msg.id = canID
            myXLevent[i].msg.flags = flags
            myXLevent[i].msg.data[0] = data[0]
            myXLevent[i].msg.data[1] = data[1]
            myXLevent[i].msg.data[2] = data[2]
            myXLevent[i].msg.data[3] = data[3]
            myXLevent[i].msg.data[4] = data[4]
            myXLevent[i].msg.data[5] = data[5]
            myXLevent[i].msg.data[6] = data[6]
            myXLevent[i].msg.data[7] = data[7]
            myXLevent[i].msg.dlc = dlc
        result = xlCanTransmit(portHandle, accessMark, message_count, myXLevent)
        if result == 0:
            logging.info('send message ' + str(hex(messageID)) + ' result ' + str(result))
        else:
            logging.error('send message ' + str(hex(messageID)) + ' result ' + str(result))
    except Exception as e:
        logging.error(f"Error: {e}")

def setup():
    xlstatus = xlOpenDriver()
    logging.info('open driver result is ' + str(xlstatus))
    xlstatus = xlOpenPort(ctypes.pointer(portHandle),
                          userName,
                          accessMark,
                          ctypes.pointer(permissionMask),
                          rx_queue_size,
                          xlInterfaceVersion,
                          busType)
    logging.info('open port result is ' + str(xlstatus))
    xlstatus = xlActivateChannel(portHandle,
                                 accessMark,
                                 busType,
                                 0)
    logging.info('open driver result is ' + str(xlstatus))





