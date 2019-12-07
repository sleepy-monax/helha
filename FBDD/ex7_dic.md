# Dictionaire des données

| Nom               | Type         | Format | Description |
| ----------------- | ------------ | -----: | ----------- |
| CLUB_ID           | Numeric      |      - |
| CLUB_NOM          | Alphanumeric |    128 |
| CLUB_BUDGET       | Numeric      |      - |
| TEAM_ID           | Numeric      |      - |
| TEAM_SURNAME      | Alphanumeric |    128 |
| MATCH_DATE        | Date         |      - |
| MATCH_HOME_POINT  | Numeric      |      - |
| MATCH_GUEST_POINT | Numeric      |      - |
| PLAYER_ID         | Numeric      |      - |
| PLAYER_FIRSTNAME  | Alphanumeric |     64 |
| PLAYER_LASTNAME   | Alphanumeric |     64 |
| PLAYER_BIRTHDATE  | Date         |      - |
| TRAINER_ID        | Numeric      |      - |
| TRAINER_FIRSTNAME | Alphanumeric |     64 |
| TRAINER_LASTNAME  | Alphanumeric |     64 |


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