import IP
table_ip = []
class RouteTable():
    """
    Defines a routing table object, and basic operations on it. Next hop is a symbolic string
    """
    def __init__(self, table=[]):
        if not isinstance(table, list):
            raise ValueError('Invalid routing table: it must be a list')
        self.table = table
        for row in table:
            table_ip.append(IP.IPaddress(row))
        if table == []:
            self.fillTable()
        
    def fillTable(self):
        print("Enter IP address, netmask and next hop pair (comma separated), or just hit enter to finish: ")
        while True:
            user_input = input()
            if user_input == '':
                break
            table_ip.append(IP.IPaddress(input))
            #ip, netmask, next_hop = user_input.split(',')
            #self.table[IP.IPaddress(ip.strip(), netmmask=netmask)] = next_hop.strip()

    """
    def __str__(self):
        table_str = ''
        for ip, next_hop in self.table.items():
            table_str += f"{ip} -> {next_hop}\n"
        return table_str
    """
    
    def match(self, ip):
        """
        Given an IP address, return a list dict containing all matching ips, in the form of {ip: next_hop}. The ips are ordered by the number of matching bits
        """
        netmask_list = []
        for row in table_ip:
            if bin(row.ipBin)[:int(row.netmask)] != bin(ip.ipBin)[:int(row.netmask)]:
                table_ip.remove(row)
            else:
                netmask_list.append(int(row.netmask))
        
        posix=0
        netmask_list.sort(reverse=True)
        for net in netmask_list:
            for i in range(len(table_ip)):
                if(int(table_ip[i].netmask) == net):
                    elem = table_ip.pop(i)
                    table_ip.insert(posix, elem)
                    posix = posix + 1
                    break
        """
        matching = {}
        for table_ip, next_hop in self.table.items():
            if bin(table_ip.ipBin)[:table_ip.netmask] == bin(ip.ipBin)[:table_ip.netmask]:
                matching[table_ip] = next_hop       
        for table_ip, next_hop in self.table.items():
            result = '0b' + (bin(table_ip.ipBin & ip.ipBin)[2:]).zfill(32)
            limit = max(ip.netmask, table_ip.netmask)
            for i in range(2, limit):
                if result[i] != bin(ip.ipBin)[i]:
                   break
                matching[table_ip] = next_hop
        """
            
        # TODO: anzichè un dizionario, crea una lista di tuple, e ordina per il numero di bit corrispondenti
        # TODO: cambiare la modalità di caricamento degli ip della tabella in modo che vengano caricati iterativamente finché non viene inserito l'ip di default
        # TODO: inserire oltre la tabella di instradamento anche gli ip (con relative netmask) delle interfacce, dando una priorità superiore nel controllo di instradamento
        # TODO (facoltativo): stampare la tabella di routing bella formattata
        return table_ip
