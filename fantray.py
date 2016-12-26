from imbus import imbus_class

# 13 read 11 write

class fantray_class():
    def open_imbus(self,HOST= "10.220.52.30", PORT = 10003):
        self.imbus = imbus_class()
        self.imbus.imbus_open(HOST,PORT)
        self.imbus.clear_error_buf() # Solve the problem that some serial server port Receive Buf generate redundancy data

    def close_imbus(self):
        self.imbus.imbus_close()

    def get_volte(self,flag):
        res=self.imbus.imbus_read([0x10, 0x04+flag])
        return float(res[3]*256+res[4])/100

    def get_curent(self,flag):
        res = self.imbus.imbus_read([0x10, 0x08 + flag])
        return float(res[3]*256+res[4])

    def read_rpm(self,flag):
        res = self.imbus.imbus_read([0x10, 0x10 + flag])
        return res[3] * 256 + res[4]
    def read_temp(self,flag):# flag 0 ,1,2,3
        res = self.imbus.imbus_read([0x10, 0x16 + flag])
        return  res[4]-128

    def un_lock_write(self):
        res =self.imbus.imbus_write([0x10, 0xff], [0xcf, 0x05])
        return  res

    def lock_write(self):
        res = self.imbus.imbus_write([0x10, 0xff], [0x00, 0x00])
        return res

    def read_rpm_per(self,flag):
        res = self.imbus.imbus_read([0x10, 0x0c + flag])
        return res[3], res[4]

    def mode_set(self,flag):
        res = self.imbus.imbus_read([0x10, 0x0c]) #just set one resister to change mode
        if flag == 'AUTO':
            mode = res[4] & 0xfc
        elif flag == 'HOST':
            mode = res[4] | 0x03
        self.un_lock_write()
        self.imbus.imbus_write([0x10, 0x0c], [res[3], mode])
        self.lock_write()
    #def get_mode(self):
        #res = self.imbus.imbus_read([0x10, 0x0c])  # just set one resister to change mode


    def set_rpm_per(self,flag,rpm):
        res = self.imbus.imbus_read([0x10, 0x0c + flag])
        self.un_lock_write()
        res2=self.imbus.imbus_write([0x10, 0x0c + flag], [rpm, res[4]])
        self.lock_write()
        self.mode_set('HOST')
        return res2

    def read_eerom(self):
        buf='EEPROM Shadow Registers\n'
        for i in range(128/2):
            res = self.imbus.imbus_read([0x20, 0x00 + i])
            buf += chr(res[3])
            buf += chr(res[4])
        return buf
    def read_all(self):
        buf=''
        #buf+='Test Registers\n\n'
        # for i in range(0x0000,0x0fff+1):
        #     addr=[i/256,i%256]
        #     res = self.imbus.imbus_read(addr)
        #     buf += hex(i) + ':' + hex(res[3]*256+res[4])+'\n'
        buf += 'Control and Status Registers\n'
        for i in range(0x1000,0x1023+1):
            addr=[i/256,i%256]
            res = self.imbus.imbus_read(addr)
            buf += hex(i) + ':' + hex(res[3]*256+res[4])+'\n'
        # buf += 'I2C Master Registers\n'
        # for i in range(0x1100,0x11ff+1):
        #     addr=[i/256,i%256]
        #     res = self.imbus.imbus_read(addr)
        #     buf += hex(i) + ':' + hex(res[3]*256+res[4])+'\n'
        buf += 'EEPROM Shadow Registers\n'
        for i in range(0x2000, 0x2040+1):
            print i
            addr = [i / 256, i % 256]
            res = self.imbus.imbus_read(addr)
            buf += hex(i) + ':' + hex(res[3] * 256 + res[4]) + '\n'
            # buf += chr(res[3])
            # buf += chr(res[4])
        return buf


# fantray =fantray_class()
# fantray.open_imbus('10.220.52.30',10003)
# print fantray.get_volte(0)
# fantray.close_imbus()