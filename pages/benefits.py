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
image = Image.open("benefits.jpg")
resized_image = image.resize((200, 70))  # Width: 200px, Height: 150px

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

color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">REIKI</p>', unsafe_allow_html=True)
st.write("Reiki is a gentle, non-invasive healing practice that promotes relaxation, reduces stress, and supports overall well-being. It helps alleviate physical discomfort, enhance energy levels, improve sleep, and boost the body’s natural healing processes. Emotionally, Reiki fosters balance, clarity, and resilience, while slritually, it encourages self-awareness, inner peace, and alignment of energy centers. Safe and complementary, Reiki can be used alongside medical treatments to enhance holistic healing without side effects.")

st.write("  ")
color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">MEDITATION</p>', unsafe_allow_html=True)
st.write("Meditation offers numerous benefits for the mind, body, and spirit. It reduces stress, anxiety, and negative emotions by promoting relaxation and mindfulness. Physically, it can lower blood pressure, improve sleep, and enhance immune function. Meditation boosts focus, mental clarity, and emotional resilience while fostering self-awareness and inner peace. It also supports spiritual growth, helping individuals feel more connected to themselves and their surroundings, making it a powerful tool for holistic well-being.")

st.write("  ")
color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">EMOTIONAL FREEDOM TECHNIQUE</p>', unsafe_allow_html=True)
st.write("EFT involves tapping on certain points of your face and body while thinking about negative emotions or stress you want to release. EFT may be helpful in the treatment of depression, PTSD, and phobias. Tapping may also curb food cravings and aid in weight loss.")

st.write("  ")
color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">BREATHING</p>', unsafe_allow_html=True)
st.write("Breathing techniques offer several benefits to your body including reducing your blood pressure and heart rate, reducing anxiety, improving sleep and improving relaxation.")
