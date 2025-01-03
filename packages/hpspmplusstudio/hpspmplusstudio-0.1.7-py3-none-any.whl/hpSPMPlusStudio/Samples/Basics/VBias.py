from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()
    VBias = Device.VBIAS()

    print(VBias.Get_DCOffset())
    print(VBias.Get_ACAmplitude())
    print(VBias.Get_ACFrequency())
    print(VBias.Get_MinDCOffset())
    print(VBias.Get_MaxDCOffset())

    print(VBias.Set_DCOffset(5))
    print(VBias.Set_ACAmplitude(5))
    print(VBias.Set_ACFrequency(30000))
    
    
    


 
    

