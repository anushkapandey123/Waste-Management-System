import streamlit as st
import database as db
import pandas as pd

st.title("PES1UG20CS123")
st.subheader("SQL Queries")


sel = st.text_input("Enter select SQL query")

if st.button("Execute"):
        res = db.sql_query(sel)
    
        with st.expander("View all"):
            df = pd.DataFrame(res)
            st.dataframe(df)


upd = st.text_input("Enter update/delete SQL query",key=5)

if st.button("Execute",key=6):
        if upd == '':
            st.error("Please enter query")
        db.sql_query_upd(upd)
        
        st.write("Successfully executed")
            