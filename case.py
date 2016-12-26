import logging
import traceback
try:
    import time
    from gpib import *
    from power import *
    from multimeter import *
    from datapool import datapoolclass
    from PySide import QtCore
    import random
    import math
    import json
    from fantray import fantray_class
except:
    info=traceback.format_exc()
    logging.info(info)

class case_class(QtCore.QObject):
    sig_case = QtCore.Signal(str)
    def __init__(self):
        super(case_class, self).__init__()
        self.datapool = datapoolclass()
    def double_test(self,caller):
        self.datapool.clear_pool()
        self.datapool.append_menber('data1', [])
        self.datapool.append_menber('data2', [])
        # self.datapool.append_menber('data3', [])
        # self.datapool.append_menber('data4', [])
        # self.datapool.append_menber('data5', [])
        # self.datapool.append_menber('data6', [])
        for i in range(10000000):
            if not caller.runing:
                break
            self.datapool.append_value('data1', [i,random.randrange(0,100)])
            self.datapool.append_value('data2', [i,random.randrange(0,20)])
            # self.datapool.append_value('data3', [i, random.randrange(0,30)])
            # self.datapool.append_value('data4', [i, random.randrange(0,40)])
            # self.datapool.append_value('data5', [i, random.randrange(0,50)])
            # self.datapool.append_value('data6', [i, random.randrange(0,60)])
            self.datapool.update()
            time.sleep(1)

    def gpib_dev_test(self,addr='',name='dev'):
        gpib = init_gpib()
        try:
            dev= open_dev(gpib, addr)
        except:
            self.sig_case.emit('open %s failed  '%(name))
        else:
            try:
                self.sig_case.emit(get_info(dev))
            except:
                self.sig_case.emit('get %s info failed'%(name))
            else:
                self.sig_case.emit('open %s successed'%(name))
        try:
            close_dev(dev)
        except:
            pass
        remove_gpib(gpib)




    def test(self,caller):
        self.sig_case.emit('test start')
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()
        self.sig_case.emit('power: '+res['pow_addr'])
        self.gpib_dev_test(res['pow_addr'], 'pow')

        self.sig_case.emit('voltage: '+res['vol_addr'])
        self.gpib_dev_test(res['vol_addr'], 'vol')

        self.sig_case.emit('current: '+res['cur_addr'])
        self.gpib_dev_test(res['cur_addr'], 'cur')

        self.sig_case.emit('fantray: '+res['imbus_addr'])
        imbus_addr = res['imbus_addr'].split(':', 1)
        try:
            fantry = fantray_class()
            fantry.open_imbus(imbus_addr[0], int(imbus_addr[1]))
        except:
            self.sig_case.emit("can't connect fantray serial server")
        else:
            try:
                print fantry.get_volte(0)
               #self.sig_case.emit('fantray voltage A :'+fantry.get_volte())
            except:
                self.sig_case.emit("can't open fantray device")
            else:
                self.sig_case.emit('open fantray successed ')
            fantry.close_imbus()
        self.sig_case.emit('test end')


    def uv_ov(self,caller):
        self.datapool.clear_pool()
        print 'uv_ov'
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()

        step_num =int(math.ceil( math.fabs( (float(res['uv_ov_begin'])-float(res['uv_ov_end']))/float(res['uv_ov_step']) ) ))
        set_vol = float(res['uv_ov_begin'])

        if float(res['uv_ov_begin'])-float(res['uv_ov_end'])<0:
            step = math.fabs( float(res['uv_ov_step']))
        else:
            step = -math.fabs(float(res['uv_ov_step']))
        interval =float(res['uv_ov_interval'])
        self.datapool.append_menber('unit', '(V)/(A)')
        self.datapool.append_menber('Current', [])
        try:
            gpib = init_gpib()
            dev_pow = open_dev(gpib, res['pow_addr'])
            dev_vol=open_dev(gpib, res['vol_addr'] )
            dev_cur = open_dev(gpib, res['cur_addr'])
        except:
            print "can't open GPIB device"
        else:
            print get_info(dev_pow)
            print get_info(dev_vol)
            print get_info(dev_cur)

            power_set_vol(dev_pow, set_vol)
            power_set_cur(dev_pow, 10)
            power_on(dev_pow)
            time.sleep(10)
            for i in range(step_num+1):
                if not caller.runing:
                    break
                power_set_vol(dev_pow, set_vol)
                time.sleep(interval/2)

                #power_read_vol(dev_pow)

                vol = round(float(get_mul_vol(dev_vol)), 2)
                cur = round(float(get_mul_vol(dev_cur))*1000/float(res['uv_ov_samp_res']), 2)
                print vol ,cur

                self.datapool.append_value('Current', [vol, cur])


                self.datapool.update()
                set_vol += step

                time.sleep(interval/2)

            power_off(dev_pow)
            close_dev(dev_pow)
            close_dev(dev_vol)
            close_dev(dev_cur)
            remove_gpib(gpib)

        print 'end'
    def rpm_rpm_per(self, caller):
        self.datapool.clear_pool()
        print 'rpm rpm %'
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()
        imbus_addr = res['imbus_addr'].split(':', 1)
        self.datapool.append_menber('unit', '(%)/(PPM)')
        fantry = fantray_class()
        fantry.open_imbus(imbus_addr[0], int(imbus_addr[1]))

        for i in range(4):
            self.datapool.append_menber('RPM%s' % (i), [])
            fantry.set_rpm_per(i, 0)
        time.sleep(5)
        for i in range(101):
            if not caller.runing:
                break
            for j in range(4):
                fantry.set_rpm_per(j, i)
            time.sleep(3)

            for j in range(4):
                rpm = fantry.read_rpm(j)
                self.datapool.append_value('RPM%s' % (j), [i, rpm])
            self.datapool.update()
        for i in range(4):
            fantry.set_rpm_per(i, 0)
        fantry.close_imbus()
        print 'end'


    def power_rpm_per(self,caller):
        print 'power rpm %'
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()
        imbus_addr=res['imbus_addr'].split(':',1)
        self.datapool.append_menber('unit', '(%)/(W)')
        self.datapool.append_menber('power', [])
        fantry = fantray_class()
        fantry.open_imbus(imbus_addr[0], int(imbus_addr[1]))

        try:
            gpib = init_gpib()
            dev_vol = open_dev(gpib, res['vol_addr'])
            dev_cur = open_dev(gpib, res['cur_addr'])
        except:
            print "can't open GPIB device"
        else:
            print get_info(dev_vol)
            print get_info(dev_cur)

        for i in range(4):
             fantry.set_rpm_per(i, 0)
        time.sleep(5)

        for i in range(101):            # set RPM 0-100 %
             if not caller.runing:
                 break
             for j in range(4):
                fantry.set_rpm_per(j,i)
             time.sleep(3)
             #read power
             vol = round(float(get_mul_vol(dev_vol)), 2)
             cur = round(float(get_mul_vol(dev_cur)) * 1000 / float(res['uv_ov_samp_res']), 2)
             power =vol *cur
             print vol ,cur
             self.datapool.append_value('power', [i,power])
             self.datapool.update()



        for i in range(4):             # set rpm 0 at end
             fantry.set_rpm_per(i, 0)

        close_dev(dev_vol)             # close vol ,cur multimeter
        close_dev(dev_cur)
        remove_gpib(gpib)              # close gpib
        fantry.close_imbus()           # close imnud
        print 'end'

    def temp_rpm_per(self, caller):
        self.datapool.clear_pool()
        print 'temp rpm %'
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()
        imbus_addr = res['imbus_addr'].split(':', 1)
        self.datapool.append_menber('unit', '(T)/(deg|100RPM)')
        fantray = fantray_class()
        fantray.open_imbus(imbus_addr[0], int(imbus_addr[1]))
        self.datapool.append_menber('senser', [])
        for i in range(4):
            self.datapool.append_menber('RPM%s' % (i), [])
        fantray.mode_set('AUTO')
        time.sleep(5)
        for i in range(5000):
            if not caller.runing:
                break
            temp=0
            try:
                for j in range(4):
                    temp += fantray.read_temp(j)
                    rpm = fantray.read_rpm(j)
                    self.datapool.append_value('RPM%s' % (j), [i, rpm/100])
            except:
                i-=1
                print 'error %s'%(i)
                fantray.close_imbus()
                fantray.open_imbus(imbus_addr[0], int(imbus_addr[1]))
                continue
            else:
                self.datapool.append_value('senser', [i, float(temp)/4])
                self.datapool.update()
            time.sleep(5)
        fantray.close_imbus()
        print 'end'










def case2(caller):
    for i in range(50):
        if caller.runing == True:
            # print 'get vol'
            # data.data_append( 1, get_vol(dev))
            print 'case2'
            time.sleep(2)
        else:
            break
    print 'end'

