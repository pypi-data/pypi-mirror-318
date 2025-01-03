from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()
    Pid  = Device.PID()

    print(Pid.Get_PidTypes())
    print(Pid.Get_PID(0))
    print(Pid.Get_PID(1))
    print(Pid.Get_PID(2))
    print(Pid.Get_PID(3))

    print(Pid.Set_Pid_PValue(0,10))
    print(Pid.Set_Pid_IValue(0,20))
    print(Pid.Set_Pid_DValue(0,30))
    print(Pid.Set_Pid_SetValue(0,40))

    print(Pid.Set_Pid_Enable(0))
    print(Pid.Set_Pid_NegativePolarity_Enable(0))
    print(Pid.Set_Pid_InvertVz_Enable(0))

    time.sleep(4)
    print(Pid.Set_Pid_Disable(0))
    print(Pid.Set_Pid_NegativePolarity_Disable(0))
    print(Pid.Set_Pid_InvertVz_Disable(0))

   







    

