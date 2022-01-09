"""
Test Script for trace_route method in module assessment. Test cases involve
1. Testing for trace route with wrong values
2. Testing for trace route with correct values
"""
import socket
import unittest
from networkdevices import assessment as asm


class TraceRouteTest(unittest.TestCase, asm.DeviceNetwork):
    # test for trace_route - wrong IP/hostname and port values
    def test_trace_route_with_wrong_values(self):
        print()
        print("test for trace_route - wrong IP and port values")
        print("-------------------------------------------------")
        ip = 'foo'    # wrong IP/hostname value
        port = 'bar'  # wrong port value
        result = asm.DeviceNetwork.route_tracer(self, ip, port, hops=30)
        self.assertEqual(result, '', "Expected result is PASS.")

    # test for trace_route - correct IP/hostname and port values
    def test_trace_route_with_correct_values(self):
        print()
        print("test for trace_route - correct IP/hostname and port values")
        print("-------------------------------------------------")
        ip = 'localhost'    # correct IP/hostname
        port = '80'     # correct port value
        result = asm.DeviceNetwork.route_tracer(self, ip, port, hops=30)
        self.assertEqual(result, str(socket.gethostbyname(ip)),
                         "Expected result is PASS.")


if __name__ == "__main__":
    unittest.main()
