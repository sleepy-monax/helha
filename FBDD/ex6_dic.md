# Dictionaire des données
 
| Nom                 | Type         | Format | Description                            |
| ------------------- | ------------ | -----: | -------------------------------------- |
| PIECE_ID            | Numeric      |      - | ID de la piece de theatre              |
| PIECE_TITRE         | Alphanumeric |    128 | Titre de la piece de theatre           |
| PIECE_TEMPS         | Numeric      |      - | Temps de la piece de theatre           |
| PIECE_PRIX_TICKET   | Numeric      |      - | Prix de la piece de theatre            |
| PIECE_ENTREE        | Numeric      |      - | Nombre d'entree de la piece de theatre |
| SPECTATEUR_ID       | Numeric      |      - | ID du spectateur                       |
| SPECTATEUR_NOM      | Alphanumeric |     64 | Nom du spectateur                      |
| SPECTATEUR_PRENOM   | Alphanumeric |     64 | Prenom du spectateur                   |
| AUTEUR_ID           | Numeric      |      - | ID de l'auteur                         |
| AUTEUR_NOM          | Alphanumeric |     64 | Nom de l'auteur                        |
| AUTEUR_PRENOM       | Alphanumeric |     64 | Prenom de l'auteur                     |
| ACTEUR_ID           | Numeric      |      - | ID de l'acteur                         |
| ACTEUR_NOM          | Alphanumeric |     64 | Nom de l'acteur                        |
| ACTEUR_PRENOM       | Alphanumeric |     64 | Prenom de l'acteur                     |
| REPRESENTATION_DATE | Date         |      - | Date de la representation              |

# Matrice des dépendances fonctionelles

|                     | PIECE_ID | SPECTATEUR_ID | AUTEUR_ID | ACTEUR_ID | REPRESENTATION_DATE |
| ------------------- | :------: | :-----------: | :-------: | :-------: | :-----------------: |
| PIECE_ID            |    -     |               |           |           |                     |
| PIECE_TITRE         |    1     |               |           |           |                     |
| PIECE_TEMPS         |    1     |               |           |           |                     |
| PIECE_PRIX_TICKET   |    1     |               |           |           |                     |
| PIECE_ENTREE        |    1     |               |           |           |                     |
| SPECTATEUR_ID       |          |       -       |           |           |                     |
| SPECTATEUR_NOM      |          |       1       |           |           |                     |
| SPECTATEUR_PRENOM   |          |       1       |           |           |                     |
| SPECTATEUR_DATE     |          |       1       |           |           |                     |
| AUTEUR_ID           |          |               |     -     |           |                     |
| AUTEUR_NOM          |          |               |     1     |           |                     |
| AUTEUR_PRENOM       |          |               |     1     |           |                     |
| ACTEUR_ID           |          |               |           |     -     |                     |
| ACTEUR_NOM          |          |               |           |     1     |                     |
| ACTEUR_PRENOM       |          |               |           |     1     |                     |
| REPRESENTATION_DATE |          |               |           |           |          -          |

# Modèle logique des données

 - Spectateur( *Id*, Nom, Prenom)
 - Assiste( **Spectateur**, **Representation**)
 - Representation( Date, **Piece**)
 - Piece( *Id*, Titre, Temps, PrixTicket)
 - Auteur( *Id*, Nom, Prenom)
 - Ecrit( **Auteur**, **Piece**)
 - Acteur( *Id*, Nom, Prenom)
 - Joue( **Acteur**, **Piece**)
 
