import hpSPMPlusStudio as hps
from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

hps.help()


if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()
    AdjustFiber = Device.ADJUSTFIBER()

    print(AdjustFiber.Get_IsInit())
    print(AdjustFiber.Set_Initialize())
    print(AdjustFiber.Get_IsInit())

    print(AdjustFiber.Get_Commands())
    print(AdjustFiber.Get_NumSamples())
    print(AdjustFiber.Get_NumAvg())
    print(AdjustFiber.Get_Delay())
    print(AdjustFiber.Get_MiddleDelay())
    print(AdjustFiber.Get_KFiber())
    print(AdjustFiber.Get_SlopeStepSize())
    print(AdjustFiber.Get_SinPeriod())
    print(AdjustFiber.Get_SlopeModeList())
    print(AdjustFiber.Get_SlopeMode())
    print(AdjustFiber.Get_Gamma())
    print(AdjustFiber.Get_MaxPztVoltage())
    print(AdjustFiber.Get_IsAutoKFiberEnable())

    print(AdjustFiber.Get_Results())
    print(AdjustFiber.Get_ResultMaxSlope())
    print(AdjustFiber.Get_ResultMinSlope())
    print(AdjustFiber.Get_ResultQuadraturePointPower())
    print(AdjustFiber.Get_ResultFiberVoltage())
    print(AdjustFiber.Get_ResultFiberPosition())
    print(AdjustFiber.Get_ResultLaserPower())
    print(AdjustFiber.Get_ResultFinesse())
    print(AdjustFiber.Get_ResultVisibility())

    
    print(AdjustFiber.Set_NumSamples(256))
    print(AdjustFiber.Set_NumAvg(6))
    print(AdjustFiber.Set_SlopeStepSize(6))
    print(AdjustFiber.Set_SlopeMode("MaxSlope"))
    print(AdjustFiber.Set_Gamma(0.85))
    print(AdjustFiber.Set_AutoKFiberEnable())


    print(AdjustFiber.FindQuadrature())
    time.sleep(5)
    while(True):
        isTunning = (bool)(AdjustFiber.Get_IsRunning()["IsRunning"])
        if(isTunning==False):
            break
        time.sleep(0.5)
        print(isTunning)
    
    print(AdjustFiber.Set_AutoKFiberDisable())
    print(AdjustFiber.Get_Results())
    print(AdjustFiber.Get_ResultMaxSlope())
    print(AdjustFiber.Get_ResultMinSlope())
    print(AdjustFiber.Get_ResultQuadraturePointPower())
    print(AdjustFiber.Get_ResultFiberVoltage())
    print(AdjustFiber.Get_ResultFiberPosition())
    print(AdjustFiber.Get_ResultLaserPower())
    print(AdjustFiber.Get_ResultFinesse())
    print(AdjustFiber.Get_ResultVisibility())

    print(AdjustFiber.Get_ForwardDataList())
    print(AdjustFiber.Stop())

  


 
    

