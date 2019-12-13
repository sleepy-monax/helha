/*
Création des tables
*/

create table if not exists compagnie (
indcomp char(3) not null,
nomcomp varchar(100) not null,
nbavions smallint not null,
primary key (indcomp))engine=innodb;

create table if not exists vol (
numvol int not null,
datedep datetime not null,
dureevol time not null,
typavion varchar(100) not null,
indcomp char(3) not null, 
nomaero varchar(100) not null,
numlic char(15) not null,
codenav char(15) not null,
primary key (indcomp, numvol),
key(nomaero),
key(numlic),
key(codenav))engine=innodb;

create table if not exists aeroport(
nomaero varchar(100) not null,
nbterm smallint not null,
paysaero varchar(100) not null,
vaccin1 varchar(100),
vaccin2 varchar(100),
vaccin3 varchar(100),
nomaeroprinc varchar(100),
primary key(nomaero),
key(nomaeroprinc))engine=innodb;

create table if not exists pilote(
numlic char(15) not null,
nompil varchar(100) not null,
nbheures int not null,
primary key(numlic))engine=innodb;

create table if not exists navigateur(
codenav char(15) not null,
nomnav varchar(100) not null,
primary key(codenav))engine=innodb;

create table if not exists passager(
numpass char(15) not null,
nompass varchar(100) not null,
prepass varchar(100) not null,
datenais date not null,
mail varchar(150) not null,
primary key(numpass))engine=innodb;

create table if not exists place(
numplace smallint not null,
catplace varchar(60) not null,
hublot boolean not null,
prixplace decimal(7,2),
indcomp char(3) not null,
numvol int not null,
numpass char(15),
primary key(indcomp, numvol, numplace),
key(numpass))engine=innodb;

create table if not exists escale(
indcomp char(3) not null,
numvol int not null,
nomaero varchar(100) not null,
durescale time not null,
primary key(indcomp, numvol, nomaero),
key(nomaero))engine=innodb;

/*
Les clés étrangères
*/

alter table vol add constraint fkvolcomp foreign key(indcomp) references compagnie(indcomp) on delete cascade on update cascade,
	add constraint fkvolaerodest foreign key(nomaero) references aeroport(nomaero) on update cascade,
	add constraint fkvolpilote foreign key(numlic) references pilote(numlic) on update cascade,
	add constraint fkvolnavigateur foreign key(codenav) references navigateur(codenav) on update cascade;
alter table aeroport add constraint fkaeroprinc foreign key(nomaeroprinc) references aeroport(nomaero) on delete set null on update cascade;
alter table place add constraint fkplacevol foreign key(indcomp, numvol) references vol(indcomp, numvol),
	add constraint fkplacepassager foreign key(numpass) references passager(numpass);
alter table escale add constraint fkescalevol foreign key(indcomp, numvol) references vol(indcomp, numvol),
	add constraint fkescaleaeroport foreign key (nomaero) references aeroport(nomaero);
	

