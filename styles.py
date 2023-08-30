import streamlit as st

global_styles = """
<style> 
    [data-testid="stHeader"] {display: none}
    [data-testid="stToolbar"] {display: none} 
    .css-y5kc8u {display: none} <-- remove .md anchors -->

    header {
        background-color: #000000;
        padding: 0.5rem;
        margin-bottom: 1rem;
        border-bottom: 1px solid #00ff00;
    }


    .stMarkdown > div > ul > li {
        color: #ffffff00; /* make dots invisible */
        background-color: #000000;
        padding: 0.5rem;
        margin-bottom: 1rem;
        border: 1px solid #00ff00;
        text-decoration: none;
    }

  a:-webkit-any-link {
    text-decoration: none;
    color: #00ff00;
}
</style>
"""

off_navbar = """
<style>
    [data-testid="collapsedControl"] {display: none}
</style>
"""

