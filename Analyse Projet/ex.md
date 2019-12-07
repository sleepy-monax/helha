# Exercice 1 - Observeur

Un produit est caractérisé par un intitulé, un prix et une quantité en stock. Un client possède un nom
et souhaite acheter un produit. Si le produit est disponible (stock suffisant), le stock est diminué de
1 et l'achat est accompli. Si le produit n'est plus disponible, le client est mis en attente et sera
prévenu au prochain réassortiment (augmentation de la quantité en stock). Au réassortiment, tous
les clients en attente sont prévenus. Ils essaient alors d'acheter le produit. Si le produit n'est plus
disponible, l'achat échoue. Dans tous les cas, les clients sont retirés de la liste d'attente.

Un produit
- intitulé
- prix
- une quantité en stock.

Un client
- nom

# Exercice 2 - Strategie

L'affichage d'une facture doit pouvoir s'effectuer différemment selon le pays dans lequel elle est
envoyée (utilisez un affichage en console). Une facture peut être envoyée soit en France soit en
Grande-Bretagne soit aux États-Unis. Une facture est caractérisée par un montant à payer (en
euros). Les informations à afficher sont : un texte dans la langue du pays d'envoi et l'affichage du
montant dans l'unité monétaire du pays (n'oubliez pas de convertir le montant). Un nouveau pays
doit pouvoir être ajouté facilement.

facture
- montant

# Exercice 3 - Iterateur

Un catalogue possède un nom ainsi qu'une liste de produits. Un produit est représenté par un nom,
un prix unitaire et une référence. L'ajout de produits au catalogue doit être réalisable (il s'agit ici
d'une composition) ainsi que de récupérer les informations concernant chacun des produits du
catalogue. Pour consulter la liste des produits du catalogue, la classe devra implémenter l'interface
Iterable<T> (il convient donc de rechercher les méthodes à implémenter dans l'API Java). La
consultation des produits du catalogue doit pouvoir se faire dans les deux sens (il faut donc pouvoir
revenir en arrière). La position de départ de la consultation doit aussi pouvoir être fournie.
Dans un deuxième temps, vous pouvez reprendre votre itérateur et prévoir de ne parcourir que les
éléments dont le prix unitaire est supérieur à celui spécifié à la création de l'itérateur.

# Exercice 4 - State

Lors de l'organisation d'un festival, il est possible d'acheter, de demander le remboursement et de
réserver des tickets ainsi que de valider une réservation (on veut chaque fois récupérer le prix de
l'opération). Un festival possède un nom, un nombre de tickets encore disponibles et un prix par
billet (fixé à la création du festival). Il y a différentes étapes dans la vente des billets. Lors de la
prévente, on peut acheter des tickets au prix normal, se faire rembourser au prix normal et réserver
des tickets en payant la moitié du prix. La validation d'une réservation n'est pas possible. La
deuxième étape commence 1 mois avant le festival, l'achat de tickets se fera à 150% du prix normal,
le remboursement à 50% du prix normal, il n'est plus possible de réserver et la validation d'une
réservation demande de payer 50% du prix. La troisième étape débute le premier jour du festival, il
est possible uniquement d'acheter des tickets à 200% du prix normal, les autres opérations ne sont
plus disponibles. Enfin la dernière étape du festival a lieu lorsque le festival est terminé, il n'y a
alors plus moyen de faire aucune des opérations.

# Exercice 5
Les données météorologiques récoltées par une station météorologique doivent être affichées dans
une fenêtre. Celle-ci doit être réactualisée à chaque changement d'une des informations. Les
données à afficher sont la température, le taux d'humidité et la vitesse du vent. Quels sont les
changements à apporter si une seconde fenêtre souhaite afficher ces mêmes informations ?