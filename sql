create database url_database;
use url_database;
create table url_table ( id varchar(20) PRIMARY KEY , long_url varchar(1000), creation_date DATE, modify_date DATE, changekey varchar(513) UNIQUE);
