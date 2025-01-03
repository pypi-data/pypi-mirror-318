from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()
    HallCard = Device.HALLCARD()

    print(HallCard.Get_IsHallProbeEnabled())
    print(HallCard.Get_IsInfraRedLedOn())
    print(HallCard.Get_IHallRange())
    print(HallCard.Get_IHall())
    print(HallCard.Get_IHallOffset())
    print(HallCard.Get_RHall())
    print(HallCard.Get_VHall())
    print(HallCard.Get_BHall())
    print(HallCard.Get_HallAmplitudeGain())
    print(HallCard.Get_HallAmplitudeBandwith())
    print(HallCard.Get_CoilVoltage())
    print(HallCard.Get_CoilVoltageRate())

    print(HallCard.Set_IHall(2))
    print(HallCard.Set_IHallOffset(3))
    print(HallCard.Set_RHall(3))
    print(HallCard.Set_IHallOffset(3))

    print(HallCard.Set_EnableHallProbe())
    print(HallCard.Set_EnableIRLed())

    print(HallCard.Set_HallAmplitudeGain(100))
    print(HallCard.Set_HallAmplitudeBandwidth(1))

    print(HallCard.Set_CoilVoltage(3))
    print(HallCard.Set_CoilVoltageRate(0.6))

    print(HallCard.NullHallOffset())
 

    print(HallCard.Get_IsHallProbeEnabled())
    print(HallCard.Get_IsInfraRedLedOn())
    print(HallCard.Get_IHallRange())
    print(HallCard.Get_IHall())
    print(HallCard.Get_IHallOffset())
    print(HallCard.Get_RHall())
    print(HallCard.Get_VHall())
    print(HallCard.Get_BHall())
    print(HallCard.Get_HallAmplitudeGain())
    print(HallCard.Get_HallAmplitudeBandwith())
    print(HallCard.Get_CoilVoltage())
    print(HallCard.Get_CoilVoltageRate())
    
    


 
    

