import streamlit as st
from my_Sidebar import Sidebar
import random

st.set_page_config(
    page_title="Homepage",
    page_icon="🏡",)

#Sidebar
Sidebar.Decorate()
Sidebar.feedback()

#Function
def music_player(audio):
    audio_select = audio
    audio_file = open(audio_select, 'rb')
    audio_bytes = audio_file.read()
    path, song = audio_select.split('/')
    song_name, dot = song.split('.')
    song_name, artist = song_name.split(' - ')

    st.text(f'Now Playing 🎵\n'
            f'{song_name}\n'
            f'By: {artist}')
    st.audio(audio_bytes, format='audio')

def music_option():
    option = st.radio('Wanna Listen to Some Random Classical Music?', ['Yay', 'Nay'], 0)
    if option == 'Yay':
        music_random()

    if option == 'Nay':
        music_select()

def music_random():
    song = [
        'my_Sidebar/Piano Sonata No 11, Rondo alla Turca - Wolfgang Amadeus Mozart.mp3',
        'my_Sidebar/Piano Sonata No 1, Allegro - Ludwig van Beethovan.mp3',
        'my_Sidebar/Symphony No 40, Molto Allegro - Wolfgang Amadeus Mozart.mp3',
        'my_Sidebar/Waltz No 2 - Dmitri Shostakovich.mp3'
    ]
    audio = random.choice(song)
    music_player(audio)

def music_select():
    selection = st.selectbox('Choose By Yourself Here!',
                             ['Playlist',
                              'Piano Sonata No 11, Rondo alla Turca',
                              'Piano Sonata No 1, Allegro',
                              'Symphony No 40, Molto Allegro',
                              'Waltz No 2',
                              'Hidden Track'
                              ], 0)

    if selection == 'Piano Sonata No 11, Rondo alla Turca':
        audio = 'my_Sidebar/Piano Sonata No 11, Rondo alla Turca - Wolfgang Amadeus Mozart.mp3'
        music_player(audio)

    elif selection == 'Piano Sonata No 1, Allegro':
        audio = 'my_Sidebar/Piano Sonata No 1, Allegro - Ludwig van Beethovan.mp3'
        music_player(audio)

    elif selection == 'Symphony No 40, Molto Allegro':
        audio = 'my_Sidebar/Symphony No 40, Molto Allegro - Wolfgang Amadeus Mozart.mp3'
        music_player(audio)

    elif selection == 'Waltz No 2':
        audio = 'my_Sidebar/Waltz No 2 - Dmitri Shostakovich.mp3'
        music_player(audio)

    elif selection == 'Hidden Track':
        audio = 'my_Sidebar/Hidden Track - Hidden Cat.mp3'
        music_player(audio)

#Home
st.title(f'Hello World!')
st.image('https://media.tenor.com/Iu6K9JSRnREAAAAC/van-gogh.gif', use_column_width='always')
music_option()