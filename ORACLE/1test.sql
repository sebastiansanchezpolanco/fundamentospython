--
select * from EMP;
--
select APELLIDO, SALARIO*14+COMISION as SALARIO_ANUAL 
from EMP 
where COMISION>100000;
--
select APELLIDO, SALARIO*14+COMISION as SALARIO_ANUAL 
from EMP 
where SALARIO*14+COMISION>750000;
--
select APELLIDO, SALARIO*14+COMISION as SALARIO_ANUAL 
from EMP 
where SALARIO*14+COMISION>1000000;
--
select * 
from EMP 
order by DEPT_NO, OFICIO;
--
select * 
from ENFERMO 
where FECHA_NAC>'1/1/70';

select * 
from ENFERMO 
where FECHA_NAC<'1/1/70' 
order by INSCRIPCION desc;
--
select * 
from PLANTILLA;
--
select * 
from PLANTILLA 
where TURNO ='M';
--
select * 
from PLANTILLA 
where TURNO ='N';
--
select * 
from DOCTOR 
where SALARIO*12>3000000;
--
select * 
from PLANTILLA 
where TURNO ='M' and SALARIO*12>2000000 and SALARIO*12<2250000;
--
select * 
from EMP 
where FECHA_ALT<'01/01/80' or FECHA_ALT>'12/12/82';
--
select * 
from DEPT 
where LOC='MADRID' or LOC='BARCELONA';





