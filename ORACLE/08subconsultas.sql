select max(SALARIO) from EMP;
select * from EMP where SALARIO=(select max (SALARIO) from EMP);
--lo que esta entre parentesis es una subconsulta
select OFICIO from EMP where APELLIDO='alonso';
select * from EMP where OFICIO=(select OFICIO from EMP where APELLIDO='alonso');
select OFICIO from EMP where APELLIDO='alonso';--EMPLEADO
select SALARIO from EMP where APELLIDO='sala';--162500
select * from EMP where OFICIO=(select OFICIO from EMP where APELLIDO='alonso') and SALARIO>(select SALARIO from EMP where APELLIDO='sala');
select OFICIO from EMP where APELLIDO='jimenez' or APELLIDO='alonso';--
select * from EMP where OFICIO in (select OFICIO from EMP where APELLIDO='jimenez' or APELLIDO='alonso');
--el promedio de los 4 suledos superiores ignorando al presi
--avg(SALARIO)
--OFICIO<>'PRESIDENTE'
--SALARIO >??
--LOS 4 SALARIOS
select SALARIO from EMP order by SALARIO desc;
select avg(SALARIO) as MEDIASALARIAL from EMP where OFICIO <> 'PRESIDENTE';
--
select APELLIDO, SALARIO from EMP order by SALARIO desc;
select APELLIDO, avg(SALARIO) as MEDIASALARIAL from EMP where OFICIO <> 'PRESIDENTE' and rownum <= 4 group by APELLIDO order by avg(SALARIO) desc;
--COSULTAS UNION EMP DOCTOR PALTILLA
select APELLIDO, OFICIO, SALARIO from EMP;
select APELLIDO, ESPECILIDAD, SALARIO from DOCTOR;
select APELLIDO, FUNCION, SALARIO from PLANTILLA;
-- WHERE SOLO APLICA A CADA TABLA INDIVIDUAL 
select APELLIDO, OFICIO, SALARIO from EMP
union
select APELLIDO, ESPECIALIDAD, SALARIO from DOCTOR
union
select APELLIDO, FUNCION, SALARIO from PLANTILLA 
where SALARIO>250000
order by APELLIDO;
-- PARA APLICAR WHERE TIENE QUE HACERSE SOBRE TODAS LAS TABLAS DESUNIDAD
select APELLIDO, OFICIO, SALARIO from EMP
where SALARIO>250000
union
select APELLIDO, ESPECIALIDAD, SALARIO from DOCTOR
where SALARIO>250000
union
select APELLIDO, FUNCION, SALARIO from PLANTILLA 
where SALARIO>250000
order by APELLIDO;
-- EL ORDER BY SI FINCIONA PARA TODAS APLICANDOLO UNA VEZ AL FINAL
--consulta sobre una consulta HACERRRRR!!!!
--SELECT TO ROW
select APELLIDO, FUNCION, 
case TURNO 
    when 'T' then 'Tarde' 
    when 'M' then 'Mañana' 
    else 'Noche'
end as TURNOBONITO, TURNO
from PLANTILLA;

