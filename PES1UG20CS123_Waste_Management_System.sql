create database pes1ug20cs123_project;
use pes1ug20cs123_project;
CREATE TABLE AREA (area_id varchar(15), name varchar(50), latitude float, longitude float, PRIMARY KEY(area_id));

CREATE TABLE TRUCK (v_no varchar(15), driver_name varchar(50), driver_no varchar(15),  PRIMARY KEY(v_no));


CREATE TABLE CITIZEN (aadhar_no varchar(15), name varchar(50), gender varchar(10), dob date, phno varchar(15), house_no varchar(15), street varchar(20), area varchar(50), city varchar(50),aid varchar(15),FOREIGN KEY(aid) REFERENCES AREA(area_id) ON DELETE CASCADE, PRIMARY KEY(aadhar_no,aid));


create table COMPLAINT (compl_id varchar(15), compl_msg varchar(255), compl_status varchar(25), compl_date date, compl_resolved_date date, uid varchar(15), FOREIGN KEY(uid) REFERENCES CITIZEN(aadhar_no) on delete cascade, PRIMARY KEY(compl_id,uid));
ALTER TABLE COMPLAINT ADD UNIQUE(compl_id);

create table WASTE (w_id varchar(15), non_bio_wt float,bio_wt float, c_date date, uid varchar(15),vid varchar(15), FOREIGN KEY(uid) REFERENCES CITIZEN(aadhar_no) on delete cascade, FOREIGN KEY(vid) REFERENCES truck(v_no) on delete cascade,PRIMARY KEY(w_id,uid));
ALTER TABLE WASTE ADD UNIQUE(w_id);

create table AreaHasATruck(area_id varchar(15), vid varchar(15), FOREIGN KEY(area_id) REFERENCES area(area_id) on delete cascade, FOREIGN KEY(vid) REFERENCES truck(v_no) on delete cascade,PRIMARY KEY(vid,area_id));
