import streamlit as st
import webbrowser
from PIL import Image

# CSS to hide the header and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        color: white;  
    }
    </style>
    """, 
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([4,4,4])
image = Image.open("eft.jpg")
resized_image = image.resize((2000, 300))  # Width: 200px, Height: 150px

# Display the resized image
with col2:
    st.image(resized_image)

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #61279c;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    
    """
    <style>
    
    .stButton > button {
        background-color: #61279c;  
        color: white;               
        border-radius: 12px;        
        padding: 10px 20px;         
        font-size: 16px;            
        border: none;               
        cursor: pointer;           
    }
    <style>

"""
, unsafe_allow_html=True)

if st.sidebar.button("Home"):
    webbrowser.open('http://localhost:9988')

if st.sidebar.button("Explore"):
    webbrowser.open('http://localhost:9989')
if st.sidebar.button("Benefits"):
    webbrowser.open('http://localhost:9995')

if st.sidebar.button("About"):
    webbrowser.open('http://localhost:9994')

st.write("Tap each of the EFT points while giving the following affirmations :- ")
st.write("    ")
st.image("eftaff.png",width=800)

st.image("eft1.jpg",width=800)
st.write("    ")
