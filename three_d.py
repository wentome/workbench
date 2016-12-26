#!/usr/bin/env python

"""PySide port of the opengl/hellogl example from Qt v4.x"""

import sys
import math
from PySide import QtCore, QtGui, QtOpenGL

try:
    from OpenGL import GL
except ImportError:
    app = QtGui.QApplication(sys.argv)
    QtGui.QMessageBox.critical(None, "OpenGL hellogl",
                               "PyOpenGL must be installed to run this example.",
                               QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                               QtGui.QMessageBox.NoButton)
    sys.exit(1)


class three_d_class(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.glWidget = GLWidget()

        self.xSlider = self.createSlider(QtCore.SIGNAL("xRotationChanged(int)"),
                                         self.glWidget.setXRotation)
        self.ySlider = self.createSlider(QtCore.SIGNAL("yRotationChanged(int)"),
                                         self.glWidget.setYRotation)
        self.zSlider = self.createSlider(QtCore.SIGNAL("zRotationChanged(int)"),
                                         self.glWidget.setZRotation)
        self.button = QtGui.QPushButton("change")
        self.button.clicked.connect(self.change)
        mainLayout = QtGui.QHBoxLayout()
        mainLayout.addWidget(self.glWidget)
        mainLayout.addWidget(self.xSlider)
        mainLayout.addWidget(self.ySlider)
        mainLayout.addWidget(self.zSlider)
        mainLayout.addWidget(self.button)
        self.setLayout(mainLayout)

        self.xSlider.setValue(0 * 16)
        self.ySlider.setValue(0 * 16)
        self.zSlider.setValue(0 * 16)

        self.setWindowTitle(self.tr("Hello GL"))

    def change(self):
        # print "change"
        self.glWidget.change()

    def createSlider(self, changedSignal, setterSlot):
        slider = QtGui.QSlider(QtCore.Qt.Vertical)

        slider.setRange(0, 360 * 16)
        slider.setSingleStep(16)
        slider.setPageStep(15 * 16)
        slider.setTickInterval(15 * 16)
        slider.setTickPosition(QtGui.QSlider.TicksRight)

        self.glWidget.connect(slider, QtCore.SIGNAL("valueChanged(int)"), setterSlot)
        self.connect(self.glWidget, changedSignal, slider, QtCore.SLOT("setValue(int)"))

        return slider


class GLWidget(QtOpenGL.QGLWidget):
    def __init__(self, parent=None):
        QtOpenGL.QGLWidget.__init__(self, parent)

        self.object = 0
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.flag = False
        self.offset = 0

        self.lastPos = QtCore.QPoint()

        self.trolltechGreen = QtGui.QColor.fromCmykF(0.40, 0.0, 1.0, 0.0)
        self.trolltechPurple = QtGui.QColor.fromCmykF(0.39, 0.39, 0.0, 0.0)

    def change(self):
        # print "change"
        if self.flag == True:
            self.flag = False
            self.offset = 0.2

        else:
            self.flag = True
            self.offset = -0.2

        self.updateGL()

    def xRotation(self):
        return self.xRot

    def yRotation(self):
        return self.yRot

    def zRotation(self):
        return self.zRot

    def minimumSizeHint(self):
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        return QtCore.QSize(400, 400)

    def setXRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.xRot:
            self.xRot = angle
            self.emit(QtCore.SIGNAL("xRotationChanged(int)"), angle)
            self.updateGL()

    def setYRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.emit(QtCore.SIGNAL("yRotationChanged(int)"), angle)
            self.updateGL()

    def setZRotation(self, angle):
        angle = self.normalizeAngle(angle)
        if angle != self.zRot:
            self.zRot = angle
            self.emit(QtCore.SIGNAL("zRotationChanged(int)"), angle)
            self.updateGL()

    def initializeGL(self):
        self.qglClearColor(self.trolltechPurple.darker())
        self.object = self.makeObject()
        GL.glShadeModel(GL.GL_FLAT)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_CULL_FACE)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        GL.glLoadIdentity()
        GL.glTranslated(0.0, 0.0, -10.0)
        GL.glRotated(self.xRot / 16.0, 1.0, 0.0, 0.0)
        GL.glRotated(self.yRot / 16.0, 0.0, 1.0, 0.0)
        GL.glRotated(self.zRot / 16.0, 0.0, 0.0, 1.0)

        GL.glCallList(self.makeObject())

    def resizeGL(self, width, height):
        side = min(width, height)
        GL.glViewport(int((width - side) / 2), int((height - side) / 2), side, side)

        GL.glMatrixMode(GL.GL_PROJECTION)
        GL.glLoadIdentity()
        GL.glOrtho(-0.5, +0.5, -0.5, +0.5, 4.0, 15.0)
        GL.glMatrixMode(GL.GL_MODELVIEW)

    def mousePressEvent(self, event):
        self.lastPos = QtCore.QPoint(event.pos())

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()

        if event.buttons() & QtCore.Qt.LeftButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setYRotation(self.yRot + 8 * dx)
        elif event.buttons() & QtCore.Qt.RightButton:
            self.setXRotation(self.xRot + 8 * dy)
            self.setZRotation(self.zRot + 8 * dx)

        self.lastPos = QtCore.QPoint(event.pos())

    def makeObject(self):
        genList = GL.glGenLists(1)
        GL.glNewList(genList, GL.GL_COMPILE)

        GL.glBegin(GL.GL_QUADS)

        L = 0.5
        W = 0.3
        H = 0.05

        self.box(-L / 2, 0, -W / 2, L, W, H)
        self.box(-L / 2, 0.06, -W / 2, L, W, H)
        # if self.flag==True:
        self.box(-L / 2, 0.12, -W / 2, L, W, H)

        self.box(-L / 2, 0.18, -W / 2 + self.offset, L, W, H)
        self.box(-L / 2, 0.24, -W / 2, L, W, H)

        GL.glEnd()
        GL.glEndList()

        return genList

    def box(self, X=0, Y=0, Z=0, L=0.1, W=0.1, H=0.1):

        #######################front back#############################
        self.qglColor(QtCore.Qt.magenta)

        GL.glVertex3d(X, Y, Z + W)  # front l
        GL.glVertex3d(X + L, Y, Z + W)
        GL.glVertex3d(X + L, Y + H, Z + W)
        GL.glVertex3d(X, Y + H, Z + W)

        GL.glVertex3d(X, Y, Z)  # back
        GL.glVertex3d(X, Y + H, Z)
        GL.glVertex3d(X + L, Y + H, Z)
        GL.glVertex3d(X + L, Y, Z)

        ################################################################
        self.qglColor(QtCore.Qt.green)

        GL.glVertex3d(X, Y + H, Z)
        GL.glVertex3d(X, Y + H, Z + W)
        GL.glVertex3d(X + L, Y + H, Z + W)
        GL.glVertex3d(X + L, Y + H, Z)

        GL.glVertex3d(X, Y, Z)
        GL.glVertex3d(X + L, Y, Z)
        GL.glVertex3d(X + L, Y, Z + W)
        GL.glVertex3d(X, Y, Z + W)

        #################### lift right###############################
        self.qglColor(QtCore.Qt.blue)

        GL.glVertex3d(X, Y, Z)
        GL.glVertex3d(X, Y, Z + W)
        GL.glVertex3d(X, Y + H, Z + W)
        GL.glVertex3d(X, Y + H, Z)

        GL.glVertex3d(X + L, Y, Z)
        GL.glVertex3d(X + L, Y + H, Z)
        GL.glVertex3d(X + L, Y + H, Z + W)
        GL.glVertex3d(X + L, Y, Z + W)

    def normalizeAngle(self, angle):
        while angle < 0:
            angle += 360 * 16
        while angle > 360 * 16:
            angle -= 360 * 16
        return angle


# if __name__ == '__main__':
#     app = QtGui.QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
