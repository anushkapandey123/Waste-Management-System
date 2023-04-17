import mysql.connector
mydb = mysql.connector.connect(
host="database-2.cjueszsg36jc.us-east-1.rds.amazonaws.com",
user="admin",
database="pes1ug20cs123_project"
)
c = mydb.cursor()
import streamlit as st


import pandas as pd
 

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS AREA(aid TEXT, name TEXT, latitude TEXT,longitude TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS TRUCK(uid TEXT, driver_name TEXT, driver_no TEXT)")

def add_data_area(aid,aname,lat,long):
    c.execute('INSERT INTO AREA(area_id, name ,latitude ,longitude ) VALUES (%s,%s,%s,%s)',(aid,aname,lat,long))
    mydb.commit()

def add_data(vid,driver_name,driver_no):
    c.execute('INSERT INTO TRUCK(v_no , driver_name , driver_no ) VALUES (%s,%s,%s)',(vid,driver_name,driver_no))
    mydb.commit()

def add_data_citizen(uid,name,gender,dob,phno,house_no,street,area_name,city,aid):
    c.execute('INSERT INTO CITIZEN(aadhar_no , name , gender , dob , phno , house_no , street , area, city ,aid ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(uid,name,gender,dob,phno,house_no,street,area_name,city,aid))
    mydb.commit()

def add_data_complaint(cid,msg,status, comp_date,uid, res_date= ' '):
    c.execute('INSERT INTO COMPLAINT(compl_id , compl_msg , compl_status , compl_date , compl_resolved_date , uid ) VALUES (%s,%s,%s,%s,%s,%s)',(cid,msg,status,comp_date, res_date,uid))
    mydb.commit()

def add_data_waste(wid,non_bio_wt,bio_wt,uid,c_date,vid):
    c.execute('INSERT INTO WASTE(w_id,non_bio_wt,bio_wt, c_date,uid,vid ) VALUES (%s,%s,%s,%s,%s,%s)',(wid,non_bio_wt,bio_wt,c_date,uid,vid))
    mydb.commit()

def add_data_area_truck(aid,vid):
    c.execute('INSERT INTO AreaHasATruck(area_id,vid ) VALUES (%s,%s)',(aid,vid))
    mydb.commit()

def view_all_data(name):
    c.execute(f'SELECT * FROM {name}')
    data = c.fetchall()
    return data


def view_unique(key,name):
    c.execute(f'SELECT DISTINCT {key} from {name}')
    data = c.fetchall()
    return data



def get_area(area_id):
	c.execute('SELECT * FROM AREA WHERE area_id="{}"'.format(area_id))
	data = c.fetchall()
	return data

def get_citizen(uid):
	c.execute('SELECT * FROM CITIZEN WHERE aadhar_no="{}"'.format(uid))
	data = c.fetchall()
	return data

def get_complaint(cid):
    c.execute('SELECT * FROM COMPLAINT WHERE compl_id="{}"'.format(cid))
    data = c.fetchall()
    return data

def get_truck(vid):
    c.execute('SELECT * FROM TRUCK WHERE v_no="{}"'.format(vid))
    data = c.fetchall()
    return data

def get_area_truck(vid):
    c.execute('SELECT * FROM AreaHasATruck WHERE vid="{}"'.format(vid))
    data = c.fetchall()
    return data

def get_waste(wid):
    c.execute('SELECT * FROM WASTE WHERE w_id="{}"'.format(wid))
    data = c.fetchall()
    return data

def edit_task_data(new_aid,new_aname,new_lat,new_long,aid,aname,lat,long):
	c.execute("UPDATE AREA SET area_id = %s,name= %s,latitude= %s,longitude= %s WHERE area_id =%s ",(new_aid,new_aname,new_lat,new_long,aid))
	
	mydb.commit()
	#data = c.fetchall()
	#return data

def edit_citizen_data(new_uid,new_name ,new_gender ,new_dob,new_phno,new_house_no ,new_street,new_area_name ,new_city ,new_aid ,uid):
	c.execute("UPDATE CITIZEN SET aadhar_no = %s , name = %s , gender = %s , dob = %s , phno = %s , house_no = %s , street = %s , area = %s, city = %s ,aid = %s WHERE aadhar_no =%s ",(new_uid,new_name ,new_gender ,new_dob,new_phno,new_house_no ,new_street,new_area_name ,new_city ,new_aid ,uid))
	mydb.commit()

def edit_complaint_data(new_uid,new_cid ,new_msg,new_comp_date ,new_status,new_res_date,cid,uid):
    c.execute("UPDATE COMPLAINT SET compl_id = %s , compl_msg = %s , compl_status = %s , compl_date  = %s , compl_resolved_date = %s , uid = %s WHERE compl_id = %s and uid = %s  ",(new_cid ,new_msg,new_status,new_comp_date,new_res_date,new_uid,cid,uid))
    mydb.commit()

def edit_truck_data(new_vid,new_driver_name,new_driver_no,vid,name,phno):
    c.execute("UPDATE TRUCK SET v_no = %s , driver_name = %s , driver_no = %s WHERE v_no =%s ",(new_vid,new_driver_name,new_driver_no,vid))
    mydb.commit()

def edit_waste_data(new_wid,new_non_bio_wt,new_bio_wt,new_c_date,new_uid,new_vid,wid,uid,vid):
    c.execute("UPDATE WASTE SET w_id = %s , non_bio_wt = %s , bio_wt = %s ,c_date = %s , uid  = %s , vid = %s WHERE w_id = %s and uid = %s and vid = %s",(new_wid,new_non_bio_wt,new_bio_wt,new_c_date,new_uid,new_vid,wid,uid,vid))
    mydb.commit()

def edit_area_truck_data(new_aid,new_vid,aid,vid):
    c.execute("UPDATE AreaHasATruck SET area_id = %s , vid = %s WHERE area_id = %s and vid = %s",(new_aid,new_vid,aid,vid))
    mydb.commit()


def delete_data(area_id):
    c.execute('DELETE FROM AREA where area_id ="{}"'.format(area_id))
    mydb.commit()

def delete_citizen(uid):
    c.execute('DELETE FROM CITIZEN where aadhar_no ="{}"'.format(uid))
    mydb.commit()

def delete_complaint(cid):
    c.execute(f'DELETE FROM COMPLAINT where compl_id ="{cid[1]}" and uid ="{cid[0]}"')
    mydb.commit()

def delete_truck(vid):
    c.execute('DELETE FROM TRUCK where v_no ="{}"'.format(vid))
    mydb.commit()
 
def delete_waste(wid):
    c.execute('DELETE FROM WASTE where w_id ="{}"'.format(wid))
    mydb.commit()

def delete_area_truck(vid):
    c.execute('DELETE FROM WASTE where vid ="{}"'.format(vid))
    mydb.commit()


def sql_query(qry):
    c.execute(qry)
    data = c.fetchall()
    return data

def sql_query_upd(qry):
    c.execute(qry)
    mydb.commit()

def agg1():
    c.execute('SELECT uid,COUNT(compl_id) FROM COMPLAINT group by uid')
    data = c.fetchall()
    return data

def agg2():
    c.execute('SELECT aid,COUNT(aadhar_no) FROM CITIZEN group by aid order by aid')
    data = c.fetchall()
    return data

def agg3():
    c.execute('select c_date,uid,max(non_bio_wt) from WASTE group by c_date;')
    data = c.fetchall()
    return data


def agg4():
    c.execute('select uid,sum(non_bio_wt),sum(bio_wt) from WASTE group by uid')
    data = c.fetchall()
    return data

'''def create_procedure():
    c.execute('SOURCE C:/Users/DEVIKA S/Documents/DBMS LAB/PROJECT/procedure.sql')
    mydb.commit()
'''

def procedure(wid):
    c.execute(f'CALL totalwaste("{wid}", @total);' )
    c.execute('SELECT @total;')
    data = c.fetchall()
    return data

def function():
    c.execute('select uid,organic_user(bio_wt,non_bio_wt) from WASTE' )
    data = c.fetchall()
    return data

def function1():
    c.execute('select  compl_id,uid,compl_resolved_date,resolved_date(compl_resolved_date) from COMPLAINT' )
    data = c.fetchall()
    return data

def join1():
    c.execute(' select * from AREA inner join citizen on area_id = aid' )
    data = c.fetchall()
    return data


def join2():
    c.execute('select * from COMPLAINT inner join citizen on uid = aadhar_no' )
    data = c.fetchall()
    return data

def set():
    c.execute('(select uid from COMPLAINT) intersect (select aadhar_no from CITIZEN)')
    data = c.fetchall()
    return data


def set2():
    c.execute('(select uid from COMPLAINTS) except (select aadhar_no from CITIZEN)')
    data = c.fetchall()
    return data

def set3():
    c.execute('(select uid from WASTE) intersect (select aadhar_no from CITIZEN)')
    data = c.fetchall()
    return data
