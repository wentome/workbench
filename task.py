from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger

import logging
from case import case_class
from PySide import QtCore
class task_class(QtCore.QObject):
    def __init__(self):
        logging.basicConfig()
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.runing=True
        self.case=case_class()
################################################################
        self.task_queue={'1':[self.task1,'1'],
                         '2':[self.task2,'2'],
                         '3':[self.task3,'3'],
                         '11':[self.task11, '11'],
                         #'12': [self.task12, '12'],
                         '13': [self.task13, '13'],
                         '14': [self.task14, '14'],
                         '15': [self.task15, '15'],
                         '16': [self.task16, '16'],
                         '31': [self.task31, '31']}
#################################################################

    def tasks_add(self,num,interval=3):
        if self.scheduler.get_job(self.task_queue['%d' % num][1]) == None:
            if num>10:
                self.runing = True
                self.scheduler.add_job(self.task_queue['%d'%num][0], trigger=DateTrigger(),
                                       id=self.task_queue['%d'%num][1])
            else:
                #self.scheduler.add_job(self.task_queue['%d' % num][0], 'interval', seconds=interval,
                #                       id=self.task_queue['%d' % num][1])
                self.scheduler.add_job(self.task_queue['%d' % num][0], trigger=IntervalTrigger(seconds=interval),
                                       id=self.task_queue['%d' % num][1])

    def tasks_remove(self,num):
        #self.scheduler.shutdown(wait=False)
        if self.scheduler.get_job(self.task_queue['%d'%num][1])!=None:
            self.scheduler.remove_job(self.task_queue['%d'%num][1])
        if num>10:
            self.runing = False


    def stop(self):
        self.scheduler.shutdown()
#################################################################################
    def task1(self):
        pass
    def task2(self):
        print "task2"
    def task3(self):
        print "task3"

######################################################################
    def task11(self):
        self.case.test(self)


    def task13(self):
        self.case.uv_ov(self)

    def task14(self):
        self.case.rpm_rpm_per(self)

    def task15(self):
        self.case.power_rpm_per(self)

    def task16(self):
        self.case.temp_rpm_per(self)
    def task31(self):
        self.case.test(self)
        #self.case.double_test(self)








