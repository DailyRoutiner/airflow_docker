--SELECT * FROM master.dbo.sysdatabases;

create table testTable
(
    id int identity(1,1) primary key,
    name varchar(50)
);

select * from testTable;

insert into testTable(name) values('test2');