# Goupe B4: CAUDRON David, DHAEYER Sasha, VAN BOSSUYT Nicolas

CREATE DATABASE IF NOT EXISTS Travail_groupe_SQL character set = 'utf8';
USE Travail_groupe_SQL ;

SET default_storage_engine = INNODB;

CREATE TABLE IF NOT EXISTS Employe(
    numemp VARCHAR(15) UNSIGNED NOT NULL,
    numregnat VARCHAR(15) UNSIGNED NOT NULL,
    nomemp VARCHAR(50) NOT NULL,

    prenomsemp0 VARCHAR(50) NOT NULL,
    prenomsemp1 VARCHAR(50),
    prenomsemp2 VARCHAR(50),

    dateNais DATE NOT NULL,
    sexe CHAR(1) NOT NULL,
    rueemp VARCHAR(100) NOT NULL,
    numeroemp VARCHAR(5) NOT NULL,
    cpemp SMALLINT UNSIGNED NOT NULL,
    villeemp VARCHAR(100) NOT NULL,
    salfixe FLOAT(9,2) UNSIGNED NOT NULL,
    saldepl FLOAT(5,2) UNSIGNED NOT NULL,

    supervise SMALLINT UNSIGNED,
    travailPour VARCHAR(50),
    nomdep VARCHAR(50),

    PRIMARY KEY(numemp),
    KEY (numregnat, nomdep)
);

CREATE TABLE IF NOT EXISTS Enfant(
    prenomenf VARCHAR(100) NOT NULL,
    respenf INT NOT NULL,
    sexenf CHAR(1),
    naisenf DATE NOT NULL,

    numemp SMALLINT UNSIGNED NOT NULL,

    PRIMARY KEY (prenomenf),
    KEY (numemp)
);

CREATE TABLE IF NOT EXISTS Departement(
    numdep INT NOT NULL,
    nomdep VARCHAR(50) NOT NULL,

    services0 VARCHAR(200) NOT NULL,
    services1 VARCHAR(200),
    services2 VARCHAR(200),
    services3 VARCHAR(200),
    services4 VARCHAR(200),

    ruedep VARCHAR(100) NOT NULL,
    numemrodep INT NOT NULL,
    cpdep INT NOT NULL,
    villedp VARCHAR(100) NOT NULL,

    datedepdir DATETIME NOT NULL,

    controle VARCHAR(100),

    PRIMARY KEY(nomdep)
);

CREATE TABLE IF NOT EXISTS Projet(
    nomproj VARCHAR(100) NOT NULL,
    budgetpoj DECIMAL(9,2) NOT NULL,
    datedeproj DATETIME NOT NULL,

    PRIMARY KEY(nomproj)
);

CREATE TABLE IF NOT EXISTS TravailleSur(
    nbheures FLOAT(6,2) NOT NULL,
    numemp SMALLINT UNSIGNED NOT NULL,
    nomproj VARCHAR(100) NOT NULL,

    KEY (numemp),
    KEY (nomproj),

    PRIMARY KEY (numemp, nomproj)
);

ALTER TABLE Enfant ADD CONSTRAINT FK_emp FOREIGN KEY(numemp) REFERENCES Employe(numemp);
ALTER TABLE Employe ADD CONSTRAINT FK_supervise FOREIGN KEY(supervise) REFERENCES Employe(numemp);
ALTER TABLE Employe ADD CONSTRAINT FK_travailPour FOREIGN KEY(travailPour) REFERENCES Departement(nomdep);
ALTER TABLE Departement ADD CONSTRAINT FK_controle FOREIGN KEY(controle) REFERENCES Projet(nomproj);
