"""
Test Script for port_scan method in module assessment. Test cases involve
1. Testing for wrong IP/hostname list values (with correct port values)
2. Testing for correct IP/hostname list values (with correct port values)
3. Testing for wrong port values
"""
import unittest
from networkdevices import assessment as asm

class PortScanTest(unittest.TestCase):
    def test_ip_is_wrong_list_values(self):
        print()
        print("Testing: IP is wrong list values.")
        print("----------------------------------")
        self.start_time = asm.DeviceNetwork.start_time
        ip = [43.2, 85.2, 93.5] # IP/hostname list
        r1 = '443'              # first range value (correct value)
        r2 = '444'              # second range value (correct value)
        result = asm.DeviceNetwork.port_scan(self, ip, r1, r2)
        self.assertNotEqual(result, 0, "Expected result is PASS")
    
    def test_ip_is_correct_list_values(self):
        print()
        print("Testing: IP is correct list values.")
        print("----------------------------------")
        self.start_time = asm.DeviceNetwork.start_time
        ip = 'yahoo.com, google.com, facebook.com' # IP/hostname list
        r1 = '443'              # first range value (correct value)
        r2 = '444'              # second range value (correct value)
        result = asm.DeviceNetwork.port_scan(self, ip, r1, r2)
        self.assertEqual(result, 0, "Expected result is PASS")
        
    def test_wrong_port_values(self):
        print()
        print("Testing: wrong port values.")
        print("----------------------------------")
        self.start_time = asm.DeviceNetwork.start_time
        ip = 'yahoo.com, google.com, facebook.com' # IP/hostname list
        r1 = 'foo'              # first range value (incorrect value)
        r2 = 'bar'              # second range value (incorrect value)
        result = asm.DeviceNetwork.port_scan(self, ip, r1, r2)
        self.assertNotEqual(result, 0, "Expected result is PASS")

if __name__ == "__main__":
    unittest.main()