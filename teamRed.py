import streamlit as st


from auth import log_in

from styles import Style, GREEN, RED, BLUE, YELLOW
from helpers import teams, hacker_view

style = Style(RED)
target = [team for team in teams if team.color == style.color][0]

st.set_page_config(page_title=target.name, initial_sidebar_state="collapsed")
st.markdown(style.global_styles, unsafe_allow_html=True)


if 'counter' not in st.session_state:
    st.session_state.counter = 0
    st.session_state.logged = False



def show_sidebar():
    st.sidebar.markdown(f"""
        ## Menu:
        - [Strona Główna](#witaj-w-projekcie-{target.name.lower()}) 
        - [Fabryka](#fabryka)
        - [Zastosowania](#zastosowania)
        - [Reaktor](#reaktor)
    """)

st.markdown(f"## {target.dziedzina} - Projekt {target.name.upper()}")

if not st.session_state.logged:
    st.write("Enter the secret key to continue")

if log_in():  # TODO: remove True
    hacker_view() # TODO: uncomment
    show_sidebar()
    st.markdown(f"""
    ### Witaj w projekcie {target.name} 
    {target.welcome_text}

    ### Zastosowania
    {target.dziedzina} można zostać wykorzystana do stworzenia wielu wartościowych produktów. Oto kilka z nich (kolejność ma znaczenie):
    1. **Skażenie radioaktywne**:
        - opis: umożliwiają wyeliminowanie celów po zetknięciu z nimi. Nie działa przeciw zaszczepionym. Nie zużywa się.
        - substraty: `Plazma`, `Ciekły azot`,`Biomateriały`, `Nanomateriały`

    1. **Skażenie biologiczne**:
        - opis: umożliwiają wyeliminowanie celów po zetknięciu z nimi. Działa przeciw zaszczepionym. Można użyć tylko 6 razy.
        - substraty: `Biomateriały`, `Nanomateriały`, `Plazma`, `Ciekły azot`

    1. **Szczepionka** 
        - opis: zapewnia odporność na toksyny krótkodystansowe.
        - substraty: `Biomateriały`, `Ciekły azot`, `Plazma` `Nanomateriały`

    1. **Strój ochronny**
        - opis: zapewnia odporność na wszelkie toksyny.
        - substraty: `Biomateriały`, `Plazma`, `Nanomateriały`, `Ciekły azot`

    1. **Haptyka**
        - opis: Ułatwia regenerację tkanek o 40%.
        - substraty: `Nanomateriały`, `Ciekły azot`, `Plazma`, `Biomateriały`
        
    1. **Bomba termiczna**
        - opis: Wybuchająca bomba termiczna, która momentalnie na 30 sekund zamraża budynek uniemożliwiając wkroczenie lub opuszczenie go. 
        - substraty: `Ciekły azot`, `Nanomateriały`, `Plazma`, `Biomateriały`
    
    ### Reaktor
    W reaktorze możesz przeprowadzić reakcję chemiczną, która pozwoli Ci uzyskać jeden z produktów zastosowań. Przed syntezą należy wyłączyć reaktor.
    Należy pozbawić reaktor odpowiednich składników w następującej kolejności:

    <p style="size: 40px"> {target.reactor_sequence} </p>

    """, unsafe_allow_html=True)
    