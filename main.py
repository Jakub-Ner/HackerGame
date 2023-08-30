import streamlit as st



import subprocess, time, os, signal

from auth import log_in
from styles import global_styles, off_navbar

st.set_page_config(page_title="Home")
st.markdown(global_styles, unsafe_allow_html=True)


if 'counter' not in st.session_state:
    st.session_state.counter = 0
    st.session_state.logged = False


def hacker_view():
    process = subprocess.Popen(["hollywood"], preexec_fn=os.setsid)
    time.sleep(10)
    os.killpg(os.getpgid(process.pid), 15) 


def show_sidebar():
    st.sidebar.markdown("""
        ## Menu:
        - [Strona Główna](/) 
        - [Fabryka](#fabryka) <br>
        - [Zastosowania](#zastosowania)
        - [Surowce](#surowce)
    """
    
    )
st.markdown("## Gemstone Management System")

if not st.session_state.logged:
    # st.markdown(off_navbar, unsafe_allow_html=True)

    st.write("Enter the secret key to continue")

if log_in():
    hacker_view()
    show_sidebar()
    st.markdown("### Welcome to the Gemstone Management System")
    st.markdown("""

    ### Add Gemstone 
    Here you can add a new gemstone to the database.
    """)
    