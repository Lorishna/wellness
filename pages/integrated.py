mport streamlit as st
import webbrowser
from PIL import Image
import time

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
image = Image.open("integrated.jpg")
resized_image = image.resize((275, 70))  

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

st.write("This is a 20 minute integrated practice combining reiki, meditation, breathing and EFT - all in one")

color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">5 MINUTE MEDITATION</p>', unsafe_allow_html=True)
st.video("https://www.youtube.com/watch?v=LDs7jglje_U", format="video/mp4", start_time=0)

color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">EMOTIONAL FREEDOM TECHNIQUE - 6 minute practice</p>', unsafe_allow_html=True)
st.write("Tap each of the EFT points for 40 seconds (according to the timer) while giving the following affirmations :- ")
st.write("    ")
st.image("eftaff.png",width=800)

st.image("eft1.jpg",width=800)
st.write("    ")

# Input for the timer duration
duration = st.number_input("Enter countdown time in seconds (optimal time - 40 seconds):", min_value=1, max_value=3600, value=10)

# Start button
if st.button("Start Timer"):
    
    for cycle in range(1, 10):  # Repeat 9 times
        st.write(f"### Cycle {cycle} of 9")
        
        # Initialize the progress bar and text
        progress_bar = st.progress(0)
        timer_placeholder = st.empty()

        for remaining in range(duration, -1, -1):
            # Update the progress bar
            progress_percentage = ((duration - remaining) / duration) * 100
            progress_bar.progress(int(progress_percentage))
            
            # Format the time as MM:SS
            mins, secs = divmod(remaining, 60)
            time_str = f"{mins:02}:{secs:02}"
            
            # Update the timer text
            timer_placeholder.markdown(f"## {time_str}")
            time.sleep(1)
        
        # Complete the progress bar for the current cycle
        progress_bar.progress(100)
        
        # Add a short pause between cycles
        if cycle < 9:  # Skip the pause after the last cycle
            time.sleep(2)  # 2-second break between cycles

    st.success("All cycles completed!")

color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">REIKI - 6 minute practice</p>', unsafe_allow_html=True)
st.write("A bell will ring every 3 minutes. Change the reiki point when the bell rings. First reiki point - third eye chakra, second - heart chakra")
st.write("    ")
st.image("chakra.jpg")
st.write("    ")
st.video("https://www.youtube.com/watch?v=O4AJrtSvy_M&t=2s", format="video/mp4", start_time=0,end_time=360)

color = "violet"
size = 25
st.markdown(f'<p style="color:{color}; font-size:{size}px;">BREATHING - 4 minute practice</p>', unsafe_allow_html=True)
st.audio("breathingaudio.M4A",start_time=0,end_time=240)
