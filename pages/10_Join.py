import streamlit as st

import database as db
import pandas as pd
st.title("PES1UG20CS123")

choice = st.selectbox("Choice",["Join 1","Join 2"])

if choice == 'Join 1':
    res = db.join1()
    st.write("Join AREA and CITIZEN on area id")
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Area ID','Area_Name','Latitude','Longitude','Aadhar No','Name','Gender','dob','Phno','House_no','Street','Area_name','City','Area_ID'])
        st.dataframe(df)

if choice == 'Join 2':
    res = db.join2()
    st.write("Join COMPLAINT and CITIZEN on aadhar no")
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Complaint ID','Complaint msg','Status','Complaint Date','Complaint Resolved Date','User ID','Aadhar No','Name','Gender','dob','Phno','House_no','Street','Area_name','City','Area ID'])
        st.dataframe(df)


