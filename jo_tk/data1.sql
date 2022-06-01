create schema back_end;

use back_end;

create table clients(
    id_client smallint auto_increment primary key,
    noms varchar(50),
    telephones varchar(15),
    sexes char(1),
    categorie varchar(20),
    province varchar(30)
);

