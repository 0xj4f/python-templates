import bluetooth
"""
sudo apt-get install libbluetooth-dev
pip3 install pybluez


References:
- https://pybluez.readthedocs.io/en/latest/install.html
- https://people.csail.mit.edu/albert/bluez-intro/c212.html
"""

class BluetoothEnumerator:

    def __init__(self):
        # Initialize any necessary attributes
        pass

    def scan_for_devices(self):
        """Scans for nearby Bluetooth devices."""
        print("Scanning for Bluetooth devices...")
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        
        if not nearby_devices:
            print("No devices found.")
            return []

        print(f"Found {len(nearby_devices)} devices.")
        devices = []
        for addr, name in nearby_devices:
            print(f"  Address: {addr}, Name: {name}")
            devices.append((addr, name))
        return devices

    # Additional Bluetooth functionalities can be added as methods here
    # For example, methods to pair, connect, send data, etc.

# Usage
if __name__ == "__main__":
    enumerator = BluetoothEnumerator()
    devices = enumerator.scan_for_devices()
