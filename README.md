# OpenGauss JDBC

## For reference

## Effect looks like this
Jun 08, 2022 6:15:22 PM org.postgresql.core.v3.ConnectionFactoryImpl openConnectionImpl
INFO: [a85e2185-e799-490e-9860-75368f40aaca] Try to connect. IP: localhost:5432
Jun 08, 2022 6:15:22 PM org.postgresql.core.v3.ConnectionFactoryImpl openConnectionImpl
INFO: [127.0.0.1:52572/ocalhost/127.0.0.1:5432] Connection is established. ID: a85...
Jun 08, 2022 6:15:22 PM org.postgresql.core.v3.ConnectionFactoryImpl openConnectionImpl
INFO: Connect complete. ID: a85...
Connection succeed!
DROP VIEW IF EXISTS V1; 
DROP VIEW IF EXISTS V2; 
DROP VIEW IF EXISTS V3; 
 DROP TABLE IF EXISTS SC249; 
DROP TABLE IF EXISTS S249; 
DROP TABLE IF EXISTS C249; 
CREATE TABLE IF NOT EXISTS S249 (Sno Integer PRIMARY KEY, Sname VARCHAR(32), Sex Char(4), BDATE Date, Height Number, Dorm VARCHAR(32)); 
CREATE TABLE IF NOT EXISTS C249 (Cno VARChar(16) PRIMARY KEY, Cname VARCHAR(32), Period Integer, Credit Float, Teacher VARCHAR(32)); 
CREATE TABLE IF NOT EXISTS SC249 (Sno Integer, Cno VARChar(16), Grade Number,     PRIMARY KEY(Sno, Cno), Foreign Key(Sno) references S249(Sno), Foreign Key(Cno) references C249(Cno)); 
INSERT INTO S249 VALUES (1032010,'王涛','男','2002-4-5',1.72,'东14舍221'), (1032023,'孙文','男','2003-6-10',1.8,'东14舍221'), (1032001,'张晓梅','女','2003-11-17',1.58,'东1舍312'), (1032005,'刘静','女','2002-1-10',1.63,'东1舍312'), (1032112,'董蔚','男','2003-12-20',1.71,'东14舍221'), (3031011,'王倩','女','2002-2-20',1.66,'东2舍104'), (3031014,'赵思扬','男','2001-6-6',1.85,'东18舍421'), (3031051,'周剑','男','2001-5-8',1.68,'东18舍422'), (3031009,'田婷','女','2002-8-11',1.6,'东2舍104'), (3031033,'蔡明明','男','2002-3-12',1.75,'东18舍423'), (3031056,'曹子衿','女','2003-12-15',1.65,'东2舍305'); 
  INSERT INTO C249 VALUES ('CS-01','数据结构',60,3,'张军'), ('CS-02','计算机组成原理',80,4,'王亚伟'), ('CS-04','人工智能',40,2,'李蕾'), ('CS-05','深度学习',40,2,'崔均'), ('EE-01','信号与系统',60,3,'张明'), ('EE-02','数字逻辑电路',100,5,'胡海东'), ('EE-03','光电子学与光子学',40,2,'石韬'); 
 INSERT INTO SC249 VALUES (1032010,'CS-01',82), (1032010,'CS-02',91), (1032010,'CS-04',83.5), (1032001,'CS-01',77.5), (1032001,'CS-02',85), (1032001,'CS-04',83), (1032005,'CS-01',62), (1032005,'CS-02',77), (1032005,'CS-04',82), (1032023,'CS-01',55), (1032023,'CS-02',81), (1032023,'CS-04',76), (1032112,'CS-01',88), (1032112,'CS-02',91.5), (1032112,'CS-04',86), (1032112,'CS-05',NULL), (3031033,'EE-01',93), (3031033,'EE-02',89), (3031009,'EE-01',88), (3031009,'EE-02',78.5), (3031011,'EE-01',91), (3031011,'EE-02',86), (3031051,'EE-01',78), (3031051,'EE-02',58), (3031014,'EE-01',79), (3031014,'EE-02',71); 
=======================================
Executing SELECT Cno, Cname FROM C249 WHERE Cno LIKE CONCAT('EE', '%'); :
EE-01,信号与系统,
EE-02,数字逻辑电路,
EE-03,光电子学与光子学,
=======================================
