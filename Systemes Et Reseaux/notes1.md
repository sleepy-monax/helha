# Chapitre 8 : L'adressage IP

Structure en classe
 - A 255.0.0.0
 - B 255.255.0.0
 - C 255.255.255.0

 - D pas de masque (multi cast)
 - E pas de masque  (experimental)

## Classe A

- premier bit == 0b0xxxxxxx
- tres gros reseaux avec beaucoup de machine (reserver au GROS FAI)
-  1er octet : reseaux 
  - de 1 à 127
  - 254 resaux diferents 
- 2, 3, 4 octet : n° d'hote
    - 256^3 = 1677216 machines - 2 (car une address pour le reseaux + le broadcast)

## Classe B

premier bits = 0b10xxxxxx
- 1er octe : reseaux
  - de 128 à 191
- 16384 réseaux de classe b
- 256^2 = 65536 machines - 2 (car une address pour le reseaux + le broadcast)
- Gros reseaux

## Classe C

premier bits = 0b110xxxxx
- 1er octe : reseaux
  - de 192 à 223
- 2^21: 2_097_152resaux de classe c
- 256 machine - 2 (car une address pour le reseaux + le broadcast)
- Petit reseaux
  
## Classe E

premier bits = 0b1110xxxx
- 1er octe : reseaux
  - de 224 à 239

## Classe D

premier bits = 0b1110xxxx
- 1er octe : reseaux
  - de 240 à 247

# Trouver l'adresse resaux 

## 192.168.52.17 mask 255.255.255.0

l'address resaux = address & mask
 - 192.168.52.17 & 255.255.255.0 = 192.168.52.0

## 192.168.52.17 mask 255.255.192.0

192.168.52.17 & 255.255.192.0 = 192.168.0.0

# Trouver l'adresse broadcast 

Mettre la partie machine a la valeur maximal

## 192.168.52.17 mask 255.255.255.0

l'address broadcast = (address & mask) | (~mask)
 - (192.168.52.17 & 255.255.255.0) | (~mask)  = 192.168.52.255

reseaux suivant 192.168.53.000

## 192.168.52.17 mask 255.255.192.0

192.168.52.17 & 255.255.192.0 | (~mask) = 192.168.63.255

reseaux suivant 192.168.64.0

## Certaine IPv4 sont reserver
tout ce qui commence par un 0 est reserver
tout ce qui commence par 127 est resrver pour les test reseaux
    - 127.0.0.1 (loop back device) local host

## Adress particulier : les addresse priver

### Classe A
**10**.0.0.0

### Classe B
**172**.**16**.0.0

### Classe C
**192**.**168**.0.0

# Bidouille pour pouvoir assez d'ip priver public
- distinction des ip public / priver
- adressage sans classe
- distribution dynamique des IP

# Distinction entre ip public et priver

## Ip public 
fournie par le FAI

## Ip priver

fourni par l'admin resaux
ou un serveur dhcp

# Exercices

## 1. Soit l'adresse ip 10000000 00001010 00000010 00011110
1. Classe b car commence par 10
2. 128.10.2.30

## 2. 1, 2, 3
1. 4
2. 5
3. a: 1-3 b: 2-3 c:3-1 d: 1-3 e: 1-3
4. Un adress qui est restraite a un resaux priver
5. Classes:
    - Classe A : **10**.0.0.0
    - Classe B: **172**.**16**.0.0
    - Classe C :**192**.**168**.0.0

## 3
## 4
- 65000 car classe b
## 5. Reseaux