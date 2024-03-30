from manager import * # Interacts with the JSON songs file and validate pw
import streamlit as st  # Streamlit website
from random import choice  # Pick a random song from a list
from PIL import Image  # Load the favicon
from configs import *  # Custom page styles
import time  # Show instructions only temporarily

# Function for password checking w/ Streamlit secrets
def is_correct_password(user_password):
    password = st.secrets["modify_db_password"]
    if user_password == password:
        return True
    else:
        return False

# Load favicon
favicon = Image.open('favicon.webp')

# Name tab and show favicon
st.set_page_config(page_title="El DJ Español", page_icon=favicon)

# Import and apply the custom styling configs
page_configs = [remove_st_ui, hide_enter_to_submit, hide_made_with_s]
for custom_style in page_configs:
    st.markdown(custom_style, unsafe_allow_html=True)

# Make a songs list based on the JSON file
songs_dict = dict(get_songs())
songs = list(songs_dict.keys())

# Check if a song has already been selected, if not, pick a random one
if 'song_name' not in st.session_state:
    st.session_state.song_name = choice(songs)

# Get the URL of the title
url = songs_dict[st.session_state.song_name]

# Shows the song name on the top of the page
st.title(f'"{st.session_state.song_name}"')

# Set the now_playing song to own var for use later
now_playing = st.session_state.song_name

# Loads the video
st.video(url)

# Create three columns for content alignment
col1, col2, col3 = st.columns([1,2,1])

# Places control buttons
with col1:
    # Refresh button
    if st.button("🔄 Nueva"):
        # Pick a new random song and update the session state
        st.session_state.song_name = choice(songs)
        st.rerun()

# Open in YouTube button
with col3:  # Even though in col 3, must come first to be seen
    st.link_button("📺 Ver en YouTube", url)

# Form for adding a song
with st.form("Add a song to the list", clear_on_submit=True):
    st.subheader("📝 Agregar tu propia música")

    user_input_title = st.text_input("🎵 Nombre de la cancion")
    user_input_url = st.text_input("🔗 URL de YouTube para la canción")
    user_password_guess = st.text_input("🔑 Contraseña", type='password')
    if st.form_submit_button('Agregar'):
        if is_correct_password(user_password_guess) is True:
            add_song(user_input_title, user_input_url)
            st.success("Canción agregada!", icon="✅")
            st.balloons()
        else:
            st.error("Contraseña incorrecta. Tu canción no ha sido agregada.")

# Form for removing the current song from the playlist
with st.form("remove_song", clear_on_submit=True):
    st.subheader("🗑️ Eliminar una canción de la lista")

    song_name_pop = st.selectbox("🎵 Elige una canción para eliminar", list(get_songs()), index=None, placeholder="Haga clic en el menú desplegable o escriba aquí...")
    user_password_guess = st.text_input("🔑 Contraseña", type='password')
    if st.form_submit_button("Remove song"):
        if is_correct_password(user_password_guess) is True:
            remove_status = remove_song(song_name_pop)
            if remove_status == 'complete':
                st.success("¡Canción eliminada!", icon="✅")
            else:
                st.error("Esa canción no está en esta lista de reproducción.")
        else:
            st.error("Contraseña incorrecta. La canción actual no ha sido eliminada.")


# Playlist info
st.title("🎧 Canciones en esta lista:")

# Download button for the playlist info
with open('songs.json', 'r') as download_file:
    song_list_dict = dict(json.load(download_file)) # Load as dict to auto translate escape codes back

    document_download = "🇪🇸 Lista de reproducción 🎤\n\n\n\n" # Adds a doc title

    for key in song_list_dict.keys():
        document_download += f"{key} - {song_list_dict[key]}\n\n"

    st.download_button("📥 Descarga las URL", data=document_download, file_name="lista_de_reproducción.txt")

# List all the songs in the playlist
index = 1
for song in get_songs():
    st.text(f"{str(index)}) {song}")
    index += 1