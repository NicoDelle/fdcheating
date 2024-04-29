import IP
import unittest
import routeTable

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.ip = IP.IPaddress('192.168.1.100')
        self.rt = routeTable.RouteTable()

    def test_toBin(self):
        self.assertEqual(self.ip.toBin(), '0b11000000101010000000000101100100')

    def test_route(self):
        print(self.rt)

if __name__ == '__main__':
    unittest.main()
