from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    Status = Device.STATUS()
    PhotoDiode = Device.PHOTODIODE()

    print(PhotoDiode.Get_Commands())
    print(PhotoDiode.Get_FL())
    print(PhotoDiode.Get_FN())
    print(PhotoDiode.Get_FN10())
    print(PhotoDiode.Get_FT())
    print(PhotoDiode.Get_LaserPower())
    print(PhotoDiode.Get_LaserRF_Frequency())
    print(PhotoDiode.Set_LaserPower(20.5))
    print(PhotoDiode.Set_LaserRF_Frequency(21.5))

    time.sleep(5)
    print(PhotoDiode.Null10FN())
    time.sleep(5)
    print(PhotoDiode.NullFL())
    time.sleep(5)
    print(PhotoDiode.PhotoDiodeReset())
    


 
    

