
def power_on(dev):
    dev.write("OUTP ON")
def power_off(dev):
    dev.write("OUTP OFF")

def power_read_vol(dev):
    return dev.query("VOLT?")

def power_set_vol(dev,value):
    dev.write("VOLT " + str(value) )

def power_set_cur(dev,value):
    dev.write("CURR " + str(value) )