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
image = Image.open("reiki.jpg")
resized_image = image.resize((150, 70))  # Width: 200px, Height: 150px

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

st.write("A bell will ring every 3 minutes. Change the reiki point when the bell rings according to the image shown below. Scroll down to access the video.")
st.write("    ")

st.image("reikipoints1.jpg")
st.write("    ")
st.video("https://www.youtube.com/watch?v=O4AJrtSvy_M&t=2s", format="video/mp4", start_time=0)
