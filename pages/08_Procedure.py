import streamlit as st
import database as db
st.title("PES1UG20CS123")
st.subheader("Stored procedure")
import pandas as pd

#db.create_procedure()

st.write("This stored procedure returns the sum of biodegradable and non-biodegradable waste given a waste id")

entered_wid = st.text_input("Enter waste ID")
if st.button("Call procedure"):
    res = db.procedure(entered_wid)
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Total Weight'])
        st.dataframe(df)