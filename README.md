libreria per confrontare indirizzi ip con agio, pensata per tabelle di routing

## Installazione facile
Per usare il modulo python come una qualunque libreria (e quindi per poterlo importare da qualunque posizione nel sistema), basta:
<ol>
  <li>Clonare la repo nel sistema</li>
  <li><a href='https://www.tutorialspoint.com/How-to-set-python-environment-variable-PYTHONPATH-on-Windows'>Aggiungere la cartella contenente gli script ad PYTHONPATH</li>
</ol>
Ciò  può essere particolarmenrte comodo per usare i moduli in una shell spawnata ad hoc.

## Esempi di utilizzo
### Match di IP
Il modulo IP è pensato per supportare il più ampio modulo delle tabelle di routing, ma è anche flessibile di suo.
Per confrontare due IP secondo la meccanica "match":
 ```
   import IP
   ip1 = IP.IPaddress('192.168.1.0/24')
   ip2 = IP.IPaddress('192.168.1.53')

   #Controllo che facciano match:
   ip1.matchWith(ip2)

>>> True
 ```
