import streamlit as st
import webbrowser

st.title("PES1UG20CS123")
st.subheader("Waste Details")

import database as db
import pandas as pd


menu = ['Create ✅','Read','Update','Delete ❌']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create ✅":
    st.subheader("Add waste details")
    col1,col2 = st.columns(2)

    with col1:
        wid = st.text_input("Enter Waste ID")
        non_bio_wt = st.number_input("Enter weight of non-biodegradable waste",step = 1.0)
        
    with col2 :
        uid = st.text_input("Enter User ID")
        bio_wt = st.number_input("Enter weight of biodegradable waste",step = 1.0)
    
    col3,col4 = st.columns(2)

    with col3:
        c_date = st.date_input("Date")
    
    with col4:
        vid = st.text_input("Enter Truck No/ID")

    if st.button("Register Waste"):
        try:
            db.add_data_waste(wid,non_bio_wt,bio_wt,uid,c_date,vid)
        except:
            st.error(f"POP UP!! THIS IS A TRIGGER! Send an email to citizen {uid} that non-biodegradable waste is greater",icon="🚨")
            


            url = 'http://localhost:8501/Error'
            webbrowser.open_new_tab(url)
            e = RuntimeError('This is an POP UP of type RuntimeError - Non-biodegradable waste is greater than limit')
            st.exception(e)
        else:
            st.success("Successfully added waste  : {}".format(wid))
       
   
elif choice == "Read":

    st.subheader("View Waste")
    res = db.view_all_data('WASTE')
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Waste ID','Non-bio Weight','Bio Weight','Date','User ID','Truck No'])
        st.dataframe(df)
    
elif choice == "Update":
    st.subheader("Update waste details")
    res = db.view_all_data('WASTE')
   

    with st.expander("Current data"):
        df = pd.DataFrame(res,columns = ['Waste ID','Non-bio Weight','Bio Weight','Date','User ID','Truck No'])
        st.dataframe(df)

    list = [i[0] for i in db.view_unique('w_id','WASTE')]

    selected = st.selectbox("Waste to Edit",list)

    selected_res = db.get_waste(selected)

    if selected_res:
        wid = selected_res[0][0]
        non_bio_wt = selected_res[0][1]
        bio_wt = selected_res[0][2]
        date = selected_res[0][3]
        uid = selected_res[0][4]
        vid = selected_res[0][5]

        col1,col2 = st.columns(2)

        with col1:
            new_wid = st.text_input("Enter Waste ID",wid)
            new_non_bio_wt = st.number_input("Enter weight of non-biodegradable waste",non_bio_wt,step = 1.0)

        with col2 :
            new_uid = st.text_input("Enter User ID",uid)
            new_bio_wt = st.number_input("Enter weight of biodegradable waste",bio_wt,step = 1.0)
        
        col3,col4 = st.columns(2)

        with col3:
            new_c_date = st.date_input("Date",date)
        
        with col4:
            new_vid = st.text_input("Enter Truck No/ID",vid)

        if st.button("Update Waste Details"):
            
            db.edit_waste_data(new_wid,new_non_bio_wt,new_bio_wt,new_c_date,new_uid,new_vid,wid,uid,vid)
            st.success("Successfully edited area : {}".format(wid))

    res2 = db.view_all_data('waste')

    with st.expander("Updated data"):
        df2 = pd.DataFrame(res2,columns = ['Waste ID','Non-bio Weight','Bio Weight','Date','User ID','Truck No'])
        st.dataframe(df2)

elif choice == "Delete ❌":
    st.subheader("Delete Waste Details")

    with st.expander("View Data"):
        result = db.view_all_data('WASTE')
        clean_df = pd.DataFrame(result,columns= ['Waste ID','Non-bio Weight','Bio Weight','Date','User ID','Truck No'])
        st.dataframe(clean_df)

    unique_list = [i[0] for i in db.view_unique('w_id','WASTE')]
    delete_by_task_name =  st.selectbox("Select",unique_list)
    if st.button("Delete"):
        db.delete_waste(delete_by_task_name)
        st.warning("Deleted: '{}'".format(delete_by_task_name))

    with st.expander("Updated Data"):
        result = db.view_all_data('WASTE')
        clean_df = pd.DataFrame(result,columns= ['Waste ID','Non-bio Weight','Bio Weight','Date','User ID','Truck No'])
        st.dataframe(clean_df)