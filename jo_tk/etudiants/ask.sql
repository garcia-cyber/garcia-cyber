use back_end;


create table etudiants(
    matricule smallint auto_increment primary key,
    nom varchar(25),
    prenom varchar(25),
    villes varchar(25),
    sexe char(1),
    faculte varchar(20),
    promotion varchar(25),
    telephone varchar(15)

);


create table commentaires(
    id_com smallint auto_increment primary key,
    mots text
);


create table user_login (
    id_log tinyint auto_increment primary key,
    username varchar(25),
    pwd varchar(255)
);
