create database empdepsystem;
use empdepsystem;
 create table employees(id int,empname varchar(100),age int,depname varchar(100));
 create table department(id int,depname varchar(100) );
 insert into employees(id,empname,age,depname)values(1000,'tom',20,'technical'),(1001,'ram',21,'hr'),(1002,'sam',22,'medical'),(1003,'ragu',23,'technical'),(1004,'mate',23,'hr'),(1005,'nate',25,'medical');
 insert into department(id,depname)values(2000,'technical'),(2002,'medical'),(2003,'hr');
 SELECT e.id,e.empname,e.age,e.depname,
    d.id,d.depname
    FROM employees as e,department as d
    WHERE e.depname=d.depname;
 UPDATE employees
     SET
        depname='hr'
     WHERE
        empname='sam';
DELETE FROM employees
     WHERE age=25;