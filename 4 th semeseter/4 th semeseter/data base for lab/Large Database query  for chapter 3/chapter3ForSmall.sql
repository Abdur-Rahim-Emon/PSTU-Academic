use smallRelationsInsertFile;
select course_id from teaches where semester='Fall' and year=2017 and course_id in 
(select course_id from teaches where semester='Spring' and year=2018 );
select * from instructor where name not in('Mozart' , 'Einstein');
select distinct name
                 from instructor
                 where  name not in ('Mozart', 'Einstein') ;
select count(distinct id )  from teaches where course_id='10101'; 
select salary ,name from instructor where salary> all
(select salary from instructor where dept_name='Biology');
select salary,name from instructor where salary> 
--(select max(salary) from instructor where dept_name='Biology');
  -- select course_id from section as S
 --  where semester = 'Fall' and year = 2017 and exists  (select * from section as T
  --   where semester = 'Spring' and year= 2018   and S.course_id = T.course_id);
  
     