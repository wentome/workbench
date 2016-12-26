#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http://www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http://www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
#############################################################################


from PySide import  QtGui
import sys
import logging
import time
import traceback


from manager import manager_class


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        try:
            self.M=manager_class()
            self.M.put_ui(self)
            self.M.put_curve()
            self.M.put_2D()
            #self.M.put_3D()
            self.M.put_textbrowser()
            self.M.sig_slot()
        except:
            info = traceback.format_exc()
            logging.info(info)

        
 
#if __name__ == "__main__":
logging.basicConfig(level=logging.INFO,filename='sys.log')
logging.info(time.ctime())
app = QtGui.QApplication(sys.argv)
M = MainWindow()
M.show()
sys.exit(app.exec_())
