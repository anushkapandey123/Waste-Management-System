
import streamlit as st

import database as db
import pandas as pd
st.title("PES1UG20CS123")
st.subheader("Area Has A Truck Details")



menu = ['Create ✅','Read 👨‍💻','Update','Delete ❌']
choice = st.sidebar.selectbox("Menu",menu)

if choice == "Create ✅":
    st.subheader("Add details")

    col1,col2 = st.columns(2)

    with col1:
        aid = st.text_input("Enter Area ID")

    with col2 :
        vid = st.text_input("Enter Vehicle No")
    
    if st.button("Register Details"):
        
        db.add_data_area_truck(aid,vid)
        st.success("Successfully added data : {} , {}".format(aid,vid))
   
elif choice == "Read 👨‍💻":
    st.subheader("View details")

    res = db.view_all_data('AREAHASATRUCK')
    
    with st.expander("View all"):
        df = pd.DataFrame(res,columns = ['Area ID','Vehicle No'])
        st.dataframe(df)
  
elif choice == "Update":
    st.subheader("Update details")
  
    res = db.view_all_data('AREAHASATRUCK')
 
    with st.expander("Current data"):
        df = pd.DataFrame(res,columns = ['Area ID','Vehicle No'])
        st.dataframe(df)

    list = [i[0] for i in db.view_unique('vid','AREAHASATRUCK')]

    selected = st.selectbox("Detail to Edit",list)

    selected_res = db.get_area_truck(selected)

    if selected_res:
        aid = selected_res[0][0]
        vid = selected_res[0][1]
       
        col1,col2 = st.columns(2)

        with col1:
            new_aid = st.text_input("Enter Area ID",aid)

        with col2 :
            new_vid = st.text_input("Enter Area Name",vid)
        
        if st.button("Update Details"):
            
            db.edit_area_truck_data(new_aid,new_vid,aid,vid)
            st.success("Successfully edited ")

    res2 = db.view_all_data('AREAHASATRUCK')

    with st.expander("Updated data"):
        df2 = pd.DataFrame(res2,columns = ['Area ID','Vehicle No'])
        st.dataframe(df2)


    
elif choice == "Delete ❌":
    st.subheader("Delete details")
    with st.expander("View Data"):
        result = db.view_all_data('AREAHASATRUCK')
			# st.write(result)
        clean_df = pd.DataFrame(result,columns= ['Area ID','Vehicle No'])
        st.dataframe(clean_df)

    unique_list = [i[0] for i in db.view_unique('vid','AREAHASATRUCK')]
    delete_by_task_name =  st.selectbox("Select",unique_list)
    if st.button("Delete"):
        db.delete_area_truck(delete_by_task_name)
        st.warning("Deleted: '{}'".format(delete_by_task_name))

    with st.expander("Updated Data"):
        result = db.view_all_data('AREAHASATRUCK')
		# st.write(result)
        clean_df = pd.DataFrame(result,columns=['Area ID','Vehicle No'])
        st.dataframe(clean_df)