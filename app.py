import streamlit as st

from PIL import Image

main_image = Image.open('main_banner.png')
st.image(main_image,use_column_width='always')
st.title("Team 6 - PES1UG20CS072, PES1UG20CS073, PES1UG20CS106, PES1UG20CS123")
st.subheader("Team 6 - Anushka Pandey, Anushka Siri Raghunandan, B Praneetha, Devika S")
def main():
    st.title("Project 3")
    
    st.subheader("WASTE MANAGEMENT SYSTEM - UE20CS301")

    main1_image = Image.open('Screenshot (11075).png')
    st.image(main1_image,use_column_width='always')

    st.write("Please navigate to the side menubar and choose the table of your choice")

if __name__ == '__main__':
    main()

