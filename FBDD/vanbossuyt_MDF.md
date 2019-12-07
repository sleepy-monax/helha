---
geometry: margin=1cm
---

# Dictionnaire des données
|      | Nom                  | Type         | Format | Description                                 |
| ---: | -------------------- | ------------ | -----: | ------------------------------------------- |
|    0 | PERSONNE_ID          | Numeric      |      - | Identifiant de la personne                  |
|    1 | PERSONNE_FISTNAME    | Alphanumeric |     64 | Nom de la personne                          |
|    2 | PERSONNE_LASTNAME    | Alphanumeric |     64 | Prenom de la personne                       |
|    3 | PERSONNE_BIRTHDATE   | Date         |      - | Date de la personne (pour calculer l'age)   |
|    4 | AUTHOR_PSEUDO        | Alphanumeric |     64 | Pseudo de l'auteur                          |
|    5 | AUTHOR_STAYTIME      | Numeric      |      - | Combien de temps reste l'auteur             |
|    6 | AUTHOR_BREAKFAST     | Bool         |      - | L'auteur prend il le petit dej              |
|    7 | ACTIVITY_ID          | Numeric      |      - | Identifiant de l'activiter                  |
|    8 | ACTIVITY_DATE        | DateTime     |      - | Date précise de l'activiter                 |
|    9 | ACTIVITY_LOCATION    | Alphanumeric |     64 | Lieu ou se déroule l'activiter              |
|   10 | ACTIVITY_PARTICIPANT | Numeric      |      - | Nombre maximun de participant a l'activiter |
|   11 | VOLUNTEER_TIME       | Numeric      |      - | Temps de travail d'un bénévole              |
|   12 | HOTEL_NAME           | Alphanumeric |    128 | Nom de l'hotel                              |
|   13 | HOTEL_ROOMPRICE      | Numeric      |      - | Prix de la chambre de l'hotel               |
|   14 | HOTEL_BREAKFASTPRICE | Numeric      |      - | Prix du petit dej de l'hotel                |

# Matrice des dépendances fonctionnelles

|                      | PERSONNE_ID | ACTIVITY_ID | HOTEL_NAME |
| :------------------: | :---------: | :---------: | :--------: |
|     PERSONNE_ID      |      -      |             |            |
|  PERSONNE_FISTNAME   |      1      |             |            |
|  PERSONNE_LASTNAME   |      1      |             |            |
|  PERSONNE_BIRTHDATE  |      1      |             |            |
|    AUTHOR_PSEUDO     |      1      |             |            |
|   AUTHOR_STAYTIME    |      1      |             |            |
|   AUTHOR_BREAKFAST   |      1      |             |            |
|     ACTIVITY_ID      |             |      -      |            |
|    ACTIVITY_DATE     |             |      1      |            |
|  ACTIVITY_LOCATION   |             |      1      |            |
| ACTIVITY_PARTICIPANT |             |      1      |            |
|    VOLUNTEER_TIME    |      1      |             |            |
|      HOTEL_NAME      |             |             |     -      |
|   HOTEL_ROOMPRICE    |             |             |     1      |
| HOTEL_BREAKFASTPRICE |             |             |     1      |