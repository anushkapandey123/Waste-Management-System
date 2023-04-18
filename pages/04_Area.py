import streamlit as st

import database as db
import pandas as pd
st.title("PES1UG20CS072, PES1UG20CS073, PES1UG20CS106, PES1UG20CS123")
st.subheader("Area Details")



menu = ['Create ✅','Read 👨‍💻','Update','Delete ❌']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create ✅":
    st.subheader("Add area")

    col1,col2 = st.columns(2)

    with col1:
        aid = st.text_input("Enter Area ID")

    with col2 :
        aname = st.text_input("Enter Area Name")
    

    col3,col4 = st.columns(2)

    with col3:
        lat = st.text_input("Latitude")
    
    with col4:
        long = st.text_input("Longitude")
    
    if st.button("Register Area"):
        
        db.add_data_area(aid,aname,lat,long)
        st.success("Successfully added area : {}".format(aid))
   
elif choice == "Read 👨‍💻":
    st.subheader("View area")

    res = db.view_all_data('AREA')
    
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Area ID','Name','Latitude','Longitude'])
        st.dataframe(df)
  
elif choice == "Update":
    st.subheader("Update area")
  
    res = db.view_all_data('AREA')
    

    with st.expander("Current data"):
        df = pd.DataFrame(res,columns = ['Area ID','Name','Latitude','Longitude'])
        st.dataframe(df)

    list_of_areas = [i[0] for i in db.view_unique('area_id','AREA')]

    selected_area = st.selectbox("Area to Edit",list_of_areas)

    selected_res = db.get_area(selected_area)

    if selected_res:
        aid = selected_res[0][0]
        aname = selected_res[0][1]
        lat = selected_res[0][2]
        long = selected_res[0][3]

        col1,col2 = st.columns(2)

        with col1:
            new_aid = st.text_input("Enter Area ID",aid)

        with col2 :
            new_aname = st.text_input("Enter Area Name",aname)
        

        col3,col4 = st.columns(2)

        with col3:
            new_lat = st.text_input("Latitude",lat)
        
        with col4:
            new_long = st.text_input("Longitude",long)
        
        if st.button("Update Area"):
            
            db.edit_task_data(new_aid,new_aname,new_lat,new_long,aid,aname,lat,long)
            st.success("Successfully edited area : {}".format(aid))

    res2 = db.view_all_data('AREA')

    with st.expander("Updated data"):
        df2 = pd.DataFrame(res2,columns = ['Area ID','Name','Latitude','Longitude'])
        st.dataframe(df2)


    
elif choice == "Delete ❌":
    st.subheader("Delete area")
    with st.expander("View Data"):
        result = db.view_all_data('AREA')
			# st.write(result)
        clean_df = pd.DataFrame(result,columns= ['Area ID','Name','Latitude','Longitude'])
        st.dataframe(clean_df)

    unique_list = [i[0] for i in db.view_unique('aadhar_no','CITIZEN')]
    delete_by_task_name =  st.selectbox("Select",unique_list)
    if st.button("Delete"):
        db.delete_data(delete_by_task_name)
        st.warning("Deleted: '{}'".format(delete_by_task_name))

    with st.expander("Updated Data"):
        result = db.view_all_data('CITIZEN')
		# st.write(result)
        clean_df = pd.DataFrame(result,columns=['Area ID','Name','Latitude','Longitude'])
        st.dataframe(clean_df)
