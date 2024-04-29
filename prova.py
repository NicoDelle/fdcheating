import IP
import routeTable

table = {
    IP.IPaddress(
        '192.168.1.0', 
        netmask=24
        ): 'A',

    IP.IPaddress(
        '31.128.0.0',
          netmask=9
        ): 'B'
}

ip = IP.IPaddress('192.168.1.10')
rt = routeTable.RouteTable(table)
print(rt.match(ip))
