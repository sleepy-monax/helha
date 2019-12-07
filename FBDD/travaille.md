Regroupez dans un document converti en PDF (respectant la convention suivante pour le
nom : Groupe « numéro » rapport travail de groupe 1) dans lequel les noms des membres
composant le groupe apparaîtront clairement : dictionnaire des données, matrice des
dépendances fonctionnelles (avec les simplifications visibles) et schéma entités-associations
(complété éventuellement de choix de représentation sous forme de questions à poser au
client avec les réponses que vous avez apportées) pour le problème suivant.

Une société propriétaire de plusieurs stations de ski souhaite créer une base de données afin
de gérer au mieux le fonctionnement de ses différentes stations.

**Une station de ski** possède un **nom** qui est unique. Il faut savoir à quelle **altitude** se trouve la
station ainsi que l'**épaisseur actuelle de la couche de neige**. Chaque station dispose d'un
**budget annuel** pour l'entretien de ses infrastructures. Certaines stations, étant plus
importantes que d'autres, sont **responsables administrativement** de plus petites stations.
Une station de ski compte plusieurs *pistes de ski*. Chaque piste possède un *numéro unique
pour la station à laquelle elle appartient*. Il faut connaître *la couleur* de la piste ainsi que sa
*longueur*. Une piste peut éventuellement être *rendue indisponible*, on doit alors connaître *la
date de fin de son indisponibilité*.

Chaque **station de ski est également propriétaire de différents logements** dans lesquels
séjournent des clients. On veut **retenir l'historique des séjours des clients**. Il faut donc
connaître les **dates de début** et de **fin de séjour** de chaque client dans un logement. Un
**logement est identifié par un code de 20 caractères**. Chaque logement a un **prix** de location à
la **semaine** (reste le même toute l'année). Il faut également savoir **combien de personnes
peuvent y séjourner simultanément**.
Un **client** possède un **identifiant unique (nombre auto-incrémenté)**. Il faut connaître le **nom**
et le **prénom** du client. Il faut aussi pouvoir fournir des statistiques sur les **pays de
provenance** des clients. Une **ristourne est offerte aux clients de moins de 30 ans (age)**. Le client
doit fournir au moins une **adresse mail** et **peut éventuellement en donner une seconde**.
Chaque client doit scanner son pass lorsqu'il souhaite emprunter une piste. **Il faut donc
pouvoir retrouver quel client a déjà skié sur quelle piste** (on ne souhaite pas savoir quand le
client a emprunté la piste).
Une **station** dispose aussi de **matériels qu'elle peut louer**. Un matériel est **identifié par un
code de 20 caractères**. Chaque matériel possède une **dénomination** et un **prix** à la journée. Il
faut savoir de quel **type de matériel il s'agit (ski, bâtons,...)**. Un client peut **louer plusieurs
matériels** mais on ne souhaite pas en garder un historique. On veut juste savoir quel client
est en train de louer quel matériel **(la date de début de la location est nécessaire pour pouvoir
facturer le client).**

