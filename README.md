# OpenGauss JDBC

## For reference

### Effect looks like this


src/DBTest.java:

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

script/create_data.py

    INSERT INTO S249 VALUES
    (1033001, '陈或月', '男', '1999-11-08', 1.93, '西16舍163'),
    (1033004, '吕太接', '女', '2001-05-15', 1.46, '东3舍121'),
    (1033007, '郝德明', '男', '2000-04-25', 1.45, '东18舍137'),
    (1033010, '马种', '男', '1999-02-02', 1.47, '东7舍1718'),
    (1033013, '贺国加', '女', '1999-08-30', 1.68, '东8舍620'),
    (1033016, '于问文', '女', '1999-12-08', 1.94, '西10舍127'),
    (1033017, '孙几色', '男', '2000-08-01', 1.73, '西2舍612'),
    (1033020, '穆车写', '女', '1999-02-07', 1.69, '西15舍15'),
    (1033022, '奚往', '女', '2001-06-02', 1.66, '东4舍1915'),
    (1033025, '方从放', '女', '2000-04-30', 1.5, '西19舍192'),
    (1033028, '马下国', '女', '1999-06-30', 1.72, '西13舍35'),
    (1033029, '郝走拉', '女', '2000-01-29', 1.84, '西16舍1119'),
    (1033032, '姜比物', '女', '1999-09-03', 1.66, '西13舍1817'),
    (1033033, '金告就', '男', '2000-06-01', 1.62, '东15舍1620'),
    (1033036, '姜明立', '男', '1999-01-02', 1.91, '西16舍115'),
    (1033037, '任话样', '男', '2001-11-11', 1.71, '西15舍78'),
    (1033040, '冯着活', '女', '2001-12-27', 1.69, '西20舍1421'),
    (1033043, '穆望就', '女', '2000-03-26', 1.56, '西8舍172'),
    (1033045, '唐可德', '女', '2000-01-26', 1.47, '东7舍208'),
    (1033046, '柏太由', '女', '1999-06-22', 1.66, '东3舍164'),
    (1033049, '元所种', '男', '2000-03-20', 1.71, '西17舍717'),
    (1033051, '章走样', '女', '2001-02-17', 1.53, '西4舍1320'),
    (1033054, '韦英度', '女', '2001-08-03', 1.9, '东11舍1813'),
    (1033056, '郑界正', '女', '1999-03-22', 1.81, '东4舍186'),
    (1033057, '李此国', '男', '2001-02-22', 1.68, '西1舍919'),
    (1033060, '常国', '女', '1999-06-17', 1.6, '西8舍182'),
    (1033061, '邵常却', '男', '2000-11-25', 1.62, '东6舍182'),
    (1033062, '陶比', '女', '2001-05-23', 1.92, '东10舍920'),
    (1033063, '尤女门', '男', '2001-05-29', 1.46, '东15舍108'),
    (1033064, '唐世每', '男', '2000-02-01', 1.76, '西8舍49'),
    (1033065, '伍三尔', '女', '2001-05-31', 1.68, '东16舍47'),
    (1033068, '于母太', '男', '2001-07-04', 1.68, '西7舍208'),
    (1033071, '柳海口', '女', '2001-05-23', 1.92, '东9舍319'),
    (1033072, '昌表以', '女', '2000-06-28', 1.42, '东10舍182'),
    (1033073, '殷像出', '女', '1999-12-26', 1.75, '西10舍69'),
    (1033074, '鲍笑进', '男', '2000-11-19', 1.56, '西12舍821'),
    (1033076, '平出', '女', '2001-09-30', 1.56, '西12舍1811'),
    (1033079, '马使明', '女', '2001-10-12', 1.66, '西20舍420'),
    (1033081, '苗表', '男', '2001-08-06', 1.98, '西12舍1720'),
    (1033084, '平方马', '女', '2001-08-22', 1.73, '西1舍68'),
    (1033085, '尤地场', '女', '2001-04-14', 1.45, '西12舍1021'),
    (1033088, '卞写像', '男', '1999-04-05', 1.84, '西19舍73'),
    (1033089, '华并才', '女', '2001-03-05', 1.81, '东14舍518'),
    (1033091, '和日每', '男', '2001-08-28', 1.65, '西2舍113'),
    (1033092, '雷内两', '女', '2001-06-10', 1.8, '西8舍610'),
    (1033094, '乐力果', '女', '2000-03-02', 1.79, '东14舍12'),
    (1033096, '钱写字', '男', '2000-10-27', 1.48, '西3舍819'),
    (1033097, '苏比世', '女', '2001-03-01', 1.71, '东10舍89'),
    (1033100, '殷与样', '女', '2001-09-20', 1.5, '西13舍105'),
    (1033103, '尹会员', '男', '2000-08-15', 1.96, '东1舍1510'),
    (1033104, '元将表', '男', '2000-11-20', 1.81, '西4舍514'),
    (1033105, '朱记山', '男', '1999-04-28', 1.97, '西5舍206'),
    (1033107, '于头眼', '女', '1999-03-26', 1.56, '东11舍713'),
    (1033108, '马结书', '男', '1999-02-28', 1.93, '西17舍1715'),
    (1033110, '任些儿', '男', '2001-05-11', 1.42, '东18舍151'),
    (1033113, '时命字', '男', '1999-04-06', 1.98, '东6舍69'),
    (1033114, '余定处', '男', '2000-05-11', 1.64, '西10舍73'),
    (1033117, '陈记同', '女', '2001-06-27', 1.61, '东16舍193'),
    (1033119, '顾此性', '男', '2000-05-29', 2.0, '东9舍186'),
    (1033122, '许结神', '男', '2000-10-06', 1.75, '西6舍1219'),
    (1033123, '傅张那', '女', '2000-03-27', 1.89, '东4舍711'),
    (1033125, '费花手', '男', '2000-07-09', 1.65, '东14舍1911'),
    (1033128, '姚身下', '男', '1999-04-15', 1.7, '西20舍92'),
    (1033130, '康此年', '女', '1999-08-30', 1.9, '东10舍19'),
    (1033133, '苏明直', '女', '2001-09-19', 1.65, '西17舍1211'),
    (1033136, '于老岁', '男', '1999-04-28', 1.79, '东16舍816'),
    (1033137, '钱门活', '男', '1999-03-26', 1.82, '西16舍217'),
    (1033140, '范色第', '女', '2001-08-11', 1.91, '东8舍131'),
    (1033141, '鲍力情', '女', '1999-09-28', 1.87, '东7舍165'),
    (1033144, '廉中候', '女', '2001-11-26', 1.4, '东18舍75'),
    (1033147, '萧加新', '男', '1999-03-06', 1.52, '西6舍1313'),
    (1033148, '赵立文', '男', '1999-06-27', 1.5, '东8舍23'),
    (1033151, '俞想地', '女', '2001-10-05', 1.85, '东12舍1315'),
    (1033153, '汪也那', '女', '2001-10-02', 1.95, '东19舍1821'),
    (1033156, '李体两', '男', '2000-12-01', 1.81, '东5舍199'),
    (1033159, '顾世己', '女', '2000-07-30', 1.85, '西11舍208'),
    (1033161, '汤国位', '男', '2001-12-27', 1.41, '西11舍118'),
    (1033163, '周两它', '男', '2000-09-27', 1.73, '东14舍1311'),
    (1033166, '唐再场', '男', '1999-12-14', 1.98, '东12舍188'),
    (1033169, '周见十', '女', '2001-04-28', 1.55, '东19舍39'),
    (1033171, '俞张口', '女', '2001-12-17', 1.75, '西4舍79'),
    (1033173, '陈军', '男', '2000-04-23', 1.48, '西4舍26'),
    (1033176, '孟儿家', '男', '1999-01-18', 1.85, '东2舍108'),
    (1033177, '严那白', '男', '2001-05-04', 1.52, '东13舍1820'),
    (1033178, '傅望电', '女', '2001-12-09', 1.93, '东12舍1813'),
    (1033180, '秦克将', '女', '2000-08-09', 1.46, '东7舍102'),
    (1033183, '柳并给', '女', '2000-01-09', 1.43, '西1舍515'),
    (1033185, '昌气又', '男', '2000-04-13', 1.52, '西13舍68'),
    (1033188, '冯却很', '男', '2001-02-15', 1.83, '东1舍818'),
    (1033190, '史其像', '女', '2001-11-12', 1.45, '东1舍142'),
    (1033192, '陈许父', '女', '2001-06-25', 1.78, '东10舍1622'),
    (1033195, '柳民想', '男', '1999-12-15', 1.9, '西11舍214'),
    (1033198, '雷每', '男', '2000-06-18', 1.42, '东15舍191'),
    (1033200, '乐点文', '女', '1999-01-28', 1.92, '西9舍614'),
    (1033201, '谢真文', '女', '2000-03-11', 1.79, '东13舍112'),
    (1033203, '华全神', '女', '1999-03-25', 1.94, '东4舍1012'),
    (1033206, '鲍者加', '男', '2001-11-22', 1.55, '西2舍713'),
    (1033208, '戚子回', '女', '1999-11-27', 1.57, '东17舍149'),
    (1033209, '鲁体种', '男', '1999-10-23', 1.86, '东7舍1421'),
    (1033212, '孙立方', '男', '2000-12-31', 1.49, '东20舍81');
    
    
    INSERT INTO C249 VALUES
    ('EE-42', '经济电机课程', 56, 4.0, '俞再光'),
    ('HW-5', '电路学习', 48, 2.0, '戚少位'),
    ('CS-14', '爱情项目', 20, 2.0, '康感下'),
    ('HH-33', '电路经济基础', 28, 5.5, '章军太'),
    ('EE-20', '电路教学', 48, 2.0, '陈教代'),
    ('SC-80', '操作电路基础', 48, 6.0, '和母公'),
    ('AI-31', '经济电机教学', 28, 2.0, '尹所或'),
    ('SC-73', '电机深度课程', 32, 3.5, '褚并什'),
    ('HH-7', '操作操作教学', 56, 4.5, '邹因'),
    ('CS-80', '电机操作教学', 40, 6.0, '俞定西'),
    ('HH-25', '操作基础', 20, 3.5, '奚物情'),
    ('HW-81', '睡眠数据库教学', 32, 1.0, '穆次部'),
    ('AI-69', '项目', 20, 2.5, '安部友'),
    ('SC-28', '爱情基础', 44, 4.5, '陈主法'),
    ('HH-73', '经济学习', 40, 6.0, '窦至活'),
    ('SC-36', '操作教学', 44, 0.5, '金月又'),
    ('EE-58', '经济经济教学', 20, 1.5, '薛尔放'),
    ('SC-17', '数据库学习', 40, 1.5, '花样山'),
    ('SC-33', '电路经济学习', 52, 3.5, '伍方母'),
    ('HW-62', '电路经济教学', 56, 4.5, '唐什拉'),
    ('SC-63', '数据库电路学习', 24, 0.5, '卞活入'),
    ('AI-23', '睡眠操作教学', 48, 1.5, '卜行地'),
    ('AI-83', '经济爱情学习', 48, 2.0, '窦日老'),
    ('CS-67', '电路数据库基础', 52, 3.5, '何海马'),
    ('CS-45', '经济数据库学习', 36, 5.0, '平特直'),
    ('HH-38', '操作操作项目', 56, 3.0, '吴至日'),
    ('CS-29', '数据库学习', 40, 0.5, '堪着住'),
    ('AI-41', '数据库操作教学', 28, 5.5, '周车望'),
    ('HW-92', '经济电机基础', 20, 0.5, '罗爱德'),
    ('HH-17', '操作经济基础', 28, 0.5, '时相却'),
    ('HH-75', '电路深度教学', 28, 0.5, '韦至和'),
    ('CS-60', '爱情经济课程', 52, 1.5, '齐便母'),
    ('HH-45', '电机数据库学习', 24, 4.0, '陈许明'),
    ('HH-27', '经济深度课程', 44, 2.0, '秦关将'),
    ('HH-36', '睡眠课程', 52, 4.5, '余比每'),
    ('CS-63', '爱情电机项目', 20, 1.0, '罗它给'),
    ('SC-3', '电路教学', 44, 6.0, '钱十水'),
    ('AI-14', '操作电机项目', 52, 4.5, '廉动新'),
    ('AI-27', '数据库爱情基础', 52, 5.5, '毕处把'),
    ('CS-87', '数据库基础', 36, 1.5, '殷她玲'),
    ('AI-79', '电路爱情基础', 44, 0.5, '魏地为'),
    ('AI-88', '经济爱情课程', 36, 6.0, '水此张'),
    ('SC-62', '爱情爱情项目', 40, 2.0, '孙国许'),
    ('HW-33', '经济项目', 36, 0.5, '罗头别'),
    ('SC-50', '操作深度教学', 56, 3.5, '邵果次'),
    ('EE-96', '经济睡眠教学', 52, 4.0, '王面芳'),
    ('HH-79', '电路课程', 24, 2.5, '昌情感'),
    ('HH-100', '电机项目', 44, 3.0, '窦孩些'),
    ('HH-48', '操作电机项目', 36, 2.5, '傅口声'),
    ('AI-4', '电机电路学习', 20, 4.0, '昌难');
    
    
    INSERT INTO SC249 VALUES
    (1033060, 'HH-75', 63.0),
    (1033081, 'CS-45', 74.0),
    (1033061, 'SC-50', 72.0),
    (1033107, 'SC-33', 53.0),
    (1033073, 'EE-20', 53.5),
    (1033169, 'AI-4', 78.5),
    (1033161, 'AI-79', 53.5),
    (1033028, 'SC-33', 57.0),
    (1033092, 'EE-20', 65.0),
    (1033133, 'HW-62', 60.5),
    (1033032, 'HW-5', 96.5),
    (1033062, 'CS-29', 69.0),
    (1033161, 'CS-80', 80.0),
    (1033028, 'HH-45', 41.0),
    (1033074, 'AI-79', 61.0),
    (1033148, 'HH-36', 95.0),
    (1033104, 'HH-7', 93.0),
    (1033166, 'SC-28', 54.5),
    (1033178, 'HH-17', 60.0),
    (1033063, 'HW-92', 59.0),
    (1033091, 'SC-17', 74.5),
    (1033200, 'CS-80', 57.0),
    (1033208, 'AI-69', 77.0),
    (1033113, 'HW-5', 67.5),
    (1033100, 'HH-7', 71.5),
    (1033110, 'HH-100', 94.0),
    (1033103, 'AI-27', 94.5),
    (1033072, 'AI-23', 85.5),
    (1033128, 'AI-69', 64.0),
    (1033013, 'CS-67', 91.5),
    (1033144, 'HH-27', 44.5),
    (1033190, 'HH-79', 54.5),
    (1033144, 'AI-69', 88.0),
    (1033092, 'HH-38', 57.0),
    (1033079, 'SC-17', 97.5),
    (1033032, 'HH-27', 63.0),
    (1033198, 'SC-3', 85.5),
    (1033163, 'HW-81', 64.0),
    (1033045, 'SC-80', 71.0),
    (1033091, 'HH-45', 62.0),
    (1033173, 'SC-50', 40.0),
    (1033032, 'EE-58', 88.0),
    (1033054, 'AI-31', 73.0),
    (1033105, 'HH-73', 53.5),
    (1033161, 'HH-27', 68.5),
    (1033123, 'HW-5', 79.0),
    (1033033, 'CS-80', 40.0),
    (1033049, 'CS-63', 68.5),
    (1033043, 'SC-33', 77.0),
    (1033037, 'AI-4', 77.5),
    (1033123, 'CS-60', 46.0),
    (1033017, 'SC-73', 58.5),
    (1033049, 'SC-80', 93.0),
    (1033028, 'AI-31', 93.5),
    (1033054, 'CS-67', 98.0),
    (1033113, 'HW-33', 58.0),
    (1033040, 'CS-63', 48.0),
    (1033212, 'CS-87', 79.5),
    (1033117, 'AI-27', 81.5),
    (1033071, 'SC-80', 61.0),
    (1033064, 'CS-87', 79.5),
    (1033092, 'SC-62', 95.5),
    (1033161, 'AI-31', 98.0),
    (1033040, 'AI-88', 81.0),
    (1033110, 'HH-45', 68.5),
    (1033153, 'HH-36', 88.0),
    (1033079, 'CS-87', 52.5),
    (1033178, 'CS-45', 41.5),
    (1033097, 'CS-14', 98.0),
    (1033113, 'HH-33', 67.0),
    (1033133, 'SC-62', 96.5),
    (1033201, 'SC-80', 92.0),
    (1033045, 'HW-92', 51.0),
    (1033020, 'CS-67', 68.0),
    (1033057, 'AI-31', 70.5),
    (1033061, 'AI-79', 52.0),
    (1033094, 'HH-75', 42.5),
    (1033010, 'EE-42', 58.0),
    (1033156, 'SC-36', 77.5),
    (1033076, 'HH-17', 51.5),
    (1033166, 'SC-62', 91.0),
    (1033071, 'SC-17', 82.0),
    (1033022, 'AI-41', 76.0),
    (1033103, 'HW-33', 81.5),
    (1033110, 'CS-29', 46.5),
    (1033130, 'CS-67', 65.0),
    (1033057, 'SC-17', 68.5),
    (1033166, 'AI-31', 40.5),
    (1033159, 'HH-79', 42.5),
    (1033110, 'HH-79', 80.5),
    (1033062, 'AI-69', 84.0),
    (1033156, 'EE-58', 40.5),
    (1033100, 'AI-31', 72.0),
    (1033079, 'AI-31', 96.5),
    (1033029, 'CS-14', 70.0),
    (1033171, 'AI-88', 63.5),
    (1033108, 'CS-29', 57.5),
    (1033096, 'EE-42', 79.5),
    (1033144, 'SC-73', 79.0),
    (1033028, 'SC-73', 66.5),
    (1033206, 'HH-45', 71.0),
    (1033060, 'SC-17', 63.5),
    (1033016, 'CS-67', 71.0),
    (1033107, 'SC-62', 57.0),
    (1033144, 'SC-80', 77.5),
    (1033208, 'AI-27', 75.0),
    (1033028, 'SC-50', 50.0),
    (1033094, 'EE-20', 78.0),
    (1033051, 'EE-42', 96.5),
    (1033060, 'HH-45', 96.0),
    (1033049, 'AI-88', 52.0),
    (1033097, 'HH-100', 65.5),
    (1033148, 'HH-38', 67.5),
    (1033073, 'SC-3', 96.0),
    (1033178, 'HH-27', 62.5),
    (1033072, 'SC-3', 57.0),
    (1033169, 'AI-79', 51.0),
    (1033130, 'AI-23', 41.0),
    (1033065, 'AI-31', 50.0),
    (1033071, 'AI-83', 65.0),
    (1033085, 'CS-29', 44.0),
    (1033173, 'EE-58', 63.5),
    (1033100, 'CS-80', 43.5),
    (1033180, 'HH-38', 59.5),
    (1033049, 'SC-36', 58.5),
    (1033073, 'HH-25', 87.0),
    (1033105, 'SC-80', 85.5),
    (1033209, 'SC-3', 69.5),
    (1033198, 'HH-27', 95.5),
    (1033104, 'HH-100', 89.0),
    (1033071, 'HH-73', 71.5),
    (1033089, 'SC-63', 65.5),
    (1033208, 'CS-67', 75.0),
    (1033200, 'CS-14', 87.5),
    (1033148, 'AI-88', 90.0),
    (1033173, 'AI-41', 45.0),
    (1033212, 'HH-79', 54.0),
    (1033076, 'HH-36', 59.5),
    (1033209, 'EE-20', 87.5),
    (1033159, 'AI-31', 67.5),
    (1033092, 'AI-14', 44.5),
    (1033188, 'HH-79', 75.0),
    (1033051, 'SC-33', 82.0),
    (1033183, 'AI-14', 96.0),
    (1033195, 'CS-29', 50.0),
    (1033037, 'SC-33', 58.5),
    (1033081, 'HH-25', 50.0),
    (1033200, 'CS-45', 53.0),
    (1033183, 'CS-14', 59.0),
    (1033063, 'AI-88', 66.0),
    (1033125, 'HH-25', 69.0),
    (1033163, 'SC-17', 50.5),
    (1033073, 'HH-45', 69.0),
    (1033100, 'CS-67', 90.0),
    (1033113, 'CS-87', 43.5),
    (1033065, 'HW-81', 91.0),
    (1033051, 'CS-87', 77.0),
    (1033029, 'AI-31', 65.0),
    (1033107, 'AI-88', 56.0),
    (1033064, 'SC-33', 74.5),
    (1033137, 'CS-29', 77.0),
    (1033185, 'HW-33', 94.0),
    (1033061, 'CS-45', 95.0),
    (1033092, 'HH-79', 96.5),
    (1033209, 'HH-36', 61.5),
    (1033081, 'HW-62', 45.0),
    (1033183, 'HH-36', 76.0),
    (1033140, 'CS-63', 96.5),
    (1033097, 'CS-67', 69.0),
    (1033097, 'AI-83', 57.0),
    (1033203, 'HW-81', 98.0),
    (1033063, 'HH-25', 73.5),
    (1033208, 'SC-33', 55.5),
    (1033180, 'HH-73', 99.0),
    (1033200, 'SC-62', 91.0),
    (1033166, 'HH-45', 59.5),
    (1033043, 'HH-45', 48.5),
    (1033076, 'CS-45', 72.0),
    (1033081, 'EE-42', 42.0),
    (1033198, 'HW-81', 90.0),
    (1033061, 'AI-88', 55.5),
    (1033107, 'CS-14', 58.0),
    (1033125, 'AI-88', 72.0),
    (1033169, 'HW-92', 98.5),
    (1033133, 'HH-25', 85.5),
    (1033076, 'HH-100', 98.5),
    (1033190, 'EE-42', 56.0),
    (1033032, 'HW-62', 83.5),
    (1033123, 'HW-92', 64.0),
    (1033208, 'AI-83', 84.0),
    (1033068, 'CS-29', 56.0),
    (1033062, 'SC-62', 54.5),
    (1033036, 'HH-36', 91.0),
    (1033074, 'CS-87', 67.5),
    (1033089, 'CS-67', 74.0),
    (1033060, 'SC-50', 73.5),
    (1033163, 'SC-62', 53.0),
    (1033133, 'CS-60', 63.0),
    (1033103, 'HH-45', 73.0),
    (1033130, 'CS-60', 53.5);
