import streamlit as st
import base64
import requests
from io import BytesIO
from PIL import Image

st.set_page_config(page_title="Meydi's 25th Birthday web!", layout="centered")

# Image URL (Google Drive)
background_image_url = "https://drive.google.com/uc?export=view&id=1ESVRPxsojj3t2GB17NU7Y3kWt8a3Ud4m"
main_img_url = "https://drive.google.com/uc?export=view&id=1hMnBGt4mSf_D7nkwLup_bTktVyDwRhze"


# Background as Base64
# with open("https://drive.google.com/uc?export=view&id=1ESVRPxsojj3t2GB17NU7Y3kWt8a3Ud4m", "rb") as image_file:
#     encoded_string = base64.b64encode(image_file.read()).decode()
#     background_image = f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/jpg;base64,{encoded_string}");
#         background-size: cover;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     h1, div {{
#         color: #fffaf0;
#         text-shadow: 1px 1px 2px #444;
#     }}
#     </style>
#     """
#     st.markdown(background_image, unsafe_allow_html=True)

# Fetch image from URL using requests
response = requests.get(background_image_url)
if response.status_code == 200:
    # Convert image to base64
    encoded_string = base64.b64encode(response.content).decode()
    background_image = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_string}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    h1, div {{
        color: #fffaf0;
        text-shadow: 1px 1px 2px #444;
    }}
    </style>
    """
    st.markdown(background_image, unsafe_allow_html=True)
else:
    st.error("Failed to load background image.")

# Heading & content
st.markdown("<h1 style='text-align: center; color: #D8E9A8;'>Happy Birthday Meydiku sayang a.k.a bebskiiii!</h1>", unsafe_allow_html=True)
# st.image("https://drive.google.com/uc?export=view&id=1hMnBGt4mSf_D7nkwLup_bTktVyDwRhze", caption="Bebski cantik 😍", use_container_width=True)
response = requests.get(main_img_url)
if response.status_code == 200:
    # Open the image using PIL
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="Bebski cantik 😍", use_container_width=True)
else:
    st.error("Failed to load image.")

st.markdown("""
<div style='text-align: center; color: white; font-size: 20px;'>
    CIEEE 25 TAHUNNNNN, rasanya kayak baru kemarin masih 19 tahun 😝
    <br><br>
    Semoga di umur kamu yang 25 ini semua yang kamu inginkan dapat tercapai yaaa bebskiii, aamiinnnnn
    <br><br>
    Love you forevermore and more after my love ❤️
    <br><br>
    Here's to another year of adventurous yet calm and relaxing life, together. 👩🏻‍❤️‍👨🏻
</div>
""", unsafe_allow_html=True)

# Music
audio_file = open('assets/musics/birthday_song.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', start_time=57)

st.markdown("""
<div style='text-align: center; color: white; font-size: 20px;'>
    Pemilihan lagu di atas maksudnya justru karena 25 tahun inilah kita harus semakin sayang sama diri kita sendiri hehehehe
    <br><br>
    (Jujur gaktau makna lagunya apa sebenernya, tapi semoga pesanku tersampaikan ya ✌)
</div>
""", unsafe_allow_html=True)

st.balloons()