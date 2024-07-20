from shiny import *
import shinyswatch

from pubassist import SideBar, MainUI


def app_ui():
    app = ui.page_fluid(
        SideBar().render(),
        MainUI().render(),
        ui.output_text("fetch_groq_response"),
    )
    return app
