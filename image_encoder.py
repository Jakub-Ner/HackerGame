import base64

img_names = [
    "biohazard_green",
    "biohazard_blue",
    "biohazard_red",
    "biohazard_yellow",
]

for img_name in img_names:
    with open(f"assets/{img_name}.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    with open(f"assets/{img_name}.txt", "w+") as text_file:
        text_file.write(encoded_string.decode('utf-8'))