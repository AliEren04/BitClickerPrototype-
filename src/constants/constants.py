#Importing necessary libraries with files 
from pygame_menu import themes
#constant(fixed) variables are declared here and imported if necessary to other files.
window_height = 420
window_width = 420 
window_size = window_width, window_height
theme = themes.THEME_DARK.copy()
theme_dark = themes.THEME_DARK.copy()
theme_light = themes.THEME_DEFAULT.copy()
theme_solar = themes.THEME_SOLARIZED.copy()
theme_blue = themes.THEME_BLUE.copy()


def update_theme(new_theme):
    global theme
    theme = new_theme