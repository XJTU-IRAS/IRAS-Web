SELECT * FROM Course;
SELECT * FROM Student;
SELECT Sno 
FROM Student
GROUP BY Sno;
SELECT COUNT(DISTINCT Sno)
FROM Student;
 CREATE TABLE Grade(
 Cno VARCHAR (20)  REFERENCES Course(Cno),
 Sno VARCHAR (20) references Student(Sno),
 Sgrade Real ,
 primary key (Cno,Sno)
 );
 SELECT * FROM Grade;
 INSERT INTO Grade values ("12","22133",100);
 INSERT INTO Grade values ("142","21133",90);
 SELECT Student.*,Grade.* FROM Student,Grade 
 WHERE Student.Cno = Grade.Cno;
  SELECT Course.*,Student.*
 From Course ,Student
  Where Course.cno = student.cno;
  INSERT INTO COURSE VALUES("123","#123");
  SELECT Sname,S.Sno