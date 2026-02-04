select count(*) as REGISTROS from EMP;
select count(*) as REGISTROS, sum (SALARIO) as SUMASALARIAL from EMP;
select count(*) as EMPLEADOS, OFICIO from EMP group by OFICIO;
select max(SALARIO) as MAXIMOSALARIO, count(*) as PERSONAS, OFICIO, DEPT_NO from EMP group by OFICIO, DEPT_NO;
--Mostrar el numero de personas por cada ofico pero solamente mostrando directo y analista
select count(*) as PERSONAS, OFICIO from EMP where OFICIO in ('ANALISTA', 'DIRECTOR') group by OFICIO;
--Numero de empleados por cada oficio pero solamento mostrando los oficos donde tengamos mas de 2 personas trabajando
select count(*) as PERSONAS, OFICIO from EMP group by OFICIO having count(*)>2;
--Motrat la suma salarial por cada ofico 
select sum(SALARIO) as SUMASALARIA, OFICIO from EMP where COMISION >0 group by OFICIO ;
select sum(SALARIO) as SUMASALARIA, OFICIO from EMP where COMISION >0 group by OFICIO having sum(SALARIO)>515000;