IP = '192.168.1.100'
ipOK = '192.168.1.100'
ipNAH = '192.168.1.99'
ipHELLNAH = '1.3.5.7'

def toBin(ip):
    """
    prende un indirizzo IP sottoforma di stringa puntuata e lo restituisce come numero binario a 32 bit
    """
    ipPieces = ip.split('.')
    ipBin = '0b'
    for word in ipPieces:
        ipBin += padding(bin(int(word)).split('b')[1])

    return int(ipBin, 2)

def padding(rawBin):
    l = len(rawBin)
    return ('0' * (8-l)) + rawBin

def formatBin(rawBin):
    l = len(rawBin)
    rawBin = '0'*(34 - l) + (rawBin.split('b')[1])
    for i in range(0, 33, 9):
        rawBin = rawBin[:i] + '.' + rawBin[i:]
    
    return rawBin[1:]

ipBin = toBin(IP)
ipBinOK = toBin(ipOK)
ipBinNAH = toBin(ipNAH)
ipBinHELLNAH = toBin(ipHELLNAH)
"""
print(bin(ipBin & ipBinOK))
print(bin(ipBin & ipBinNAH))
"""
print(bin(ipBin))
print(bin(ipBinHELLNAH))
print(formatBin(bin(ipBin & ipBinHELLNAH)))