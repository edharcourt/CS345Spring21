--drop database if exists parts_and_suppliers;
--create database parts_and_suppliers;
\c parts_and_suppliers
--\c exam1
drop table if exists shipments;
drop table if exists suppliers;
drop table if exists parts;

create table suppliers ( 
   sno int not null,
   sname text not null,
   status int not null,
   city text not null,
   primary key(sno));

create table parts (
   pno int not null,
   pname text not null,
   color text not null,
   weight double precision not null,
   city text,
   primary key (pno));

create table shipments (
   sno int not null,
   pno int not null,
   quantity int not null,
   primary key (pno,sno),
   foreign key (pno) references parts(pno),
   foreign key (sno) references suppliers(sno));

\copy suppliers from 'suppliers.csv' with (format csv);
\copy parts from 'parts.csv' with (format csv);
\copy shipments from 'shipments.csv' with (format csv);

-- clean up 
update parts set pname=trim(pname),color=trim(color),city=trim(city);
update suppliers set sname=trim(sname),city=trim(city);
