from PySide import  QtGui ,QtCore
from workbench_ui import Ui_MainWindow
import logging
import traceback
try:
    from task import task_class
except:
    info = traceback.format_exc()
    print info
    logging.info(info)

from curve import curve_class
from two_d import two_d_class
#from three_d import three_d_class
from fantray import fantray_class
import json
class manager_class(object):
    def __init__(self):
        pass
        self.task=task_class()
    def put_ui(self,parent):
        self.mainwindow = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.mainwindow)
        self.menu_bar()
        self.ui.down_tabWidget.setCurrentWidget(self.ui.tab_device)
        self.device_mebers =['pow_addr', 'vol_addr', 'cur_addr','imbus_addr']
        self.uv_ov_mebers = ['uv_ov_begin', 'uv_ov_end', 'uv_ov_step', 'uv_ov_interval','uv_ov_samp_res']

        ################ uv_ov inition  ###################
        self.put_conf(self.device_mebers+self.uv_ov_mebers,'conf/test.conf')
        #####################################
    def put_curve(self):
        self.c = curve_class()
        self.ui.tabWidget_2.addTab(self.c,'Curve')

        #self.ui.gridLayout.addWidget(self.c,0,0,1,1)
    def put_2D(self):
        self.two_d=two_d_class()
        self.ui.tabWidget_2.addTab(self.two_d, ' 2D ')
    def put_3D(self):
        self.three_d=three_d_class()
        self.ui.tabWidget_2.addTab(self.three_d,' 3D ')
    def put_textbrowser(self):
        self.textbrowser=QtGui.QTextBrowser()
        #self.textbrowser.setStyleSheet("background-color: rgb(20, 20, 100);")
        self.ui.tabWidget_2.addTab(self.textbrowser,'print')


    def menu_bar(self):
        self.ui.fileMenu = QtGui.QMenu("&File",self.mainwindow)
        self.openAct = QtGui.QAction("&Open...", self.mainwindow, shortcut="Ctrl+O",triggered=self.open)
        self.saveAct = QtGui.QAction("&Save...", self.mainwindow, shortcut="Ctrl+S",triggered=self.save)
        self.savePictureAct = QtGui.QAction("&Save Picture...", self.mainwindow, shortcut="Ctrl+P", triggered=self.save_pic)

        self.ui.fileMenu.addAction(self.openAct)
        self.ui.fileMenu.addAction(self.saveAct)
        self.ui.fileMenu.addAction(self.savePictureAct)

        self.ui.editMenu = QtGui.QMenu("&Edit")
        self.ui.helpMenu = QtGui.QMenu("&Help")

        self.ui.menubar.addMenu(self.ui.fileMenu)
        self.ui.menubar.addMenu(self.ui.editMenu)
        self.ui.menubar.addMenu(self.ui.helpMenu)
    def open(self):
        fileName,_ = QtGui.QFileDialog.getOpenFileName(self.mainwindow, "Open File",QtCore.QDir.currentPath())
        if not fileName:
            return
        fc = open(str(fileName), 'r')
        res = json.load(fc)
        fc.close()
        self.task.case.datapool.clear_pool()
        self.task.case.datapool.copy_pool(res)
        self.c.curve_update()       ##########



    def save(self):
        fileName, _ = QtGui.QFileDialog.getSaveFileName(self.mainwindow,"Save Test Data", '',
                                                        " Test (*.json);;All Files (*)")
        fc = open(str(fileName), 'wb')
        json.dump(self.task.case.datapool.pool, fc)
        fc.close()
    def save_pic(self):
        fileName, _ = QtGui.QFileDialog.getSaveFileName(self.mainwindow,"Save Test Picture", '',
                                                        " Test (*.png);;All Files (*)")

        self.c.save_pic(fileName)

    def sig_slot(self):
        self.task.case.datapool.sig_datapool_update.connect(self.curve_update)
        self.task.case.sig_case.connect(self.case_info)

        ############################## dev ####################################
        self.ui.uv_ov_connect_testButton.clicked.connect(self.conncet_test)


        ############################## uv_ov ####################################
        self.ui.uv_ov_startButton.clicked.connect(self.uv_ov_star)
        self.ui.uv_ov_stopButton.clicked.connect(self.uv_ov_stop)
        ################################# rpm rpm #########################################
        self.ui.rpm_start_button.clicked.connect(self.rpm_rpm_star)
        self.ui.rpm_stop_button.clicked.connect(self.rpm_rpm_stop)
        ################################# pow rpm #########################################
        self.ui.power_start_button.clicked.connect(self.pow_rpm_star)
        self.ui.power_stop_button.clicked.connect(self.pow_rpm_stop)
        ################################# temp rpm #########################################
        self.ui.temp_start_button.clicked.connect(self.temp_rpm_star)
        self.ui.temp_stop_button.clicked.connect(self.temp_rpm_stop)
        ############################## fantray ###################################
        self.ui.refresh_Button.clicked.connect(self.fantray_refresh)
        self.ui.readall_Button.clicked.connect(self.fantray_readall)
        self.ui.set_rpm_pushButton.clicked.connect(self.set_rpm)

    def curve_update(self):
        self.c.curve_update()

    def case_info(self,string):
        self.textbrowser.append(string)

    def conncet_test(self):
        self.save_conf(self.device_mebers + self.uv_ov_mebers, 'conf/test.conf')
        self.ui.tabWidget_2.setCurrentWidget(self.textbrowser)
        self.task.tasks_add(31)

    def rpm_rpm_star(self):
        self.task.tasks_add(14)
    def rpm_rpm_stop(self):
        self.task.tasks_remove(14)

    def pow_rpm_star(self):
        self.task.tasks_add(15)
    def pow_rpm_stop(self):
        self.task.tasks_remove(15)

    def temp_rpm_star(self):
        self.task.tasks_add(16)
    def temp_rpm_stop(self):
        self.task.tasks_remove(16)



        # self.c.clear_sign()
        # self.task.tasks_add(11)
    def save_conf(self,members,name):
        test_conf = {}
        for i in members:
            test_conf[i] = eval('self.ui.' + i + '.text()')
        fc = open(name, 'w')
        json.dump(test_conf, fc)
        fc.close()
    def put_conf(self,members,name):
        try:
            fc = open(name, 'r')  # read previous  parameter from 'conf/uv_ov.conf'
            res = json.load(fc)
            fc.close()
            for i in members:
                eval('self.ui.'+i+'.setText(res[i])')
        except:
            print 'init conf failed'



    def uv_ov_star(self):
        self.c.clear_sign()
        temp1 = float(self.ui.uv_ov_begin.text()) -float(self.ui.uv_ov_end.text())
        temp2 =float(self.ui.uv_ov_step.text())
        if temp1 *temp2 >=0:
            self.ui.uv_ov_information.setText('pleas confirm input parameter')
        if float(self.ui.uv_ov_interval.text())<1:
            self.ui.uv_ov_interval.setText('1')

        self.save_conf(self.device_mebers + self.uv_ov_mebers, 'conf/test.conf')
        self.task.tasks_add(13)

    def uv_ov_stop(self):
        self.task.tasks_remove(13)

    def fantray_refresh(self):
        print 'fantray refresh'
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()
        imbus_addr = res['imbus_addr'].split(':', 1)
        fantray = fantray_class()
        fantray.open_imbus(imbus_addr[0], int(imbus_addr[1]))

        print fantray.get_volte(0),fantray.get_volte(1)
        self.ui.lcdNumber.display(fantray.get_volte(0))
        self.ui.lcdNumber_2.display(fantray.get_volte(1))
        self.ui.curent0.display(fantray.get_curent(0))
        self.ui.curent1.display(fantray.get_curent(1))
        fanspeed = [0, 0, 0, 0]
        for i in range(4):
            fanspeed[i] = fantray.read_rpm(i)
            self.two_d.set_fanspeed(i,fanspeed[i])

        self.ui.rpmlcd_0.display(fanspeed[0])
        self.ui.rpmlcd_1.display(fanspeed[1])
        self.ui.rpmlcd_2.display(fanspeed[2])
        self.ui.rpmlcd_3.display(fanspeed[3])
        fantray.close_imbus()
    def fantray_readall(self):
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()
        imbus_addr = res['imbus_addr'].split(':', 1)
        fantray = fantray_class()
        fantray.open_imbus(imbus_addr[0], int(imbus_addr[1]))
        self.textbrowser.setText(fantray.read_all())
        fantray.close_imbus()


    def set_rpm(self):
        fc = open('conf/test.conf', 'r')
        res = json.load(fc)
        fc.close()
        imbus_addr = res['imbus_addr'].split(':', 1)
        fantray = fantray_class()
        fantray.open_imbus(imbus_addr[0], int(imbus_addr[1]))
        for i in range(4):
            fantray.set_rpm_per(i , int(self.ui.rpm_lineEdit.text()))
        # fantray.set_rpm_per(0, 10)
        # fantray.set_rpm_per(1, 40)
        # fantray.set_rpm_per(2, 10)
        # fantray.set_rpm_per(3, 60)
        fantray.close_imbus()









       
        
