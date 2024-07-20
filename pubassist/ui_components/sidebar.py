from shiny import *
import shinyswatch


class SideBar:

    @property
    def theme_picker(self):
        return shinyswatch.theme.zephyr

    @property
    def mode_switcher(self):
        mode_switch = ui.navset_pill(ui.nav_control(ui.input_dark_mode()))
        return mode_switch

    def render(self):
        sidebar = ui.page_sidebar(ui.sidebar(self.theme_picker, self.mode_switcher))
        return sidebar
