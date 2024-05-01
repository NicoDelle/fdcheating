"""
File di esempio per l'utilizzo dei moduli IP e routeTable
"""
import IP
import routeTable

table = ['192.170.123.4/' + str(bin(IP.IPaddress("255.255.255.0").ipBin).count('1')) + ' A', 
         '192.170.124.4/' + str(bin(IP.IPaddress("255.255.255.0").ipBin).count('1')) + ' B',
         '191.138.112.0/' + str(bin(IP.IPaddress("255.255.240.0").ipBin).count('1')) + ' C', 
         '191.138.96.0/' + str(bin(IP.IPaddress("255.255.224.0").ipBin).count('1')) + ' D', 
         '192.138.0.0/' + str(bin(IP.IPaddress("255.255.0.0").ipBin).count('1')) + ' E',
         '191.138.160.0/' + str(bin(IP.IPaddress("255.255.224.0").ipBin).count('1')) + ' F', 
         '0.0.0.0/0' + ' G']
ip = IP.IPaddress('191.138.163.13') # non è necessario fornire la netmask

print("\n")
for row in result:
    print(row.ipraw)

""" 
SI può creare una tabella di routing come dizionario, fornendo coppie di oggetti IP e simbolici next hop (non serve implementari i next hop come veri IP).

La sintassi per creare un oggetto IP è:
ip = IP.IPaddress(IP, netmask=0) (si chiama la classe IPaddress del modulo IP, e gli si passa una stringa puntuata con un indirizzo ip decimale e ll'eventuale netmask, altrimenti settata ad una flag di -1). è disponibile anche un attributo per accedere al valore binario dell'IP, ip.ipBin.
Per vedere entrambe le rappresentazioni si può direttamente chiamare print() su un oggetto IP

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

ip = IP.IPaddress('192.168.1.10') # non è necessario fornire la netmask

La tabella di routing è creata passando il dizionario di cui sopra. Altrimenti, si può invocare il costruttore (routeTable.RouteTable()) senza argomenti: in questo modo si aggiungeranno le info da CLI, al momento.

rt = routeTable.RouteTable(table)


Invocare il metodo .match(ip) su un oggetto RouteTable restituisce un dizionario contenente la corrispondenza tra l'indirizzo IP e il next hop simbolico.

print(rt.match(ip))

"""
