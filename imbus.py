import socket
import time


class imbus_class():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(0.5)
    def imbus_open(self,HOST,PORT):
        try:
            self.sock.connect((HOST,PORT))
        except:
            print "time out"
    def clear_error_buf(self,):
        try:
            print self.sock.recv(256)
        except:
            print 'clear_error_buf time out'

    def imbus_write(self,addr=[],value=[]):
        self.imbus_send_pack([0x11, addr[0], addr[1],value[0], value[1]])
        res = self.sock.recv(6)
        hex_res = self.str_to_hex(res)
        if hex_res[5] == self.crc_8(hex_res[0:5]):
            return hex_res[0:5]
        else:
            return 0

    def imbus_read(self,addr=[]):
        self.imbus_send_pack([0x13, addr[0], addr[1], 0x00, 0x00])
        res = self.sock.recv(256)
        hex_res = self.str_to_hex(res)
        if hex_res[5] == self.crc_8(hex_res[0:5]):
            return hex_res[0:5]
        else:
            return 0

    def imbus_send_pack(self,value=[]):
        crc=self.crc_8(value)
        value.append(crc)
        #print value
        string=''
        for  i in value:
            string+=chr(i)
        self.sock.send(string)

    def str_to_hex(self, string=''):
        res = []
        for i in string:
            res.append(ord(i))
        return res

    def imbus_close(self):
        self.sock.close()

    def crc_8(self,value,div=0x107):
        w= div.bit_length()-1     # X8+X2+X+1
        #print w
        temp =0
        for i in range(len(value)):
            temp += value[i]<<(len(value)-i)*w
        div = div << temp.bit_length() - div.bit_length()
        while 1:
            if temp.bit_length()>w:
                temp ^= div
                div = div >>div.bit_length()-temp.bit_length()
                #print bin(temp) ,bin(div)
            else:
                break
        return  temp



    #
    # def crc16(self, data = []):
    #     crc = 0xffff
    #     for i in range(len(data)):
    #         crc ^= data[i]
    #         for j in range(8):
    #             flag = crc & 1
    #             if flag == 1:
    #                 crc = crc >> 1
    #                 crc = crc ^ 0xa001
    #             else:
    #                 crc = crc >> 1
    #     return crc
    #
    # def crc81(self, data = []):
    #     crc = 0
    #     for i in range(len(data)):
    #         crc ^= data[i]
    #         for j in range(8):
    #             flag = crc & 1
    #             if flag == 1:
    #                 crc = crc >> 1
    #                 crc = crc ^ 0x107
    #             else:
    #                 crc = crc >> 1
    #
    #     return crc
    #
    #
    #
#print '%x'%imbus.crc_8([0x12, 0x10, 0xff, 0xcf, 0x05 ])
#print '%x'%imbus.crc81([0x12, 0x10, 0xff, 0xcf, 0x05])
#print '%x'%imbus.crc16([0x12, 0x10, 0xff, 0xcf, 0x05])
















# import serial
# import time
# try:
#     ser = serial.Serial('COM7',57600,timeout=0.1)
# except:
#     print "connect fail"
# else:
#     print "connect"
#     ser.write(chr(0x48))
#     res = ser.read(1)
#     print '0x%x'%(ord(res))
#
#     ser.close()
#     print "close"
