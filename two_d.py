from PySide import QtCore, QtGui
import logging

class two_d_class(QtGui.QWidget):
    def __init__(self, parent=None):
        super(two_d_class, self).__init__(parent)
        logging.info('2d')

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(100)
        self.angle = 0
        self.fanspeed = [0, 0, 0, 0]
    def change_angle(self):
        if self.angle == 360:
            self.angle = 0
        self.angle += 1
    def set_fanspeed(self,flag,value):
        self.fanspeed[flag]=0
        self.fanspeed[flag]=value/1000

    def thrans(self,x,y,r):
        return QtCore.QRectF(x - r, y - r, 2 * r, 2 * r)
    def draw_diod(self,painter,x=100,y=100,r=10,flag=0):
        painter.save()
        if flag==1:
            painter.translate(x,y)
            x=0
            y=0
            painter.scale(-1,1)

        painter.drawLine(x-r,y,x,y)
        painter.drawLine(x , y-r, x, y+r)
        painter.drawLine(x , y-r, x+r, y)
        painter.drawLine(x, y + r, x + r, y)
        painter.drawLine(x+r, y - r, x+r, y + r)
        painter.drawLine(x+r, y, x + 2*r, y)
        painter.restore()






    def draw_fan(self, painter, x=100, y=100, r=50, angle=0,flag=0):
        painter.save()
        painter.translate(x, y)
        x = 0
        y = 0
        painter.drawRect(self.thrans(x, y, r+8))
        painter.drawEllipse(self.thrans(x, y, r+6))
        #painter.drawEllipse(self.thrans(x, y, r + 3))
        if flag==1:
            painter.setBrush(QtCore.Qt.red)
        else:
            painter.setBrush(QtCore.Qt.cyan)
        painter.rotate(angle)
        painter.drawChord(self.thrans(x, y-r/2, r/2), -90 * 16, 180 * 16)
        painter.drawChord(self.thrans(x, y+r/2, r/2), 90 * 16, 180 * 16)
        painter.drawChord(self.thrans(x-r/2, y, r/2), 0 * 16, 180 * 16)
        painter.drawChord(self.thrans(x+r/2, y, r/2), 180 * 16, 180 * 16)
        painter.restore()




    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        # painter.save()
        # pen = QtGui.QPen(QtCore.Qt.blue, 2)
        # painter.setPen(pen)
        # painter.drawRect(1, 1, self.width() - 2, self.height() - 2)
        # painter.restore()
        ###################### draw fans ###############################################
        painter.save()
        hotswap_x = 200
        hotswap_y = 50
        for i in range(2):
            painter.drawRect(hotswap_x, hotswap_y -10+ i * 200, 70, 70)
            painter.drawText(hotswap_x + 10, hotswap_y+30 + i * 200, 'HOTSWAP')

            painter.drawLine(hotswap_x-100, hotswap_y+20 + i * 200, hotswap_x, hotswap_y+20 + i * 200)
            painter.drawLine(hotswap_x +70, hotswap_y + 20 + i * 200, hotswap_x+270, hotswap_y + 20 + i * 200)
            self.draw_diod(painter, hotswap_x+280, hotswap_y+20 + i * 200, 10)

            painter.drawLine(hotswap_x - 100, hotswap_y + 70 + i * 200, hotswap_x + 25, hotswap_y + 70 + i * 200)
            painter.drawRect(hotswap_x + 25, hotswap_y + 65 + i * 200,20,10)
            painter.drawLine(hotswap_x +35, hotswap_y + 60 + i * 200, hotswap_x +35, hotswap_y + 65 + i * 200)
            painter.drawLine(hotswap_x +45, hotswap_y + 70 + i * 200, hotswap_x + 299, hotswap_y + 70 + i * 200)
            self.draw_diod(painter,  hotswap_x + 319, hotswap_y + 70 + i * 200, 10,1)

        for i in range(2):
            painter.drawLine(hotswap_x+300+i*29, hotswap_y-20+i*40, hotswap_x+300+i*29, hotswap_y+250+i*40)


        #self.draw_diod(painter, 100, 150, 10,1)

        self.change_angle()
        x_start=600
        y_start=50

        for i in range(4):
            self.draw_fan(painter, x_start, y_start + i * 90, 30, self.angle*5*self.fanspeed[i])
            painter.drawLine(x_start -100, y_start -20+ i * 90, x_start-39, y_start-20 + i * 90)
            painter.drawLine(x_start - 70, y_start+20 + i * 90, x_start - 39, y_start+20 + i * 90)


            painter.drawLine(x_start+39, y_start+i*90, x_start+100,y_start+i*90)
            painter.drawRect(x_start+100, y_start+i*90-10, 30, 20)
            painter.drawText(x_start+100, y_start+i*90+5, ' WDT')
        painter.restore()
        #####################################################################









