import streamlit as st
import time
import subprocess
import urllib.parse
import google.generativeai as genai
from PIL import Image
from util import tts
st.set_page_config(page_title="Roast Me Chef!!",
                   page_icon="👨‍🍳",initial_sidebar_state='expanded',
                   menu_items={
                       'Get Help':"https://www.linkedin.com/in/kartikey-tiwari-32bb90187/",
                       "Report a bug":"https://github.com/Iamkartikey44",
                       "About" : "# This is a fun project that generates roasts in the style of Gordon Ramsay!"
                   }
                   )

if "roaster_selection" not in st.session_state:
    st.session_state["roaster_selection"] = {}
if 'audio' not in st.session_state:
    st.session_state['audio'] = {}


def twitter_link(roast_text):
    twitter_text = f"{roast_text} @Kartikey_44"
    encoded_twitter_text = urllib.parse.quote(twitter_text)
    st.markdown(f"[Share on Twitter](https://twitter.com/intent/tweet?text={encoded_twitter_text}) 🐦",unsafe_allow_html=True)
def media_output(uploaded_file,roaster_name):
    display_choice = st.sidebar.selectbox("Choose display option:",['Text','Audio','Video'])

    if display_choice=='Audio' and st.sidebar.button("Play Roast Audio"):
        play_audio(roaster_name)
    elif display_choice=='Video' and st.sidebar.button("Generate Video"):
        generate_video(uploaded_file,roaster_name)

def play_audio(roaster_name):
    if  not st.session_state.audio.get(roaster_name):
        
        roast_content = st.session_state.roaster_selection.get(roaster_name)
        response = tts(roast_content)

        if response.status_code==200:
            st.session_state['audio'][roaster_name] = response.json()[0]['link']
            st.audio(st.session_state.audio.get(roaster_name),format='audio/mp3')
        else:
            st.error("Failed to synthesize speech.")
    else:
        st.audio(st.session_state.audio.get(roaster_name),format='audio/mp3')

def generate_video(uploaded_file,roaster_name):
    if 'roast' in st.session_state and not  st.session_state.get('audio'):
        
        roast_content = st.session_state.roaster_selection.get(roaster_name)

        response = tts(roast_content)
        if response.status_code == 200:
            st.session_state['audio'][roaster_name] = response.json()[0]['link']
        else:
            st.error("Failed to synthesize speech. Unable to generate video.")
            return  # Exit if audio cannot be generated
    if st.session_state.get('audio'):

        audio_file = st.session_state.audio.get(roaster_name)
        video_file = f'{roaster_name}_{time.time()}_output_video.mp4'
        
        subprocess.run([
            'ffmpeg','-loop','1','-i',uploaded_file.name,'-i',audio_file,
            '-c:v','libx264','-c:a','aac','-strict','experimental',
            '-b:a','192k','-shortest',video_file
        ])  
        st.video(video_file)

    else:
        st.error("Audio data is not available. Please try generating the audio first.")

def generate_roast(uploaded_file,anger_level,roaster_name):
    processing_gif = f"chefgifs/{roaster_name.split(' ')[0]}2.gif"
    st.image(processing_gif,use_column_width=True)
    img = Image.open(uploaded_file)

    google_api_key= st.secrets['GOOGLE_API_KEY']
    genai.configure(api_key=google_api_key)
    safety_settings = [
        {
            'category':"HARM_CATEGORY_HARASSMENT",
            'threshold':"BLOCK_NONE"
        },
        {
            'category':"HARM_CATEGORY_HATE_SPEECH",
            'threshold':"BLOCK_NONE"
        },
        {
            'category':"HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold":"BLOCK_NONE"
        },
        {
            "category":"HARM_CATEGORY_DANGEROUS_CONTENT",
            'threshold':'BLOCK_NONE'
        }
    ]
    vision_model = genai.GenerativeModel('gemini-pro-vision',safety_settings=safety_settings)
    mood = "not that angry" if anger_level < 50 else "very angry and lots of swearing"
    resp = vision_model.generate_content([f"Generate a short roast about the food in the style of {roaster_name}, Mood: {mood}.",img],stream=True)
    resp.resolve()
    st.session_state['roaster_selection'][roaster_name] = resp.text
    #st.write(st.session_state['roaster_selection'])
    content = st.session_state['roaster_selection'][roaster_name]
    st.write(f"**Roast Generated:** {content}")



st.title("Roast Me Chef!!")

st.sidebar.header("Instructions")
st.sidebar.info("Upload an image, set the anger level, and get roasted in the style similar to Gordon Ramsay's roast!")
st.sidebar.markdown("Connect with me on Twitter [linkedIn.com/Kartikey](https://www.linkedin.com/in/kartikey-tiwari-32bb90187/) or on [GitHub/KartikeyTiwari](https://github.com/Iamkartikey44) for more cool projects!")

initial_gif = 'chefgifs/gif_1.gif'
st.image(initial_gif,caption='Think yous a top chef innit?! Get ready to be roasted!',use_column_width=True)

uploaded_file = st.file_uploader("Choose an image...",type=['jpeg','jpg','png'])
anger_level = st.slider("Select the anger level: ",0,100,50)
roaster_name = st.selectbox("Select who want you roast your Food...",["Gordon Ramsay","Carry Minati","Lakshay Chaudhary","Samay Raina","Thugesh"],)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='Uploaded Image.',use_column_width=True)
    uploaded_gif = f"chefgifs/{roaster_name.split(' ')[0]}.gif"
    st.image(uploaded_gif,caption='Click the button...Dont be scared..',use_column_width=True)
     
    if st.button("Roast/Rate my meal, Chef!") or st.session_state['roaster_selection']:
        if not st.session_state['roaster_selection']:
            generate_roast(uploaded_file,anger_level,roaster_name)
    
        else:
            st.write(f"**Roast Generated:** {st.session_state['roaster_selection'][roaster_name]}")
            twitter_link(st.session_state['roaster_selection'][roaster_name])
            

        media_output(uploaded_file,roaster_name)
else:
    st.write("Upload an image to get started.")            





