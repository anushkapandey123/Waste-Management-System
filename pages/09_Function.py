import streamlit as st
import database as db
st.title("PES1UG20CS123")
st.subheader("Functions")
import pandas as pd
import plotly.express as px 
#db.create_procedure()




choice = st.selectbox("Choice",["Function 1","Function 2"])

if choice == 'Function 1':
    st.write("This function tells us if a complaint has been resolved yet based on the current date and resolved date.")
    if st.button("Execute function"):
        res = db.function1()
        
        with st.expander("View all"):
            df = pd.DataFrame(res,columns = ['Complaint ID','User ID','Resolved Date','Func o/p - Resolved or being resolved'])
            st.dataframe(df)
        with st.expander("Complaint Status"):
            task_df = df['Func o/p - Resolved or being resolved'].value_counts().to_frame()
                # st.dataframe(task_df)
            task_df = task_df.reset_index()
            st.dataframe(task_df)

            p1 = px.pie(task_df,names='index')
            #st.plotly_chart(p1,use_container_width=True)

if choice == 'Function 2':
    st.write("This function tells us if a citizen generates more bio-degradable or more non-biodegradable waste.")
    if st.button("Execute function"):
        res = db.function()
        with st.expander("View all"):
            df = pd.DataFrame(res,columns = ['User ID','Inference'])
            st.dataframe(df)
       
    
        