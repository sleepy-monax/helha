DROP Database IF EXISTS Exemple
CREATE DATABASE IF NOT EXISTS Exemple character set = 'utf8';

USE Exemple;

CREATE TABLE IF NOT EXISTS Livre (
    isbn CHAR(15) NOT NULL,

    titre VARCHAR(80) NOT NULL,
    datesortie DATE,
    nbpages SMALLINT UNSIGNED NOT NULL DEFAULT 100,
    prix NUMERIC(7,2) NOT NULL,

    PRIMARY KEY(isbn);
);

CREATE TABLE IF NOT EXISTS Exemplaire (
    id UNSIGNED INT NOT NULL,

    isbn char(15) NOT NULL,
    editeur VARCHAR(50) NOT NULL,

    PRIMARY KEY(isbn, id)
    # ou: PRIMARY KEY(id, isbn), KEY(isbn);
);

ALTER TABLE Exemplaire ADD CONSTRAIN fk_Exemplaire_Livre FOREIGN KEY(isbn) Livre(isbn);

DESCRIBE Exemplaire;

 
