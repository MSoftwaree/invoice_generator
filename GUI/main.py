from frames import Frames
from pathlib import Path
import customtkinter
import os


# region Load GUI default settings
project_path = os.getenv("APPDATA") + "/MSoftware/Invoice_generator/"
setting_file = project_path + 'defaults.txt'

if Path(setting_file).is_dir() is False:
    setting_file = "../utils/defaults.txt"


def read_settings():
    return read_file(setting_file)['language'], read_file(setting_file)['appearance'], read_file(setting_file)['theme']


def read_file(file_path):
    with open(file_path, "r") as f:
        lines = [line.removesuffix('\n') for line in f.readlines()]
        settings = {}

        for line in lines:
            key, value = line.split("=")
            settings[key] = value

    return settings


language, appearance_mode, theme_color = read_settings()

customtkinter.set_appearance_mode(appearance_mode)
customtkinter.set_default_color_theme(theme_color)
# endregion

# region Create GUI
app = customtkinter.CTk()
if language == "english":
    app.geometry("1330x700")
else:
    app.geometry("1400x700")
app.resizable(False, False)
app.title("Invoice generator")

frames = Frames(app, language)

frames.seller_frame()
frames.buyer_frame()
frames.data_frame()
frames.settings_frame()
frames.generate_button()
frames.signature()
frames.status_info()
# endregion

app.mainloop()
