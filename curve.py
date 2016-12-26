#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## 1 100000 1s    1000000 10S(can't work normal)
## 5 100000 3.8s
## performance  100000 point
## this file is genneral draw coordinate
## Author :CP
## Date   :2016.10
##
##
##
##
##
#############################################################################
#
#  ******** ===================================== max
#           -------------------------------------
#   grid    -------------------------------------
#           -------------------------------------
#           -------------------------------------
#  ******** =====================================
#           -------------------------------------
#  div *****-------------------------------------
#      *****-------------------------------------
#           -------------------------------------
#           ===================================== min
#
##########################################################################

from PySide import QtCore,QtGui
import math
from datapool import datapoolclass
import  time


class curve_class(QtGui.QWidget):
    def __init__(self,parent=None):
        super(curve_class,self).__init__(parent)
        self.data=datapoolclass()

        self.star_column_space = 45  # this 4 space value( pixel) adjust the coordinate outline space
        self.end_column_space = 50
        self.star_row_space = 25
        self.end_row_space = 25

        self.x_div=1
        self.y_div=1
        self.x_min_data = 0
        self.x_max_data = 1
        self.y_min_data = 0
        self.y_max_data = 1

        self.x_grid_range = [4, 9] # every grid have 5 div
        self.y_grid_range = [4, 9]

        self.y_begin = 0
        self.y_end = self.y_grid_range[0]
        self.x_begin = 0
        self.x_end = self.x_grid_range[0]
        self.x_grid = self.x_grid_range[0]
        self.y_grid = self.y_grid_range[0]
        self.update_flag=False
        self.state=2
        self.curves = []
        self.x_unit ='X'
        self.y_L_unit = 'Y'
        self.y_R_unit = 'R'
        self.y_R_flag=0
        self.point_x = 0
        self.point_y = 0
        self.sign=[]
        self.doubleclick_flag = False
        self.time_test=0
    def clear_sign(self):
        self.sign=[]


    def curve_update(self):
        self.update_flag = True
        self.update()
    def save_pic(self,filename):
        pixmap = QtGui.QPixmap.grabWidget(self)
        pixmap.save(filename)

    def mouseDoubleClickEvent(self, event):
        self.point_x = event.x()
        self.point_y = event.y()
        self.doubleclick_flag = True
        self.update()

    def paintEvent(self,event):
        #begin_time=time.clock()
        total_column_num = self.width()
        total_raw_num = self.height()
        star_column=self.star_column_space
        end_column=total_column_num -self.end_column_space
        star_row=self.star_row_space
        end_row=total_raw_num-self.end_row_space

        self.real_column = total_column_num - self.star_column_space - self.end_column_space
        self.real_raw = total_raw_num-self.star_row_space -self.end_row_space


        painter=QtGui.QPainter(self)

########################### Draw blue outer border #########################################
        if self.doubleclick_flag:
            x_per_pix =float(self.x_end - self.x_begin)/self.real_column
            y_per_pix =float(self.y_end - self.y_begin)/self.real_raw
            min_dx_pix=5
            temp=-1
            x_value = float(self.point_x - star_column) / self.real_column * (self.x_end - self.x_begin) + self.x_begin
            y_value = float((self.real_raw - self.point_y + self.end_row_space)) / self.real_raw * (self.y_end - self.y_begin) + self.y_begin
            for curve in self.curves:
                for i in range(len(self.data.pool[curve])):
                    dx_pix = math.fabs(  (x_value-self.data.pool[curve][i][0])/x_per_pix )
                    if dx_pix<min_dx_pix:
                        min_dx_pix = dx_pix
                        temp = i
                if temp != -1:
                    dy_pix=math.fabs( (y_value-self.data.pool[curve][temp][1])/y_per_pix)

                    if dy_pix<5:
                        self.sign.append([self.data.pool[curve][temp][0],self.data.pool[curve][temp][1]])
                        break
            self.doubleclick_flag = False



        # painter.save()
        # pen = QtGui.QPen(QtCore.Qt.blue, 2)
        # painter.setPen(pen)
        # painter.drawRect(1, 1, self.width()-2 , self.height()-2 )
        # painter.restore()
#####################################################################

        painter.save()
        painter.translate(0,total_raw_num)
        painter.scale(1,-1)

################################################ draw coordinate #############################################################



######################################################### X #####################################################################
        painter.save()
        pen=QtGui.QPen(QtCore.Qt.gray, 1)
        painter.setPen(pen)

        if self.update_flag == True:
            self.update_flag = False
            try:
                string=self.data.pool['unit']
                if string.count('/')==1:
                    res=string.split('/',1)
                    self.x_unit=res[0]
                    self.y_L_unit=res[1]
                else:
                    res = string.split('/', 2)
                    self.x_unit = res[0]
                    self.y_L_unit = res[1]
                    self.y_R_unit=res[2]
            except:
                self.x_unit = 'X'
                self.y_L_unit = 'Y'
                self.y_R_unit = 'R'


############################### get members #######################

            keys = self.data.pool.keys()
            self.curves=[]# clear self.curves
            for key in keys:
                if key != 'unit':
                    self.curves.append(key)
##################################################

            if self.state!=0:
                self.state = 1

                self.x_min_data =self.data.pool[self.curves[0]][0][0] # first curve's first point's 'x'
                self.x_max_data =self.x_min_data
                self.y_min_data = self.data.pool[self.curves[0]][0][1]# first curve's first point's 'x'
                self.y_max_data = self.y_min_data

                for curve in self.curves:
                    for j in self.data.pool[curve]:
                        if j[0]<self.x_min_data:
                            self.x_min_data = j[0]
                        if j[0]>self.x_max_data:
                            self.x_max_data = j[0]
                        if j[1] < self.y_min_data:
                                self.y_min_data = j[1]
                        if j[1] > self.y_max_data:
                                self.y_max_data = j[1]
            else:
                for i in self.data.pool:
                    #print 'state =0'
                    if self.data.pool[i][len(self.data.pool[i])-1][0]<self.x_min_data:
                        self.x_min_data = self.data.pool[i][len(self.data.pool[i])-1][0]
                    if self.data.pool[i][len(self.data.pool[i]) - 1][0] > self.x_max_data:
                        self.x_max_data = self.data.pool[i][len(self.data.pool[i]) - 1][0]
                    if self.data.pool[i][len(self.data.pool[i]) - 1][1] < self.y_min_data:
                        self.y_min_data = self.data.pool[i][len(self.data.pool[i])-1][0]
                    if self.data.pool[i][len(self.data.pool[i]) - 1][1] > self.y_max_data:
                        self.y_max_data = self.data.pool[i][len(self.data.pool[i]) - 1][0]



            #print  self.x_min_data , self.x_max_data,self.y_min_data, self.y_max_data

            x_dif=self.x_max_data-self.x_min_data
            if x_dif==0:
                x_dif=5

            y_dif = self.y_max_data - self.y_min_data
            if y_dif==0:
                y_dif=5
            x_grid_div = self.get_grid(self.x_grid_range, x_dif)
            self.x_div = x_grid_div[1]
            self.x_end = (self.x_max_data - (self.x_max_data % self.x_div)) + self.x_div
            self.x_begin = (self.x_min_data - (self.x_min_data % self.x_div))

            x_grid_div = self.get_grid(self.x_grid_range, self.x_end - self.x_begin)
            self.x_grid = x_grid_div[0]
            self.x_div = x_grid_div[1]
            if self.x_div >= 1:
                self.x_begin = int(self.x_begin)

            y_grid_div = self.get_grid(self.y_grid_range, y_dif)
            self.y_div = y_grid_div[1]
            self.y_end = (self.y_max_data - (self.y_max_data % self.y_div)) + self.y_div
            self.y_begin = (self.y_min_data - (self.y_min_data % self.y_div))

            y_grid_div = self.get_grid(self.y_grid_range, self.y_end-self.y_begin)
            self.y_grid = y_grid_div[0]
            self.y_div = y_grid_div[1]
            self.y_begin=self.y_end-self.y_grid*self.y_div
            if self.y_div>=1:
                self.y_end = int(self.y_end)

        x_scale = float(self.real_column) / self.x_grid / 5
        y_scale = float(self.real_raw) / self.y_grid/5
        for i in range(self.x_grid*5+1):
            if i%5==0:
                painter.save()
                pen=QtGui.QPen(QtCore.Qt.gray, 2) # bold cloumn line
                painter.setPen(pen)
                painter.drawLine(star_column+i*x_scale,star_row,star_column+i*x_scale,end_row)      # cloumn

                painter.save()
                painter.scale(1, -1)
                #painter.translate(0, -20)
                pen = QtGui.QPen(QtCore.Qt.black)  # bold cloumn line
                painter.setPen(pen)
                                                                # y mirror
                painter.drawText(star_column-4 + i * x_scale, -(star_row-20) , str(self.x_begin+i*self.x_div/5))
                painter.restore()

                painter.restore()
            else:
                painter.drawLine(star_column+i*x_scale,star_row,star_column+i*x_scale,end_row)      # cloumn
################################################# Y #################################################################
        for i in range(self.y_grid*5+1):
            if i%5==0:
                painter.save()

                pen=QtGui.QPen(QtCore.Qt.gray, 2) # bold row line
                painter.setPen(pen)
                painter.drawLine(star_column,star_row+i*y_scale,end_column,star_row+i*y_scale)        # row

                painter.save()
                painter.scale(1, -1)
                painter.translate(0, -total_raw_num)
                pen = QtGui.QPen(QtCore.Qt.black)  # bold cloumn line
                painter.setPen(pen)
                painter.drawText(10, self.end_row_space+5 + i * y_scale, str(round(self.y_end-i*self.y_div/5,3)))
                if self.y_R_flag==1:
                    painter.drawText(end_column+4, self.end_row_space + 5 + i * y_scale,
                                 str(round(self.y_end - i * self.y_div / 5, 3)))
                painter.restore()

                painter.restore()
            else:
                painter.drawLine(star_column,star_row+i*y_scale,end_column,star_row+i*y_scale)        # row
        painter.restore()



################################################## draw cutline  #############################################################################

        painter.save()
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        color =[QtCore.Qt.red,QtCore.Qt.green,QtCore.Qt.blue,QtCore.Qt.yellow,QtCore.Qt.cyan,QtCore.Qt.darkMagenta]
        for i in range(len(self.curves)):
            pen = QtGui.QPen(color[i],1)  # bold cloumn line
            painter.setPen(pen)
            for j in range(len(self.data.pool[self.curves[i]])-1):
                self.draw_line(painter, self.data.pool[self.curves[i]][j][0], self.data.pool[self.curves[i]][j][1], self.data.pool[self.curves[i]][j+1][0], self.data.pool[self.curves[i]][j+1][1] )
        painter.restore()

################################################## draw unit #############################################################################
        painter.save()
        painter.scale(1,-1)


        painter.drawText(total_column_num-20, -(star_row-20),self.x_unit)     #X
        painter.drawText(13,-(total_raw_num-15),self.y_L_unit)  #Y
        if self.y_R_flag == 1:
            painter.drawText(end_column+4, -(total_raw_num - 15), self.y_R_unit)  # Y


        painter.save()


        for i in range(len(self.curves)) :
            painter.drawText(end_column + 5, -(end_row - 30 * (i + 1)) - 5, self.curves[i])

            painter.save()
            pen = QtGui.QPen(color[i],2)  # bold row line
            painter.setPen(pen)
            painter.drawLine(end_column+10, -(end_row-30*(i+1)), end_column+40, -(end_row-30*(i+1)))
            painter.restore()
        painter.restore()


        painter.restore()


        


            
################################################### draw curve #############################################################################            


############################################################################################
        painter.restore()

        for point in self.sign:
            x = float(point[0] - self.x_begin) / (self.x_end - self.x_begin) * self.real_column + self.star_column_space
            y = total_raw_num - self.star_row_space - float(point[1] - self.y_begin) / (
            self.y_end - self.y_begin) * self.real_raw
            painter.drawLine(x, y,x+5,y-15)
            painter.setBrush(QtCore.Qt.yellow)
            painter.drawRect(x+5, y - 30, len(str(point[0]) + ' , ' + str(point[1]))*7, 15)
            painter.drawText(x+10, y - 18, str(point[0]) + ' , ' + str(point[1]))  # Y

        #print time.clock()-begin_time
    def draw_line(self,painter,x1,y1,x2,y2,):
        #print x1 ,y1,self.y_begin,self.y_end
        x_1 = float(x1-self.x_begin) / (self.x_grid * self.x_div) * self.real_column +self.star_column_space
        x_2 = float(x2-self.x_begin) / (self.x_grid * self.x_div) * self.real_column +self.star_column_space
        y_1=float(y1 - self.y_begin)/(self.y_grid * self.y_div)*self.real_raw +self.star_row_space
        y_2 = float(y2 - self.y_begin) / (self.y_grid * self.y_div) * self.real_raw + self.star_row_space
        painter.drawLine(x_1,y_1,x_2,y_2)

    def get_valid_num(self,data):
        temp = [0, 0]
        if math.floor(data) > 0:
            temp[0] = 1
            temp[1] = math.trunc(data)  # 3.67 ----3.0
        else:
            if data * 10 >= 1:
                temp[0] = 0.1
                temp1 = str(data)
                temp[1] = float(temp1[0:3])
            elif data * 100 >= 1:
                temp[0] = 0.01
                temp1 = str(data)
                temp[1] = float(temp1[0:4])
            elif data * 1000 >= 1:
                temp[0] = 0.001
                temp1 = str(data)
                temp[1] = float(temp1[0:5])
        return temp

    def get_valid_data(self,data,precision):
        return data - math.fmod(data,precision)

    def get_grid(self,grid_range=[4,7],dif=5):
        if dif == 0:
            return
        i = 0
        div = self.change_div(i)
        grid = grid_range[0]

        while 1:
            if grid * div < dif:
                if grid < grid_range[1]:
                    grid += 1
                else:
                    grid = grid_range[0]
                    i += 1
                    div = self.change_div(i)
                if grid * div >= dif:
                    break
            else:
                grid = grid_range[0]
                i -= 1
                div = self.change_div(i)
        return [grid, div]


###############################################################################################
# i:     |-6     |  -5  | -4   |  -3  | -2   |  -1  |  0  | 1   | 2  |  3  |  4  |  5  |  6   |
# return | 0.01  | 0.02 | 0.05 |  0.1 | 0.2  |  0.5 |  1  | 2   | 5  |  10 |  20 |  50 |  100 |
###############################################################################################
    def change_div(self,i):
        if i >= 0:
            return int((math.pow(i % 3, 2) + 1) * math.pow(10, i / 3))
        else:
            return (math.pow(i % 3, 2) + 1) * math.pow(10, i / 3)

########################################################################









       

