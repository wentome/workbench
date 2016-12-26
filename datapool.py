from PySide import QtCore
class datapoolclass(QtCore.QObject):
    sig_datapool_update = QtCore.Signal(str)
    #{'color':QtCore.Qt.red, 'unit':'A/V'}
    pool = {}
    def append_menber(self, menber, value):
        self.pool[menber] = value

    def pop_menber(self, menber):
        self.pool.pop(menber)

    def append_value(self, menber, value):
        self.pool[menber].append(value)

    def pop_value(self, menber):
        if len(self.pool[menber]) > 1:
            self.pool[menber].pop()
        else:
            print "data%d just one member" % menber
    def copy_pool(self,pool={}):
        self.pool.update(pool)

    def clear_pool(self):
        self.pool.clear()

    def update(self):
        self.sig_datapool_update.emit('')






