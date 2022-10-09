
-- Change dtabase name to yourusername_parts_and_suppliers
drop database if exists ehar_parts_and_suppliers ;
create database ehar_parts_and_suppliers;
\c ehar_parts_and_suppliers;
 
create table mega
(
    pno      integer,
    pname    text,
    color    text,
    weight   double precision,
    pcity    text,
    quantity integer,
    sno      integer,
    sname    text,
    status   integer,
    scity    text
);

\copy mega from 'mega.csv' with (format csv);