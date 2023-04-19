import streamlit as st

import pandas as pd

import database as db
st.title("PES1UG20CS072, PES1UG20CS073, PES1UG20CS106, PES1UG20CS123")
st.subheader("Citizen Details")


menu = ['Create ✅','Read 👨‍💻','Update','Delete ❌']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create ✅":
    st.subheader("Add citizen details")
  
    col1,col2 = st.columns(2)

    with col1:
        uid = st.text_input("Enter User ID")
        dob = st.date_input("Date of Birth")
        phno = st.text_input("Phone Number")
        pan_no = st.text_input("PAN Card")

    with col2 :
        name = st.text_input("Name")
        gender = st.selectbox("Gender",["Male","Female"])
      
    st.write("Address Details")
    
    col3,col4,col5 = st.columns(3)

    with col3:
        house_no = st.text_input("House No")
        city = st.selectbox("City",['Bengaluru','Myosre','Mandya'])
        
    with col4:
        street = st.text_input("Street")
        
    with col5:
        area_name = st.text_input("Area")
        aid = st.text_input("Area ID")

        
    if st.button("Register Citizen"):
        db.add_data_citizen(uid,name,gender,dob,phno,house_no,street,area_name,city,aid)
        st.success("Successfully added citizen  : {}".format(uid))
       
   
   
elif choice == "Read 👨‍💻":
    st.subheader("View citizen details")
    res = db.view_all_data('CITIZEN')

    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Aadhar No','Name','Gender','dob','Phno','House_no','Street','Area_name','City','Area ID'])
        st.dataframe(df)
    

elif choice == "Update":
    st.subheader("Update citizen details")
    res = db.view_all_data('CITIZEN')
 
    with st.expander("Current data"):
        df = pd.DataFrame(res,columns = ['Aadhar No','Name','Gender','dob','Phno','House_no','Street','Area_name','City','Area ID'])
        st.dataframe(df)

    list_of_citizen = [i[0] for i in db.view_unique('aadhar_no','CITIZEN')]

    selected_citizen = st.selectbox("Citizen Details to Edit",list_of_citizen)

    selected_res = db.get_citizen(selected_citizen)

    if selected_res:
        uid = selected_res[0][0]
        name = selected_res[0][1]
        gender = selected_res[0][2]
        dob = selected_res[0][3]
        phno = selected_res[0][4]
        hno = selected_res[0][5]
        street = selected_res[0][6]
        aname = selected_res[0][7]
        city = selected_res[0][8]
        aid = selected_res[0][9]

        col1,col2 = st.columns(2)

        with col1:
            new_uid = st.text_input("Enter User ID",uid)
            new_dob = st.date_input("Date of Birth",dob)
            new_phno = st.text_input("Phone Number",phno)

        with col2 :
            new_name = st.text_input("Name",name)
            new_gender = st.selectbox("Gender",["Male","Female"])
        
        st.write("Address Details")
        
        col3,col4,col5 = st.columns(3)

        with col3:
            new_house_no = st.text_input("House No",hno)
            new_city = st.selectbox("City",['Bengaluru','Myosre','Mandya'])
            
        with col4:
            new_street = st.text_input("Street",street)
            
        with col5:
            new_area_name = st.text_input("Area",aname)
            new_aid = st.text_input("Area ID",aid)
            
        
        if st.button("Update Citizen"):
            
            db.edit_citizen_data(new_uid,new_name ,new_gender ,new_dob,new_phno,new_house_no ,new_street,new_area_name ,new_city ,new_aid ,uid)
            st.success("Successfully edited citizen : {}".format(uid))

    res2 = db.view_all_data('CITIZEN')

    with st.expander("Updated data"):
        df2 = pd.DataFrame(res2,columns = ['Aadhar No','Name','Gender','dob','Phno','House_no','Street','Area_name','City','Area ID'])
        st.dataframe(df2)
    
elif choice == "Delete ❌":
    st.subheader("Delete citizen details")
    with st.expander("View Data"):
        result = db.view_all_data('CITIZEN')
			# st.write(result)
        clean_df = pd.DataFrame(result,columns= ['Aadhar No','Name','Gender','dob','Phno','House_no','Street','Area_name','City','Area ID'])
        st.dataframe(clean_df)

    unique_list = [i[0] for i in db.view_unique('aadhar_no','CITIZEN')]
    delete_by_task_name =  st.selectbox("Select",unique_list)
    if st.button("Delete"):
        db.delete_citizen(delete_by_task_name)
        st.warning("Deleted: '{}'".format(delete_by_task_name))

    with st.expander("Updated Data"):
        result = db.view_all_data('CITIZEN')
		# st.write(result)
        clean_df = pd.DataFrame(result,columns= ['Aadhar No','Name','Gender','dob','Phno','House_no','Street','Area_name','City','Area ID'])
        st.dataframe(clean_df)



    
