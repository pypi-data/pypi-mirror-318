from hpSPMPlusStudio import NMICommand,NMIEndpoint,NMIDevice
import time

if __name__ == "__main__":
    Endpoint = NMIEndpoint("192.168.10.53",9024)
    Device = NMIDevice(Endpoint)
    Scan = Device.SCAN()
    Options = Device.OPTIONS()
    XYOffsetController = Device.XYOFFSET()
    Status = Device.STATUS()
    ScannedImages = Device.SCANNEDIMAGES()
    
    ScannedImages.Get_NmiContainers()
    ScannedImages.Get_SelectedContainerImageList()
    ScannedImages.Get_SelectedContainerImage()
    

        







    

