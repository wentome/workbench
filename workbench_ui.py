# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\test\ui\workbench.ui'
#
# Created: Tue Nov 08 17:20:15 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 641)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.gridLayout.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        self.down_tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.down_tabWidget.setEnabled(True)
        self.down_tabWidget.setStyleSheet("background-color: rgb(212, 212, 212);\n"
"")
        self.down_tabWidget.setObjectName("down_tabWidget")
        self.tab_device = QtGui.QWidget()
        self.tab_device.setObjectName("tab_device")
        self.pow_addr = QtGui.QLineEdit(self.tab_device)
        self.pow_addr.setGeometry(QtCore.QRect(100, 30, 101, 21))
        self.pow_addr.setObjectName("pow_addr")
        self.vol_addr = QtGui.QLineEdit(self.tab_device)
        self.vol_addr.setGeometry(QtCore.QRect(100, 60, 101, 20))
        self.vol_addr.setObjectName("vol_addr")
        self.label_13 = QtGui.QLabel(self.tab_device)
        self.label_13.setGeometry(QtCore.QRect(30, 30, 46, 13))
        self.label_13.setObjectName("label_13")
        self.label_3 = QtGui.QLabel(self.tab_device)
        self.label_3.setGeometry(QtCore.QRect(30, 60, 46, 13))
        self.label_3.setObjectName("label_3")
        self.cur_addr = QtGui.QLineEdit(self.tab_device)
        self.cur_addr.setGeometry(QtCore.QRect(100, 90, 101, 20))
        self.cur_addr.setObjectName("cur_addr")
        self.label_4 = QtGui.QLabel(self.tab_device)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 46, 13))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtGui.QLabel(self.tab_device)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 61, 16))
        self.label_2.setObjectName("label_2")
        self.imbus_addr = QtGui.QLineEdit(self.tab_device)
        self.imbus_addr.setGeometry(QtCore.QRect(280, 30, 121, 21))
        self.imbus_addr.setObjectName("imbus_addr")
        self.uv_ov_connect_testButton = QtGui.QPushButton(self.tab_device)
        self.uv_ov_connect_testButton.setGeometry(QtCore.QRect(470, 70, 75, 31))
        self.uv_ov_connect_testButton.setObjectName("uv_ov_connect_testButton")
        self.label_21 = QtGui.QLabel(self.tab_device)
        self.label_21.setGeometry(QtCore.QRect(220, 30, 46, 13))
        self.label_21.setObjectName("label_21")
        self.uv_ov_samp_res = QtGui.QLineEdit(self.tab_device)
        self.uv_ov_samp_res.setGeometry(QtCore.QRect(300, 90, 51, 20))
        self.uv_ov_samp_res.setObjectName("uv_ov_samp_res")
        self.label_8 = QtGui.QLabel(self.tab_device)
        self.label_8.setGeometry(QtCore.QRect(290, 60, 91, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtGui.QLabel(self.tab_device)
        self.label_9.setGeometry(QtCore.QRect(360, 90, 31, 21))
        self.label_9.setObjectName("label_9")
        self.down_tabWidget.addTab(self.tab_device, "")
        self.tab_uv_ov = QtGui.QWidget()
        self.tab_uv_ov.setObjectName("tab_uv_ov")
        self.uv_ov_begin = QtGui.QLineEdit(self.tab_uv_ov)
        self.uv_ov_begin.setGeometry(QtCore.QRect(220, 50, 41, 21))
        self.uv_ov_begin.setObjectName("uv_ov_begin")
        self.label_5 = QtGui.QLabel(self.tab_uv_ov)
        self.label_5.setGeometry(QtCore.QRect(220, 20, 46, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtGui.QLabel(self.tab_uv_ov)
        self.label_6.setGeometry(QtCore.QRect(280, 20, 41, 16))
        self.label_6.setObjectName("label_6")
        self.uv_ov_end = QtGui.QLineEdit(self.tab_uv_ov)
        self.uv_ov_end.setGeometry(QtCore.QRect(280, 50, 41, 21))
        self.uv_ov_end.setObjectName("uv_ov_end")
        self.uv_ov_step = QtGui.QLineEdit(self.tab_uv_ov)
        self.uv_ov_step.setGeometry(QtCore.QRect(340, 50, 41, 21))
        self.uv_ov_step.setObjectName("uv_ov_step")
        self.label_7 = QtGui.QLabel(self.tab_uv_ov)
        self.label_7.setGeometry(QtCore.QRect(350, 20, 31, 16))
        self.label_7.setObjectName("label_7")
        self.uv_ov_startButton = QtGui.QPushButton(self.tab_uv_ov)
        self.uv_ov_startButton.setGeometry(QtCore.QRect(210, 120, 75, 31))
        self.uv_ov_startButton.setStyleSheet("background-color: rgb(189, 255, 160);")
        self.uv_ov_startButton.setObjectName("uv_ov_startButton")
        self.uv_ov_stopButton = QtGui.QPushButton(self.tab_uv_ov)
        self.uv_ov_stopButton.setGeometry(QtCore.QRect(330, 120, 75, 31))
        self.uv_ov_stopButton.setStyleSheet("")
        self.uv_ov_stopButton.setObjectName("uv_ov_stopButton")
        self.label = QtGui.QLabel(self.tab_uv_ov)
        self.label.setGeometry(QtCore.QRect(400, 50, 31, 16))
        self.label.setObjectName("label")
        self.line = QtGui.QFrame(self.tab_uv_ov)
        self.line.setGeometry(QtCore.QRect(170, 30, 20, 121))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtGui.QFrame(self.tab_uv_ov)
        self.line_2.setGeometry(QtCore.QRect(480, 30, 20, 121))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.uv_ov_information = QtGui.QLabel(self.tab_uv_ov)
        self.uv_ov_information.setGeometry(QtCore.QRect(570, 80, 171, 16))
        self.uv_ov_information.setObjectName("uv_ov_information")
        self.uv_ov_interval = QtGui.QLineEdit(self.tab_uv_ov)
        self.uv_ov_interval.setGeometry(QtCore.QRect(340, 90, 41, 20))
        self.uv_ov_interval.setObjectName("uv_ov_interval")
        self.label_10 = QtGui.QLabel(self.tab_uv_ov)
        self.label_10.setGeometry(QtCore.QRect(220, 90, 101, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(self.tab_uv_ov)
        self.label_11.setGeometry(QtCore.QRect(400, 90, 21, 21))
        self.label_11.setObjectName("label_11")
        self.down_tabWidget.addTab(self.tab_uv_ov, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.rpm_start_button = QtGui.QPushButton(self.tab_2)
        self.rpm_start_button.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.rpm_start_button.setObjectName("rpm_start_button")
        self.rpm_stop_button = QtGui.QPushButton(self.tab_2)
        self.rpm_stop_button.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.rpm_stop_button.setObjectName("rpm_stop_button")
        self.down_tabWidget.addTab(self.tab_2, "")
        self.tab_rpm = QtGui.QWidget()
        self.tab_rpm.setObjectName("tab_rpm")
        self.power_start_button = QtGui.QPushButton(self.tab_rpm)
        self.power_start_button.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.power_start_button.setObjectName("power_start_button")
        self.power_stop_button = QtGui.QPushButton(self.tab_rpm)
        self.power_stop_button.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.power_stop_button.setObjectName("power_stop_button")
        self.down_tabWidget.addTab(self.tab_rpm, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.temp_start_button = QtGui.QPushButton(self.tab)
        self.temp_start_button.setGeometry(QtCore.QRect(120, 50, 75, 23))
        self.temp_start_button.setObjectName("temp_start_button")
        self.temp_stop_button = QtGui.QPushButton(self.tab)
        self.temp_stop_button.setGeometry(QtCore.QRect(240, 50, 75, 23))
        self.temp_stop_button.setObjectName("temp_stop_button")
        self.down_tabWidget.addTab(self.tab, "")
        self.tab_fantray = QtGui.QWidget()
        self.tab_fantray.setObjectName("tab_fantray")
        self.lcdNumber = QtGui.QLCDNumber(self.tab_fantray)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 40, 64, 23))
        self.lcdNumber.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtGui.QLCDNumber(self.tab_fantray)
        self.lcdNumber_2.setGeometry(QtCore.QRect(110, 40, 64, 23))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_14 = QtGui.QLabel(self.tab_fantray)
        self.label_14.setGeometry(QtCore.QRect(40, 20, 46, 13))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtGui.QLabel(self.tab_fantray)
        self.label_15.setGeometry(QtCore.QRect(120, 20, 46, 13))
        self.label_15.setObjectName("label_15")
        self.refresh_Button = QtGui.QPushButton(self.tab_fantray)
        self.refresh_Button.setGeometry(QtCore.QRect(310, 60, 75, 23))
        self.refresh_Button.setObjectName("refresh_Button")
        self.rpmlcd_0 = QtGui.QLCDNumber(self.tab_fantray)
        self.rpmlcd_0.setGeometry(QtCore.QRect(30, 140, 64, 23))
        self.rpmlcd_0.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.rpmlcd_0.setObjectName("rpmlcd_0")
        self.rpmlcd_1 = QtGui.QLCDNumber(self.tab_fantray)
        self.rpmlcd_1.setGeometry(QtCore.QRect(110, 140, 64, 23))
        self.rpmlcd_1.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.rpmlcd_1.setObjectName("rpmlcd_1")
        self.rpmlcd_2 = QtGui.QLCDNumber(self.tab_fantray)
        self.rpmlcd_2.setGeometry(QtCore.QRect(190, 140, 64, 23))
        self.rpmlcd_2.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.rpmlcd_2.setObjectName("rpmlcd_2")
        self.rpmlcd_3 = QtGui.QLCDNumber(self.tab_fantray)
        self.rpmlcd_3.setGeometry(QtCore.QRect(270, 140, 64, 23))
        self.rpmlcd_3.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.rpmlcd_3.setObjectName("rpmlcd_3")
        self.curent0 = QtGui.QLCDNumber(self.tab_fantray)
        self.curent0.setGeometry(QtCore.QRect(30, 90, 64, 23))
        self.curent0.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.curent0.setObjectName("curent0")
        self.curent1 = QtGui.QLCDNumber(self.tab_fantray)
        self.curent1.setGeometry(QtCore.QRect(110, 90, 64, 23))
        self.curent1.setStyleSheet("background-color: rgb(85, 0, 255);")
        self.curent1.setObjectName("curent1")
        self.label_16 = QtGui.QLabel(self.tab_fantray)
        self.label_16.setGeometry(QtCore.QRect(40, 70, 46, 13))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtGui.QLabel(self.tab_fantray)
        self.label_17.setGeometry(QtCore.QRect(120, 70, 46, 13))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtGui.QLabel(self.tab_fantray)
        self.label_18.setGeometry(QtCore.QRect(40, 120, 46, 13))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtGui.QLabel(self.tab_fantray)
        self.label_19.setGeometry(QtCore.QRect(130, 120, 46, 13))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtGui.QLabel(self.tab_fantray)
        self.label_20.setGeometry(QtCore.QRect(210, 120, 46, 13))
        self.label_20.setObjectName("label_20")
        self.label_22 = QtGui.QLabel(self.tab_fantray)
        self.label_22.setGeometry(QtCore.QRect(290, 120, 46, 13))
        self.label_22.setObjectName("label_22")
        self.readall_Button = QtGui.QPushButton(self.tab_fantray)
        self.readall_Button.setGeometry(QtCore.QRect(440, 60, 75, 23))
        self.readall_Button.setObjectName("readall_Button")
        self.rpm_lineEdit = QtGui.QLineEdit(self.tab_fantray)
        self.rpm_lineEdit.setGeometry(QtCore.QRect(360, 140, 61, 20))
        self.rpm_lineEdit.setObjectName("rpm_lineEdit")
        self.set_rpm_pushButton = QtGui.QPushButton(self.tab_fantray)
        self.set_rpm_pushButton.setGeometry(QtCore.QRect(440, 140, 75, 23))
        self.set_rpm_pushButton.setObjectName("set_rpm_pushButton")
        self.down_tabWidget.addTab(self.tab_fantray, "")
        self.gridLayout.addWidget(self.down_tabWidget, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(-1)
        self.down_tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Workbench", None, QtGui.QApplication.UnicodeUTF8))
        self.pow_addr.setText(QtGui.QApplication.translate("MainWindow", "GPIB0::27::INSTR", None, QtGui.QApplication.UnicodeUTF8))
        self.vol_addr.setText(QtGui.QApplication.translate("MainWindow", "GPIB0::18::INSTR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Power", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.cur_addr.setText(QtGui.QApplication.translate("MainWindow", "GPIB0::19::INSTR", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Current", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "GPIB ADDR", None, QtGui.QApplication.UnicodeUTF8))
        self.imbus_addr.setText(QtGui.QApplication.translate("MainWindow", "10.220.52.42:10013", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_connect_testButton.setText(QtGui.QApplication.translate("MainWindow", "Connect test", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Imbus", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_samp_res.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Sampling Resistor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "m Ω", None, QtGui.QApplication.UnicodeUTF8))
        self.down_tabWidget.setTabText(self.down_tabWidget.indexOf(self.tab_device), QtGui.QApplication.translate("MainWindow", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_begin.setText(QtGui.QApplication.translate("MainWindow", "40", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", " Begin", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "   End", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_end.setText(QtGui.QApplication.translate("MainWindow", "50", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_step.setText(QtGui.QApplication.translate("MainWindow", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", " Step", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_startButton.setText(QtGui.QApplication.translate("MainWindow", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_stopButton.setText(QtGui.QApplication.translate("MainWindow", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_information.setText(QtGui.QApplication.translate("MainWindow", "UV OV", None, QtGui.QApplication.UnicodeUTF8))
        self.uv_ov_interval.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Sampling  Interval", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.down_tabWidget.setTabText(self.down_tabWidget.indexOf(self.tab_uv_ov), QtGui.QApplication.translate("MainWindow", "UV OV", None, QtGui.QApplication.UnicodeUTF8))
        self.rpm_start_button.setText(QtGui.QApplication.translate("MainWindow", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.rpm_stop_button.setText(QtGui.QApplication.translate("MainWindow", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.down_tabWidget.setTabText(self.down_tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "RPM vs RPM%", None, QtGui.QApplication.UnicodeUTF8))
        self.power_start_button.setText(QtGui.QApplication.translate("MainWindow", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.power_stop_button.setText(QtGui.QApplication.translate("MainWindow", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.down_tabWidget.setTabText(self.down_tabWidget.indexOf(self.tab_rpm), QtGui.QApplication.translate("MainWindow", "Power vs RPM%", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_start_button.setText(QtGui.QApplication.translate("MainWindow", "start", None, QtGui.QApplication.UnicodeUTF8))
        self.temp_stop_button.setText(QtGui.QApplication.translate("MainWindow", "stop", None, QtGui.QApplication.UnicodeUTF8))
        self.down_tabWidget.setTabText(self.down_tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Temp vs RPM%", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "VoltageA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "VoltageB", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh_Button.setText(QtGui.QApplication.translate("MainWindow", "refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "CurentA", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "CurentB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "RPM0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "RPM1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "RPM2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "RPM3", None, QtGui.QApplication.UnicodeUTF8))
        self.readall_Button.setText(QtGui.QApplication.translate("MainWindow", "Read all", None, QtGui.QApplication.UnicodeUTF8))
        self.rpm_lineEdit.setText(QtGui.QApplication.translate("MainWindow", "20", None, QtGui.QApplication.UnicodeUTF8))
        self.set_rpm_pushButton.setText(QtGui.QApplication.translate("MainWindow", "SET RPM%", None, QtGui.QApplication.UnicodeUTF8))
        self.down_tabWidget.setTabText(self.down_tabWidget.indexOf(self.tab_fantray), QtGui.QApplication.translate("MainWindow", "FanTray", None, QtGui.QApplication.UnicodeUTF8))

import tooltips_rc
