from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()
    Fiber = Device.FIBERCARD()

    print(Fiber.Get_IsLaserOn())
    print(Fiber.Get_IsLaserFanOn())
    print(Fiber.Get_LaserPowerSetPoint())
    print(Fiber.Get_LaserPower())
    print(Fiber.Get_IsRFModulatorOn())
    print(Fiber.Get_RFModulatorAmplitudeDigiPOT())
    print(Fiber.Get_RFModulatorFrequencyDigiPOT())
    print(Fiber.Get_SignalPhotoDiodeGain())
    print(Fiber.Get_ReferancePhotoDiodeGain())
    print(Fiber.Get_FiberPZTVoltage())
    print(Fiber.Get_QuadlockStatus())
    print(Fiber.Get_IsEnableQuadlock())
    print(Fiber.Get_IsRescanQuadlockEnable())

    print(Fiber.Set_LaserEnable())
    time.sleep(2)
    print(Fiber.Set_LaserDisable())
    time.sleep(2)
    print(Fiber.Set_LaserEnable())
    time.sleep(2)
    print(Fiber.Set_LaserFanEnable())
    time.sleep(2)
    print(Fiber.Set_LaserFanDisable())
    time.sleep(2)
    print(Fiber.Set_LaserFanEnable())
    print(Fiber.Set_LaserPowerSetPoint(41.0))
    print(Fiber.Set_SignalPhotoDiodeGain(1))
    print(Fiber.Set_ReferancePhotoDiodeGain(10))
    print(Fiber.Set_FiberPZTVoltage(30))
    print(Fiber.Set_QuadlockEnable())
    print(Fiber.Set_RescanQuadlockEnable())

    print(Fiber.NullFiber())

   


  


 
    

