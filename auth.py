import streamlit as st
import random, time, os, subprocess

def set_password(password):
    with open("./password.txt", "w") as f:
        f.write(password)

def get_password():
    with open("./password.txt", "r") as f:
        return f.read()

def fail_login():
    if st.session_state.counter > 0 :
        st.error("Wrong secret key!")
    st.session_state.counter += 1
    return False


def success_login():
    """Log in and refresh the page"""
    st.success("Logged in successfully!")
    st.session_state.logged = True
    time.sleep(2)
    st.experimental_rerun()

def log_in():
    if st.session_state.logged:
        return True

    password = st.text_input(label="Secret key:", value="", type="password")

    if (PASSWD := get_password()) != "":
        if password == PASSWD:
            return success_login()
        else:
            return fail_login()

    if st.session_state.counter < random.randint(2, 10):
        return fail_login()
    else:
        set_password(password)
        return success_login()
        
