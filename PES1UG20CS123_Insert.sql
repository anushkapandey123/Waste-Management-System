INSERT into AREA values
('A1','Banashankari',10.4,61.2),
('A2','Jayanagar',15.783,84.1),
('A3','Gandhi Bazar',20.4,70.4),
('A4','Rajajinagar',16.4,54.68),
('A5','Girinagar',18.46,78.4);

INSERT into TRUCK values 
('KA1234','Raju','12434979'),
('KA1454','Ram','458786456'),
('KA1657','Leela','4445716021'),
('KA2489','Alice','1284576048'),
('KA4857','Shivani','44587457869');

INSERT into CITIZEN values
('U1','Dhanu','Female','2002-11-01','9845678542','15','3rd Cross','Jayanagar','Bengaluru','A2' ),
('U2','Ram','Male','2002-07-27','9875846120','C78','5th Cross','Jayanagar','Bengaluru','A2'),
('U3','Raman','Male', '2001-11-28','8475626645', '12' ,'5 Main' ,'Girinagar' , 'Bengaluru' ,'A5'),
('U4','Rani','Female','2001-08-06','84756245687','65' ,'7th Main','Gandhi Bazar', 'Bengaluru' ,'A3'),
('U5','Sheela' ,'Female' ,'2003-09-06' , '45856245687', '7' , '2nd Main','Banashankari' ,'Bengaluru', 'A1');

INSERT into COMPLAINT values
('C1','Waste has not been collected since three days.', 'Resolved' ,'2022-11-21','2022-11-27', 'U1'),
( 'C2' ,'Collected waste has been dumped near the ground.','Resolved', '2022-11-21' ,'2022-11-28','U2'),
( 'C3' ,'Please collect both wet and dry waste.' , 'Resolved', '2022-11-21','2022-11-25', 'U1'),
( 'C4','Waste has not been collected.', 'Started' , '2022-11-28' , '0000-00-00','U4'),
( 'C5','Dry waste has not been collected since 4 days.', 'Being resolved' ,'2022-11-28' ,'0000-00-00', 'U5'),
( 'C6','Wet and dry waste has not been collected since 10 days.','Being resolved', '2022-11-25' ,'0000-00-00' ,'U2');

INSERT into WASTE values
('W1',5.04, 2,'2022-11-23', 'U1' ,'KA1234' ),
( 'W2' ,6.48, 2,'2022-11-28' ,'U1'  ,'KA1234' ),
( 'W3', 1.05 ,1 , '2022-11-27','U3' ,'KA1657'),
( 'W4',2.48 , 3.4,'2022-11-28' , 'U4'  , 'KA2489'),
('W5', 5.74 ,3.68,'2022-11-29' , 'U4', 'KA1454' ),
('W6', 10, 4, '2022-11-28' ,'U1', 'KA1234' ),
( 'W7', 3 ,4 ,'2022-11-28', 'U2'  , 'KA1234');


INSERT into AREAHASATRUCK (area_id,vid) values ( 'A2','KA1234' );

INSERT into AREAHASATRUCK values
('A4','KA1454'),
( 'A2','KA1657' ),
( 'A5' , 'KA2489' ),
( 'A3','KA4857');
