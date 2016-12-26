import visa

def init_gpib():
    return  visa.ResourceManager() #retuen visa
def remove_gpib(visa):
    visa.close()
def open_dev(visa,visa_addr):
    return visa.open_resource(visa_addr ,open_timeout=3,) #retuen dev
def close_dev(dev):
    dev.close()
def get_info(dev):
    return dev.query("*IDN?",3)