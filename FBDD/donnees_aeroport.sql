/*
Remplissage de compagnie
*/
insert into compagnie(indcomp, nomcomp, nbavions) values ('SNB', 'SN Brussels Airlines',10); 

insert into compagnie(indcomp, nomcomp, nbavions) values ('LUF','Lufthansa',150), ('SWS','Swiss Air',15),
('AFR','Air France',100);

/*
Remplissage de pilote
*/

insert into pilote(numlic, nompil, nbheures) values ('PIL001','Laverdure',1500), ('PIL002','Laverdure',900),
('PIL003','Tanguy',1600),('PIL004','Danny',2500);

/*
Remplissage de navigateur
*/

insert into navigateur(codenav, nomnav) values ('NAV001','Tuckson'), ('NAV002','Bryan');

insert into navigateur(codenav, nomnav) values ('NAV003','Lagaffe');

/*
Remplissage de aéroport
*/

insert into aeroport(nomaero, nbterm, paysaero, nomaeroprinc) values ('Zaventem',10,'Belgique',NULL), ('Charleroi',2,'Belgique','Zaventem'),
('Liège',1,'Belgique', 'Zaventem'), ('CDG',25,'France',NULL), ('Francfort',15,'Allemagne',NULL), ('Amsterdam',12,'Pays-Bas',NULL);

insert into aeroport(nomaero, nbterm, paysaero, vaccin1, nomaeroprinc) values ('Madrid',15,'Espagne','Peste',NULL), ('Oviedo',5,'Espagne','Grippe','Madrid'),
('JFK',50,'USA','Choléra',NULL), ('Delhi',16,'Inde','Fièvre jaune',NULL), ('Moscou',18,'Russie','Tétanos',NULL);

insert into aeroport(nomaero, nbterm, paysaero, vaccin1, vaccin2, nomaeroprinc) values ('Bangkok',19,'Thailande','Fièvre jaune','Grippe',NULL),
('Kinshasa',2,'RD Congo','Malaria','Fièvre jaune',NULL), ('Rio de Janeiro',14,'Brésil','Fièvre jaune','Grippe',NULL);

insert into aeroport(nomaero, nbterm, paysaero, nomaeroprinc) values ('Gijon',10,'Espagne','Oviedo');

/*
Remplissage de passager
*/

insert into passager(numpass, nompass, prepass, datenais, mail) values ('PASS01','Talon','Achille','1972-03-12','talon@hotmail.com'),
('PASS02','Morane','Bob','1968-10-05','morane@morane.com'), ('PASS03','Blake','Francis','1958-05-04','blake@hotmail.com');
insert into passager(numpass, nompass, prepass, datenais, mail) values ('PASS04','Dupont','Tom','1984-02-10','dupont@dupondt.com'),
('PASS05','Dupont','Jeff','1986-04-02','dupont@jeff.com'), ('PASS06','Dupond','Tim','1962-02-10','dupond@dupondt.com'),
('PASS07','Leblanc','Louis','1976-04-25','leblanc@hotmail.com');

insert into passager(numpass, nompass, prepass, datenais, mail) values ('PASS08','Dubois','Robin',19830904,'dubois@hotmail.com');
/*
Remplissage de vol
*/


insert into vol(numvol, indcomp, datedep, dureevol, typavion, nomaero, numlic, codenav) values 
(1, 'LUF','2015-03-01 12:00:00','25:00:00','Airbus A380','Zaventem','PIL001','NAV001'),
(1, 'SWS','2015-03-01 12:00:00','25:00:00','Boeing B120','Oviedo','PIL002','NAV003'),
(2, 'SWS','2015-03-01 12:00:00','25:00:00','Airbus A380','Bangkok','PIL003','NAV001');
insert into vol(numvol, indcomp, datedep, dureevol, typavion, nomaero, numlic, codenav) values 
(3, 'SWS','2015-03-20 15:00:00','05:30:00','Airbus A380','Bangkok','PIL003','NAV001');
insert into vol(numvol, indcomp, datedep, dureevol, typavion, nomaero, numlic, codenav) values 
(4, 'SWS','2015-03-21 16:00:00','01:30:00','Airbus A380','Amsterdam','PIL003','NAV001');
insert into vol(numvol, indcomp, datedep, dureevol, typavion, nomaero, numlic, codenav) values 
(2, 'LUF','2015-03-20 14:30:00','01:45:00','Airbus A380','Bangkok','PIL003','NAV001');
insert into vol(numvol, indcomp, datedep, dureevol, typavion, nomaero, numlic, codenav) values 
(5, 'SWS','2015-03-21 16:00:00','01:30:00','Airbus A380','Amsterdam','PIL001','NAV001');

/*
Remplissage de place
*/

insert into place(numplace, catplace, hublot, prixplace, indcomp, numvol, numpass) values (1, 'economique',false,1500.0,'SWS',1,null),
(2, 'economique',false,1500.0,'SWS',1,null), (3, 'economique',false,1500.0,'SWS',1,null), (4, 'economique',false,1500.0,'SWS',1,'PASS01'),
(5, 'economique',false,1500.0,'SWS',1,null), (6, 'economique',false,1500.0,'SWS',1,null), (7, 'business',false,2500.0,'SWS',1,'PASS02'),
(8, 'business',false,2500.0,'SWS',1,null), (9, 'business',false,2500.0,'SWS',1,null), (10, 'business',false,2500.0,'SWS',1,'PASS03');

insert into place(numplace, catplace, hublot, prixplace, indcomp, numvol, numpass) values (1, 'economique',false,1500.0,'SWS',2,null),
(2, 'economique',false,1500.0,'SWS',2,null);

/*
Remplissage de escale
*/

insert into escale (indcomp, numvol, nomaero, durescale) values ('SWS',1,'Zaventem','01:30:00'), ('SWS',2,'Amsterdam','01:00:00'),
('SWS',2,'Kinshasa','00:30:00'), ('LUF',1,'Zaventem','01:30:00');

insert into escale (indcomp, numvol, nomaero, durescale) values ('SWS',1,'Charleroi','00:30:00');
insert into escale (indcomp, numvol, nomaero, durescale) values ('SWS',2,'Charleroi','00:45:00');

insert into escale (indcomp, numvol, nomaero, durescale) values ('SWS',3,'Zaventem','01:30:00'), ('SWS',3,'Amsterdam','01:00:00'),
('SWS',3,'Bangkok','00:30:00'), ('SWS',4,'Zaventem','01:30:00');
