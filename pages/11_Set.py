import streamlit as st

import database as db
import pandas as pd
st.title("PES1UG20CS123")

choice = st.selectbox("Choice",["Set Operation 1","Set Operation 2","Set Operation 3"])

if choice == 'Set Operation 1':
    res = db.set()
    st.write("Finding the citizens who have registered complaint")
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Aadhar No'])
        st.dataframe(df)

if choice == 'Set Operation 2':
    res = db.set2()
    st.write("Finding the citizens who have not registered complaint")
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Aadhar No'])
        st.dataframe(df)

if choice == 'Set Operation 3':
    res = db.set3()
    st.write("Finding the citizens who have produced some waste")
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Aadhar No'])
        st.dataframe(df)
