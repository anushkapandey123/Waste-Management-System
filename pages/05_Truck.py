import streamlit as st
import database as db
st.title("PES1UG20CS123")
st.subheader("Truck Details")
import pandas as pd


menu = ['Create ✅','Read','Update','Delete ❌']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create ✅":
    st.subheader("Add trucks")

    col1,col2 = st.columns(2)

    with col1:
        vid = st.text_input("Enter Vehicle ID")

    #with col2:
        #st.camera_input("QR")
    
    driver_name = st.text_input("Driver Name")

    driver_no = st.text_input("Driver Phone No")
    if st.button("Register Vehicle"):
        db.add_data(vid,driver_name,driver_no)
        st.success("Successfully added vehicle no : {}".format(vid))
        
   
elif choice == "Read":
    st.subheader("View vehicles/trucks")
    res = db.view_all_data('TRUCK')
    
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Vehicle No','Name','Phone No'])
        st.dataframe(df)
    
elif choice == "Update":
    st.subheader("Update trucks")
    res = db.view_all_data('TRUCK')

    with st.expander("Current data"):
        df = pd.DataFrame(res,columns =  ['Vehicle No','Name','Phone No'])
        st.dataframe(df)

    list_of_trucks= [i[0] for i in db.view_unique('v_no','TRUCK')]

    selected_truck = st.selectbox("Trucks to Edit",list_of_trucks)

    selected_res = db.get_truck(selected_truck)

    if selected_res:
        vid = selected_res[0][0]
        name = selected_res[0][1]
        phno = selected_res[0][2]
        

        col1,col2 = st.columns(2)

        with col1:
            new_vid = st.text_input("Enter Vehicle ID",vid)

        #with col2:
            #st.camera_input("QR")
        
        new_driver_name = st.text_input("Driver Name",name)

        new_driver_no = st.text_input("Driver Phone No",phno)

        if st.button("Update Truck"):
            
            db.edit_truck_data(new_vid,new_driver_name,new_driver_no,vid,name,phno)
            st.success("Successfully edited truck : {}".format(vid))

    res2 = db.view_all_data('TRUCK')

    with st.expander("Updated data"):
        df2 = pd.DataFrame(res2,columns =  ['Vehicle No','Name','Phone No'])
        st.dataframe(df2)
    
elif choice == "Delete ❌":
    st.subheader("Delete trucks")
    with st.expander("View Data"):
        result = db.view_all_data('TRUCK')
        clean_df = pd.DataFrame(result,columns= ['Vehicle No','Name','Phone No'])
        st.dataframe(clean_df)

    unique_list = [i[0] for i in db.view_unique('v_no','TRUCK')]
    delete_by_task_name =  st.selectbox("Select",unique_list)
    if st.button("Delete"):
        db.delete_truck(delete_by_task_name)
        st.warning("Deleted: '{}'".format(delete_by_task_name))

    with st.expander("Updated Data"):
        result = db.view_all_data('TRUCK')
        clean_df = pd.DataFrame(result,columns=  ['Vehicle No','Name','Phone No'])
        st.dataframe(clean_df)