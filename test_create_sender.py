"""
Test Script for create_sender method in module assessment. Test cases involve
1. Testing for wrong time-to-live values
2. Testing for correct time-to-live values
"""
import socket
import unittest
from networkdevices import assessment as asm

class CreateSenderTest(unittest.TestCase):
    def test_for_wrong_ttl_values(self):
        print()
        print("Testing: Wrong TTL values")
        print("----------------------------")
        ttl = 'foo' # wrong time-to-live value
        result = asm.DeviceNetwork.create_sender(self, ttl)
        self.assertEqual(result, None, "expected result if PASS")
    
    def test_for_correct_ttl_values(self):
        print()
        print("Testing: Correct TTL values")
        print("----------------------------")
        ttl = '1'   # correct time-to-live value 
        result = asm.DeviceNetwork.create_sender(self, ttl)
        self.assertIsInstance(result, socket.socket, "expected result if PASS")
        
if __name__ == "__main__":
    unittest.main()