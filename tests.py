import IP
import unittest

ip1 = '192.168.1.100'
ipOK = '192.168.1.100'
ipNAH = '192.168.1.99'
ipHELLNAH = '1.3.5.7'


ip = IP.IPaddress(ip1)
print(bin(ip.ipBin))


class TestIP(unittest.TestCase):
    def setUp(self):
        self.ip = IP.IPaddress('192.168.1.100')

    def test_toBin(self):
        self.assertEqual(self.ip.toBin(), '0b11000000101010000000000101100100')

    

if __name__ == '__main__':
    unittest.main()