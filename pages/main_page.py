


import streamlit as st
import webbrowser
import json
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import base64
import email
import smtplib

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
st.image("homepage1.jpg", width=800)

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
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )
# Path to store user data
USER_DATA_FILE = "users_data.json"

# Function to load user data
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            return json.load(file)
    else:
        return {}

# Function to save user data
def save_user_data(data):
    with open(USER_DATA_FILE, "w") as file:
        json.dump(data, file)
        return

# Load existing users
users = load_user_data()
# Function to send a welcome email
server = smtplib.SMTP('smtp.gmail.com', 587)

# Registration page
def registration_page():
    st.title("User Registration")
    
    name = st.text_input("Enter your name:")
    email = st.text_input("Enter your email:")
    password = st.text_input("Enter a password:", type="password")
    confirm_password = st.text_input("Confirm your password:", type="password")

    if st.button("Register"):
        if not name or not email or not password:
            st.error("All fields are required!")
        elif password != confirm_password:
            st.error("Passwords do not match!")
        elif email in users:
            st.error("This email is already registered!")
        else:
            # Add user to the database
            users[email] = {"name": name, "password": password}
            save_user_data(users)
            st.success("Registration successful! You can now log in.")
            autoplay_audio("applause.WAV")
            st.balloons()
            st.snow()
            server.starttls()
            server.login('remedy.rem401@gmail.com', 'qmxcdormmpybjdrl')
            from_email = 'remedy.rem401@gmail.com'
            to_email = email
            subject = 'message'
            body = f'''Hi {name},

            Thank you for registering with us! We're thrilled to have you on board.

            Best regards,
            Remedy '''
            message = f"Subject: {subject}\n\n{body}"
            server.sendmail(from_email, to_email, message)
            server.quit()
# Login page
def login_page():
    st.title("User Login")
    
    email = st.text_input("Enter your email:")
    password = st.text_input("Enter your password:", type="password")

    if st.button("Login"):
        if email in users and users[email]["password"] == password:
            st.session_state["user_name"] = users[email]["name"]
            st.success(f"Welcome back, {users[email]['name']}!")
            webbrowser.open('http://localhost:9989')
        else:
            st.error("Invalid email or password!")

# Navigation logic
if "user_name" not in st.session_state:
    st.session_state["user_name"] = None

page = st.sidebar.selectbox("Navigation", ["Register", "Login"])

if page == "Register":
    registration_page()
elif page == "Login":
    login_page()

