# USB Device Locator

This Python script retrieves information about a USB device's location, including the USB hub number and port number, using the device's instance path from the Windows registry.

## Features

- Fetches the USB device's location information from the Windows registry.
- Displays the device instance path, location information, and registry path.
- Handles errors such as missing registry paths or insufficient permissions.

## Requirements

- Python 3.x
- Windows operating system
- Administrator privileges (to access the Windows registry)

## Installation

1. Clone this repository or download the script file.
2. Ensure Python 3.x is installed on your system.
3. Run the script with administrator privileges.

## How to Get the Device Instance Path

To retrieve the device instance path for your USB device:

1. Open **Device Manager** on your Windows system.
   - Press `Win + X` and select **Device Manager**.
2. Locate your USB device under the **Universal Serial Bus controllers** or **Other devices** section.
3. Right-click on the device and select **Properties**.
4. Go to the **Details** tab.
5. From the **Property** dropdown, select **Device Instance Path**.
6. Copy the value displayed. It will look similar to: USB\VID_0C45&PID_6366\SN0001

## Usage

1. Open the script file `main.py`.
2. Replace the `device_instance_path` variable with the instance path of your USB device. For example:
```python
device_instance_path = r"USB\VID_0C45&PID_6366\SN0001"
```
3. Run the script:
```
python.exe .\main.py
```
4. If the device instance path is valid and accessible, the script will output the following information:
Device Instance Path
Location Information
Registry Path

## Example Output

- USB Device Location Info:
- DeviceInstancePath: USB\VID_0C45&PID_6366\SN0001
- LocationInformation: Port_#0001.Hub_#0002
- RegistryPath: SYSTEM\CurrentControlSet\Enum\USB\VID_0C45&PID_6366\SN0001

## Error Handling

Device registry path not found: This error occurs if the specified device instance path does not exist in the registry.
Permission denied: This error occurs if the script is not run with administrator privileges.


## Notes

The LocationInformation field may not be available for all devices. In such cases, it will display "Not Available."
Ensure you have the correct device instance path for the USB device you want to query.


## License

This project is licensed under the MIT License.
