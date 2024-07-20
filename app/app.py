from shiny import *
import shinyswatch

import pubassist as pb

main_app_ui = pb.app_ui()

app = App(main_app_ui, server=pb.server)
