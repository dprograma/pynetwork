"""
Test Script for ping_host_by_ip, ping_host_by_name, ping_multiple_host methods in module assessment. Test cases involve
1. Testing for wrong IP/hostname list values (with correct port values)
2. Testing for correct IP/hostname list values (with correct port values)
3. Testing for wrong port values
"""
import unittest
from networkdevices import assessment as asm

class PingHostByIpTest(unittest.TestCase):

    def test_ip_is_wrong_list_values(self):
        print()
        print("Testing: IP is wrong list of values.")
        print("-------------------------------------")
        self.start_time = asm.DeviceNetwork.start_time
        ip = [43.2, 85.2, 93.5] # wrong list of IP values
        result = asm.DeviceNetwork.ping_host_by_ip(self, ip)
        self.assertNotEqual(result, 0, "Result should return PASS.")

    def test_ip_is_correct_list_values(self):
        print()
        print("Testing: IP is correct list of values.")
        print("-------------------------------------")
        self.start_time = asm.DeviceNetwork.start_time
        ip = ['127.0.0.1']  # correct list of IP value(s)
        result = asm.DeviceNetwork.ping_host_by_ip(self, ip)
        self.assertEqual(result, 0, "Result should return PASS.")

    def test_ip_is_wrong_single_value(self):
        print()
        print("Testing: IP is wrong single value.")
        print("-------------------------------------")
        self.start_time = asm.DeviceNetwork.start_time
        ip = 43.2   # wrong single IP value
        result = asm.DeviceNetwork.ping_host_by_ip(self, ip)
        self.assertNotEqual(result, 0, "Result should return PASS.")

    def test_ip_is_correct_single_value(self):
        print()
        print("Testing: IP is correct single value.")
        print("-------------------------------------")
        self.start_time = asm.DeviceNetwork.start_time
        ip = '127.0.0.1'    # correct single IP value
        result = asm.DeviceNetwork.ping_host_by_ip(self, ip)
        self.assertEqual(result, 0, "Result should return PASS.")


if __name__ == "__main__":
    unittest.main()
