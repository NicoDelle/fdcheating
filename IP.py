class IPaddress:
    def __init__(self, ipAddress):
        self.ipraw = ipAddress
        self.ip = ipAddress.split('/')[0]
        if isinstance(self.ip, str):
            if self.ip.count('.') != 3:
                raise ValueError('Invalid IP address: it must be a string with 3 dots')
        else:
            raise ValueError('Invalid IP address: it must be a string with 3 dots')
        self.ipBin = int(self.toBin()[2:], 2)
        if len(ipAddress.split('/')) == 1:
            self.netmask = -1
        else:
            self.netmask = int(ipAddress.split('/')[-1].split(' ')[0])


    def toBin(self):
        """
        prende un indirizzo IP sottoforma di stringa puntuata e lo restituisce come numero binario a 32 bit
        """
        ipPieces = self.ip.split('.')
        ipBin = '0b'
        for word in ipPieces:
            ipBin += self.__padding(bin(int(word)).split('b')[1])

        return ipBin
    
    def matchWith(self, ip):
        """
        Given an IP addrss object, returns if the two Ips match in the range of the calling IP's netmask
        """
        if self.netmask == -1:
            raise ValueError('Netmask not set for this IP address')
        return (bin(self.ipBin & ip.ipBin)[2:]).zfill(32)[:self.netmask] == (bin(self.ipBin)[2:]).zfill(32)[:self.netmask]

    def __padding(self, partialIP):
        l = len(partialIP)
        return ('0' * (8-l)) + partialIP

    def __str__(self):
        binary_str = self.toBin()[2:]

        # Pad the binary string with zeros at the beginning if it's less than 32 bits
        binary_str = binary_str.zfill(32)

        # Format the binary string to add a dot every 8 characters
        formatted_binary_str = '.'.join(binary_str[i:i+8] for i in range(0, 32, 8))

        return f"IP: {self.ip}\nBinary IP: {formatted_binary_str}\nNetmask: {self.netmask}"
