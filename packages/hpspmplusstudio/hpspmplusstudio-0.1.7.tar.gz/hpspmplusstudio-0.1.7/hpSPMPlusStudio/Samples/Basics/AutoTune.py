from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()
    AutoTune = Device.AUTOTUNE()

    print(AutoTune.Get_IsInit())
    print(AutoTune.Set_Initialize())
    print(AutoTune.Get_IsInit())

    print(AutoTune.Get_Commands())
    print(AutoTune.Get_Excitation())
    print(AutoTune.Get_ExcitationPercent())
    print(AutoTune.Get_FrequencyStartInHertz())
    print(AutoTune.Get_FrequencyEndInHertz())
    print(AutoTune.Get_FrequencyIncrementInHertz())
    print(AutoTune.Get_FrequencySlopeTypes())
    print(AutoTune.Get_FrequencySlopeType())
    print(AutoTune.Get_IsCenterSpan())
    print(AutoTune.Get_StartDelay())
    print(AutoTune.Get_Delay())

    print(AutoTune.Set_ExcitationPercent(30))
    print(AutoTune.Set_FrequencyStartInHertz(100000))
    print(AutoTune.Set_FrequencyEndInHertz(300000))
    print(AutoTune.Set_FrequencyIncrementInHertz(1000))
    print(AutoTune.Set_Delay(1))
    print(AutoTune.Set_StartDelay(300))
    print(AutoTune.Set_FrequencySlope("MinSlope"))

    print(AutoTune.StartTune())
    time.sleep(5)
    while(True):
        isTunning = (bool)(AutoTune.Get_IsTunning()["IsTunning"])
        if(isTunning==False):
            break
        time.sleep(0.5)
        print(isTunning)
    
    print(AutoTune.Get_MaxRms())
    print(AutoTune.Get_MaxRmsFrequency())
    print(AutoTune.Get_MinSlopeFrequency())
    print(AutoTune.Get_MinSlopeRms())
    print(AutoTune.Get_MaxSlopeFrequency())
    print(AutoTune.Get_MaxSlopeRms())

    print(AutoTune.Get_CoarseRmsSeries())
    print(AutoTune.Get_CoarsePhaseSeries())
    


 
    

