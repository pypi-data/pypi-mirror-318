from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()

    #GetCurrentScale
    print(Options.Get_XYScale())
    print(Options.Get_ZScale())

    #SetScanStartPosition
    XYOffsetController.Set_XYOffset(0,0)

    #ScanOptions
    Scan.Set_XOffset(0) 
    Scan.Set_YOffset(0)

    Scan.Set_ScanHeightPixel(64) #128pixel
    Scan.Set_ScanWidthPixel(64) #128pixel

    Scan.Set_ImageWidth(3) #RealDistance 
    Scan.Set_ImageHeight(3) #RealDistance

    Scan.Set_ScanAngle(0)

    Scan.Set_ScanNumberOfAverages(4)
    Scan.Set_NumberOfScans(1)
    Scan.Set_ScanSpeed(5)    
    Scan.Set_IsSaveScannedImages(True)
    Scan.Set_OffsetPosition("BottomLeft")
    Scan.Set_ScanDirection("BottomToTop")
    
    isScanning = (bool)(Scan.Get_IsScanning()["IsScanning"])
    hasError = Scan.Get_ScanError()["ScanError"]
    status = Status.Get_Status()
    time.sleep(2)
    if(isScanning==False and status == "Ready"):
        Scan.StartScan(True)
        time.sleep(2)
        while(True):
            isScanning = (bool)(Scan.Get_IsScanning()["IsScanning"])
            if(isScanning==False):
                break
            print(Scan.Get_ScanLineIndex())
            print(Scan.Get_ScanIndex())
            time.sleep(0.5)
    
    hasError = Scan.Get_ScanError()["ScanError"]
    print(hasError)

    
        







    

