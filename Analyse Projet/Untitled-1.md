Vous devez réaliser le diagramme de classes complet et le diagramme de machine à état de
l'allocation d'un PC à un employé (vous devez placer au moins 2 activités). Vous devez également
justifier vos choix de représentation et les choix que vous avez dû opérer dans le diagramme de
classes.
L'application à créer devra notamment permettre la gestion des logiciels, du matériel et des
employés d'une entreprise.
Une entreprise est identifiée par un nom et un numéro de TVA. Elle achète des logiciels. Ces
logiciels sont installés sur des ordinateurs (les dates d'installation et de dernière utilisation de
chaque logiciel devront être retenues). Ces ordinateurs peuvent aussi bien être des serveurs que des
PC. Pour chaque entreprise qui achète un logiciel, on devra connaître le nombre de licences
achetées. On devra retrouver la liste des PC, serveurs, logiciels et périphériques que possède une
entreprise.
Un employé est caractérisé par un nom, un prénom et un numéro de registre national. Il peut
travailler dans plusieurs entreprises. Pour chaque contrat de travail, on veut connaître le salaire, la
date de début et la date de fin du contrat.
C'est le DRH (directeur des ressources humaines) qui devra introduire les demandes d'allocation
d'un PC à un employé. Voici les différentes étapes par lesquelles passera une allocation. Tout
d'abord, une demande sera introduite (il faudra en connaître la date). Si aucun PC n'est attribué dans
les deux jours ouvrables, un rappel sera automatiquement envoyé tous les jours jusqu'à l'allocation
d'un PC à un employé (on souhaitera connaître le nombre de rappels). Dès que le PC sera prêt, il
sera alloué à l'employé (on en retiendra la date). Enfin, lorsque l'employé n'a plus besoin du PC, il
sera rendu au service informatique (la date devra être enregistrée). Il faudra conserver toutes les
allocations de PC même celles qui sont terminées. Un PC se caractérise par un intitulé, un prix, une
référence, un processeur, une mémoire RAM, une taille du disque dur et une durée de leasing (en
mois).









Le DRH pourra également consulter des statistiques d'utilisation des PC et des logiciels.
Un employé pourra demander un dépannage pour son PC via l'application.
Un employé informatique devra pouvoir gérer les licences des différents logiciels ainsi que
configurer un PC. La configuration d'un serveur devra également être possible. Pour réaliser cela,
l'employé informatique entrera d'abord les informations de base concernant le serveur (intitulé, prix,
référence, processeur, mémoire RAM, taille du disque dur et nombre de connexions maximum).
Ensuite, si le serveur n'est pas le serveur principal, il précisera à quel serveur il est lié. Après cela, il
mentionnera les PC qui doivent être liés au serveur (si le nombre de connexions maximum est
dépassé, il devra refaire la sélection). Puis il devra lier un à un les différents périphériques au
serveur en précisant les informations concernant le périphérique (intitulé, prix, référence, type et
liste des drivers). Si le périphérique n'existe pas encore, le système devra rechercher les drivers
correspondants et les installer. Dès que tous les périphériques auront été liés au serveur, l'employé
informatique devra sélectionner les logiciels à installer (il verra apparaître le nom, le prix d'achat et
le prix d'une licence pour chaque logiciel). Le système installera alors les logiciels un à un. S'il
manque des licences pour les logiciels installés, le directeur informatique devra décider quelles
licences devront être achetées. Enfin, le système installera les licences choisies (il ne se passera rien
pour les logiciels sans licence) et préviendra en même temps l'employé informatique de
l'installation.
Pour une entreprise, il faut pouvoir retrouver le coût total représenté par les licences de tous les
logiciels en additionnant le coût des licences pour chaque logiciel détenus par l'entreprise