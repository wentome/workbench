
#visa_addr="TCPIP0::10.220.52.102::2268::SOCKET"
#visa_addr="TCPIP0::10.220.43.26::8080::SOCKET"


#visa_addr='GPIB1::19::INSTR'



def get_mul_vol(dev):
    return dev.query("MEASure:VOLTage:DC?")



