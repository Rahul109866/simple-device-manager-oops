print('\033c')
#clears the screen for output

class DeviceManager():
    
    def __init__(self):
        self.connected_devices = []
        
    def add_device(self, device):
        self.connected_devices.append(device)
        
    def get_device_count(self):
        return f"{len(self.connected_devices)} devices are connected currently."

    def display_devices(self):
        for i, device in enumerate(self.connected_devices):
            print(i + 1, device)

class Device():
   
    device_manager = DeviceManager()
    
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
        print("Device connected...")
        Device.device_manager.connected_devices.append(self.name)
        
    def disconnect(self):
        self.connected = False
        print('{} Disconnected.'.format(self.name))
        Device.device_manager.connected_devices.remove(self.name)
    
    def connect(self):
        self.connected = True
        print('{} Connected.'.format(self.name))
    
    def __repr__(self):
        return "<{} device is connected through {}>".format(self.name, self.connected_by)
    
    
class Monitor(Device):
    
    def __init__(self, name, connected_by,view_mode='Home',current_refresh_rate=60):
        super().__init__(name, connected_by)
        self.current_refresh_rate = current_refresh_rate
        self.view_mode = view_mode
            
    def __repr__(self):
        return f"<{self.name}, {self.connected_by}, {self.current_refresh_rate}>"
    
    def help_modes(self):
        print("1.Home(Default)\n2.Cinematic\n3.Gaming\n4.Pleasant\n5.Cold")
        
    def change_mode(self, view_mode):
        self.view_mode = view_mode
        print("Display mode changed to {}".format(self.view_mode))
    
    def set_refresh_rate(self, refresh_rate):
        REFRESH_RATES = (30, 59, 60, 75, 90, 120, 144)
        if refresh_rate in REFRESH_RATES:
            print(f"Confirm change refresh rate to {refresh_rate}?\nPress y or n to confirm: ")
            
            while(True):
                user_input = input("->").lower()
                if user_input == 'y':
                    self.current_refresh_rate = refresh_rate
                    print(f"{self.name}'s refresh rate set to {self.current_refresh_rate}Hz")
                    break
                elif user_input == 'n':
                    print(f"Refresh rate unchanged. ({self.current_refresh_rate}Hz).")
                    break
                else:
                    print("Please enter a valid response.")
                    continue
        else:
            print("Invalid refresh rate.\n")
    
    @classmethod
    def gaming_mode(cls, name, connected_by):
        return cls(name,connected_by, view_mode='Gaming',current_refresh_rate=120)
        
    
    
if __name__ == "__main__":        
    printer = Device("HP printer", "Printer Cable")
    tcl_monitor = Monitor("TCL Office", 'VGA')
    acer_monitor = Monitor.gaming_mode("Acer ROG A65", 'HDMI')
    acer_monitor.set_refresh_rate(75)
    corsair_mouse = Device("Corsair Gaming Mouse", 'USB-2.0')
    
    print(Device.device_manager.get_device_count())
    Device.device_manager.display_devices()
    acer_monitor.disconnect()
    print(Device.device_manager.get_device_count())
    Device.device_manager.display_devices()
    
    
    
