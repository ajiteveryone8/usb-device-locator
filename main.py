import winreg

def get_usb_location_by_device_instance(instance_path: str):
    # Normalize for registry
    reg_path = r"SYSTEM\CurrentControlSet\Enum\{}".format(instance_path)

    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path) as device_key:
            try:
                location_info, _ = winreg.QueryValueEx(device_key, "LocationInformation")
            except FileNotFoundError:
                location_info = "Not Available"

            
            return {
                "DeviceInstancePath": instance_path,
                "LocationInformation": location_info,
                "RegistryPath": reg_path
            }

    except FileNotFoundError:
        print("Device registry path not found.")
        return None
    except PermissionError:
        print("Permission denied. Run the script as administrator.")
        return None

# Your device instance path
device_instance_path = r"USB\VID_0C45&PID_6366\SN0001"

info = get_usb_location_by_device_instance(device_instance_path)
if info:
    print("USB Device Location Info:")
    for key, value in info.items():
        print(f"{key}: {value}")
