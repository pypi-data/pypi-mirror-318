from hpSPMPlusStudio import NMIEndpoint,NMIDevice
import requests,time

if __name__ == "__main__":
    # Define the endpoint by specifying the device's IP address and port
    # Ensure the IP and port match the device configuration
    Endpoint = NMIEndpoint("192.168.10.53",9024)

    # Initialize the device with the specified endpoint  
    Device = NMIDevice(Endpoint)

    # Example calls to device functionalities
    WindowControl = Device.WINDOWCONTROLLER()
    
   
    print(WindowControl.Get_Commands())  # List available commands
    print(WindowControl.Get_OpenedWindows())
    print(WindowControl.Get_IsOpened("Auto Tune"))
    print("SetMinimizeWindow")    
    print(WindowControl.Set_MinimizeWindow("Auto Tune"))
    time.sleep(3)
    print("SetMaximizeWindow")
    print(WindowControl.Set_MaximizeWindow("Auto Tune"))
    time.sleep(3)
    print("SetCloseWindow")
    print(WindowControl.Set_CloseWindow("Auto Tune"))
    time.sleep(3)
    print("SetMinimizeAll")
    print(WindowControl.Set_MinimizeAll())
    time.sleep(3)
    print("SetNormalizeAll")
    print(WindowControl.Set_NormalizeAll())