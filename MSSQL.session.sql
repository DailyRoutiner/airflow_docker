USE master
GO
CREATE LOGIN sqlname WITH PASSWORD = N'Test123!'


create database testDB2;

USE testDB2
GO
CREATE USER sqlname FOR LOGIN sqlname