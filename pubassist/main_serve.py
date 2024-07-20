from shiny import render, reactive
import shinyswatch


import pubassist

from pubassist import Assistant


def server(input, output, session):

    assistant = Assistant()

    @render.text
    @reactive.event(input.get_feedback_button)
    def fetch_groq_response():
        return assistant.get_response(input.user_prompt._value)

    @render.image
    def render_logo():
        img = {
            "src": "/Users/mds8301/Development/pubassistant/images/DALL·E Logo 2024-07-10.png",
            "width": "100px%",
            "fill": False,
            "style": {"object-fit": "contain"},
        }
        print("img called")
        return img
