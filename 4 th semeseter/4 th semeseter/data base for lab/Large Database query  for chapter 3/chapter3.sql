use largeRelationsInsertFile;
select * from instructor;
select course_id from teaches where semester='Fall' and year=2017 and course_id in 
(select course_id from teaches where semester='Spring' and year=2018 );
select count(distinct id )  from teaches where course_id='10101'; 
SELECT COUNT(DISTINCT ID) FROM takes
WHERE (course_id, sec_id, semester, year) IN (
    SELECT course_id, sec_id, semester, year
    FROM teaches
    WHERE teaches.ID = 10101
);
select count(distinct id) from takes where
(select id from instructor where id='10101');


select count(distinct i.name)   from instructor as i,instructor as i1 where
i.salary>(i1.salary and i1.dept_name='Biology');

select count(distinct name) from instructor where salary> some
(select salary from instructor where dept_name='Biology');