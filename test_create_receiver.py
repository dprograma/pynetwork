"""
Test Script for create_receiver method in module assessment. Test cases involve
1. Testing for wrong port values
2. Testing for correct port values
"""
import socket
import unittest
from networkdevices import assessment as asm

class CreateReceiverTest(unittest.TestCase):
    def test_for_wrong_port_values(self):
        print()
        print("Testing: Wrong port values")
        print("----------------------------")
        port = 'foo'    # wrong port number
        result = asm.DeviceNetwork.create_receiver(self, port)
        self.assertEqual(result, None, "expected result if PASS")
    
    def test_for_correct_port_values(self):
        print()
        print("Testing: Correct port values")
        print("----------------------------")
        port = '443'    # correct port number
        result = asm.DeviceNetwork.create_receiver(self, port)
        self.assertIsInstance(result, socket.socket, "expected result if PASS")
        
if __name__ == "__main__":
    unittest.main()