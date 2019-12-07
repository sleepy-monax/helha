# Dictionaire des données

|   ID | Nom              | Type         | Format | Description                    |
| ---: | ---------------- | ------------ | -----: | ------------------------------ |
|    0 | BOOK_ISBN        | Numeric      |        | Numero ISBN du livre           |
|    1 | BOOK_TITLE       | Alphanumeric |    256 | Titre du livre                 |
|    2 | BOOK_PUBLISHER   | Alphanumeric |     54 | Editeur du livre               |
|    3 | AUTHOR_ID        | Numeric      |        | Identifiant unique de l'auteur |
|    4 | AUTHOR_FIRSTNAME | Alphanumeric |     64 | Prenom de l'auteur             |
|    5 | AUTHOR_LASTNAME  | Alphanumeric |     64 | Nom de famille de l'auteur     |
|    6 | AUTHOR_PSEUDO    | Alphanumeric |     64 | Pseudo de d'auteur             |
|    7 | AUTHOR_BIRTH     | Date         |        | Date de naissance de l'auteur  |

# Matrice des dépendances fonctionelles 

|        /         | BOOK_ISBN | BOOK_TITLE | BOOK_PUBLISHER | AUTHOR_ID | AUTHOR_FIRSTNAME | AUTHOR_LASTNAME | AUTHOR_PSEUDO |
| :--------------: | :-------: | :--------: | :------------: | :-------: | :--------------: | :-------------: | :-----------: |
|    BOOK_ISBN     |     x     |            |                |           |                  |                 |               |
|    BOOK_TITLE    |     1     |     x      |                |           |                  |                 |               |
|  BOOK_PUBLISHER  |     1     |            |       x        |           |                  |                 |               |
|    AUTHOR_ID     |           |            |                |     x     |                  |                 |               |
| AUTHOR_FIRSTNAME |           |            |                |     1     |        x         |                 |               |
| AUTHOR_LASTNAME  |           |            |                |     1     |                  |        x        |               |
|  AUTHOR_PSEUDO   |           |            |                |     1     |                  |                 |       x       |

# Modèle logique des données

- Book( *BookISBN*, BookTitle, BookPublisher)
- Author ( *AuthorId*, AuthorFirstName, AuthorLastName, AuthorPseudo, AuthorBirth)
- Write( **Author**, **Book**)

