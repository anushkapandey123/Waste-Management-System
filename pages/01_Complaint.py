import streamlit as st

import pandas as pd

st.title("PES1UG20CS072, PES1UG20CS073, PES1UG20CS106, PES1UG20CS123")
st.subheader("Complaint Details")
from database import view_all_data
import database as db
import plotly.express as px 

menu = ['Create  ✅','Read 👨‍💻','Update','Delete ❌']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create  ✅":
    st.subheader("Add complaints")
    col1,col2 = st.columns(2)

    with col1:
        uid = st.text_input("Enter User ID")

    with col2 :
        cid = st.text_input("Enter Complaint ID")
    msg = st.text_area("Complaint message")

    col3,col4 = st.columns(2)

    with col3:
        comp_date = st.date_input("Date")
    
    status = st.selectbox("Status",["Started","Being resolved","Resolved"])

    res_date = 'Null'
    if status == "Resolved":
        with col4:
            res_date = st.date_input("Enter resolved date")
            
    if st.button("Register Complaint"):
        db.add_data_complaint(cid,msg,status, comp_date, uid,res_date)
        st.success("Successfully added complaint no : {}".format(cid))

   
elif choice == "Read 👨‍💻":
    st.subheader("View complaints")
    result = view_all_data("complaint")
    df = pd.DataFrame(result, columns=['Complaint ID','Complaint msg','Status','Complaint Date','Complaint Resolved Date','User ID'])
    with st.expander("View all complaints"):
        st.dataframe(df)

    with st.expander("Complaint Status"):
        task_df = df['Status'].value_counts().to_frame()
			# st.dataframe(task_df)
        task_df = task_df.reset_index()
        st.dataframe(task_df)

        p1 = px.pie(task_df,names='index',values='Status')
        st.plotly_chart(p1,use_container_width=True)
        st.balloons()

    #my_bar = st.progress(0)

    #my_bar.progress(50)
        


    
elif choice == "Update":
    st.subheader("Update complaints")
    res = db.view_all_data('COMPLAINT')
 
    with st.expander("Current data"):
        df = pd.DataFrame(res,columns = ['Complaint ID','Complaint msg','Status','Complaint Date','Complaint Resolved Date','User ID'])
        st.dataframe(df)

    list_of_compl = [i[0] for i in db.view_unique('compl_id','COMPLAINT')]

    selected_compl = st.selectbox("Complaint Details to Edit",list_of_compl)
    

    selected_res = db.get_complaint(selected_compl)

  
    if selected_res:
        cid = selected_res[0][0]
        msg = selected_res[0][1]
        status = selected_res[0][2]
        compl_date = selected_res[0][3]
        res_date = selected_res[0][4]
        uid = selected_res[0][5]
    
        col1,col2 = st.columns(2)

        with col1:
            new_uid = st.text_input("Enter User ID",uid)

        with col2 :
            new_cid = st.text_input("Enter Complaint ID",cid)
        new_msg = st.text_area("Complaint message",msg)

        col3,col4 = st.columns(2)

        with col3:
            new_comp_date = st.date_input("Date",compl_date)
        
        new_status = st.selectbox("Status",["Started","Being resolved","Resolved"])

        new_res_date = st.date_input("Enter resolved date",res_date)    
        
        if st.button("Update Citizen"):
            
            db.edit_complaint_data(new_uid,new_cid ,new_msg,new_comp_date ,new_status,new_res_date,cid,uid)
            st.success("Successfully edited citizen : {}".format(uid))

    res2 = db.view_all_data('complaint')

    with st.expander("Updated data"):
        df2 = pd.DataFrame(res2,columns =['Complaint ID','Complaint msg','Status','Complaint Date','Complaint Resolved Date','User ID'])
        st.dataframe(df2)
    
elif choice == "Delete ❌":
    st.subheader("Delete complaints")
    
    with st.expander("View Data"):
        result = db.view_all_data('COMPLAINT')
        clean_df = pd.DataFrame(result,columns= ['Complaint ID','Complaint msg','Status','Complaint Date','Complaint Resolved Date','User ID'])
        st.dataframe(clean_df)

    unique_list = [(i[1],i[0]) for i in db.view_unique('compl_id,uid','COMPLAINT')]
    delete_by_task_name =  st.selectbox("Select Complaint",unique_list)
    if st.button("Delete"):
        db.delete_complaint(delete_by_task_name)
        st.warning("Deleted: '{}'".format(delete_by_task_name))

    with st.expander("Updated Data"):
        result = db.view_all_data('COMPLAINT')
        clean_df = pd.DataFrame(result,columns=  ['Complaint ID','Complaint msg','Status','Complaint Date','Complaint Resolved Date','User ID'])
        st.dataframe(clean_df)
