select avg(SALARIO) as MEDIA, count(*) as EMPLEADOS, OFICIO from EMP where OFICIO='ANALISTA' group by OFICIO;
select max(SALARIO) as MAXIMO, min(SALARIO) as MINIMO, max(SALARIO)-min(SALARIO) as DIFERENCIA from EMP where OFICIO='EMPLEADO';
select max(SALARIO) as MAXIMOS, OFICIO from EMP group by OFICIO;
select count(*) as NUMEROPERSONAS, OFICIO, DEPT_NO from EMP group by OFICIO, DEPT_NO order by DEPT_NO;
select count(*) as NUMEROPERSONAS, DEPT_NO from EMP group by DEPT_NO having count(*)>4;
select count(*) as NUMEROPERSONAS, DEPT_NO from EMP where OFICIO='DIRECTOR' group by DEPT_NO order by DEPT_NO;
select count(*) as NUMEROPERSONAS, FUNCION from PLANTILLA where FUNCION in ('ENFERMERO', 'ENFERMERA', 'INTERINO') group by FUNCION;
select count(*) as NUMEROPERSONAS, OFICIO, DEPT_NO from EMP group by OFICIO, DEPT_NO having count(*)>2 order by DEPT_NO;