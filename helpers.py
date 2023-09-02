import streamlit as st
import subprocess, time, os

from styles import GREEN, BLUE, RED, YELLOW, PURPLE
from teams import Apex, Cryogenics, Nexus, Plasma, Spectra

def hacker_view():
    process = subprocess.Popen(["hollywood"], preexec_fn=os.setsid)

    progress_bar = st.progress(0)
    for procent in range(100):
    #     if procent < 13:
    #         msg = "## Connecting with external servers..."
    #     elif procent < 25:
    #         msg = "## Retreiving data..."
    #     elif procent < 50:
    #         msg = "## Decrypting data..."
    #     elif procent < 75:
    #         msg = "## Checking for vulnerabilities..."
    #     elif procent < 100:
    #         msg = "## Entering the mainframe..."
        if procent > 70:
            time.sleep(0.07)
        progress_bar.progress(procent + 1)
        time.sleep(0.1)
    time.sleep(10)
    os.killpg(os.getpgid(process.pid), 15) 


class Team:
    def __init__(self, name, color, dziedzina, welcome_text, reactor_sequence):
        self.name = name
        self.color = color
        self.dziedzina = dziedzina
        self.welcome_text = welcome_text
        self.reactor_sequence = reactor_sequence

teams = [
    Team("Nexus", GREEN, "BioTech'a", Nexus.welcome_text, Nexus.reactor_sequence),
    Team("Plasma", BLUE, "Energia jądrowa", Plasma.welcome_text, Plasma.reactor_sequence),
    Team("Cryogenics", YELLOW, "Technologie termalne", Cryogenics.welcome_text, Cryogenics.reactor_sequence),
    Team("Apex", RED, "Sztuczna inteligencja", Apex.welcome_text, Apex.reactor_sequence),
    Team("Spectra", PURPLE, "Fizyka kwantowa", Spectra.welcome_text, Spectra.reactor_sequence)
]

