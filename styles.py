
GREEN = "green", "#04bd20"
BLUE = "blue", "#00a9ff"
RED = "red", "#bd2004"
YELLOW = "yellow", "#ffff0f"

class Style:
    def __init__(self, color):
        self.color = color

        with open(f"assets/biohazard_{self.color[0]}.txt", "r") as text_file:
            encoded_string = text_file.read()


        self.global_styles = f"""
        <style> 
            [data-testid="stHeader"] {{display: none}}
            [data-testid="stToolbar"] {{display: none}}
            .css-y5kc8u {{display: none}} <-- remove .md anchors -->

            header {{
                background-color: #000000;
                padding: 0.5rem;
                margin-bottom: 1rem;
                border-bottom: 1px solid {self.color[1]};
            }}

            [data-testid=stAppViewContainer]{{
                background-image: url(data:image/png;base64,{encoded_string});
                background-repeat: no-repeat;
                background-size: 60em;
                background-position: center;
            }}

            .stMarkdown > div > ul > li {{
                color: #ffffff00; /* make dots invisible */
                background-color: #000000;
                padding: 0.5rem;
                margin-bottom: 1rem;
                border: 1px solid {self.color[1]};
                text-decoration: none;
                transition: font-size 0.3s ease; 
                font-size: 1rem;
            }}
            .stMarkdown > div > ul > li:hover {{
                font-size: 1.1rem;
            }}

            a:-webkit-any-link {{
                text-decoration: none;
                color: {self.color[1]};
            }}
        </style>
        """

def stick(color):
    if color == "B":
        selected_color = BLUE[1]
    elif color == "G":
        selected_color = GREEN[1]
    elif color == "R":
        selected_color = RED[1]
    elif color == "Y":
        selected_color = YELLOW[1]
    else:
        print("ERROR: wrong color")
        return None
    return f"<span style='color:{selected_color}; font-size:40px'>☣</span>"

off_navbar = """
<style>
    [data-testid="collapsedControl"] {display: none}
</style>
"""

